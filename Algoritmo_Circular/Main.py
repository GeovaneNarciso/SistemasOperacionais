from Models import *
from Functions import *


def algoritmo_circular(fila, quantum, ttc, tempo):
    processos = list(fila)
    ttc_ativo = False
    troca_estado(fila, ttc_ativo)
    cont_quantum = 0
    cont_ttc = ttc
    while len(fila) > 0:
        printa_fila(fila, processos, tempo, ttc_ativo)
        tempo += 1
        if ttc_ativo:  # Todos prontos, aumenta espera e printa.
            cont_ttc += 1
            if cont_ttc < ttc:
                aumenta_espera_prontos(fila, ttc_ativo)
                input("\nEnter para continuar...")
                continue
            else:
                aumenta_espera_prontos(fila, ttc_ativo)
                input("\nEnter para continuar...")
                ttc_ativo = False
                troca_estado(fila, ttc_ativo)
                continue
        if quantum == 0:  # Não precisa ir p/ fim da fila.
            fila[0].t_processamento += 1
            aumenta_espera_prontos(fila, ttc_ativo)
            if executa_termino(fila, processos, ttc_ativo):
                if ttc > 0:
                    if len(fila) > 1:
                        ttc_ativo = True
                        cont_ttc = 0
                if len(fila) > 0:
                    troca_estado(fila, ttc_ativo)
        elif cont_quantum < quantum:
            if quantum - 1 == cont_quantum:  # Abaixo verifica se termina ou vai p/ fim da fila.
                fila[0].t_processamento += 1
                aumenta_espera_prontos(fila, ttc_ativo)
                if not executa_termino(fila, processos, cont_ttc):
                    if len(fila) > 1:
                        if ttc > 0:
                            if len(fila) > 1:
                                ttc_ativo = True
                                cont_ttc = 0
                        fim_da_fila(fila, ttc_ativo)
                else:
                    if ttc > 0:
                        if len(fila) > 1:
                            ttc_ativo = True
                            cont_ttc = 0
                    troca_estado(fila, ttc_ativo)
                cont_quantum = 0
            else:  # Abaixo verifica se termina.
                fila[0].t_processamento += 1
                aumenta_espera_prontos(fila, ttc_ativo)
                cont_quantum += 1
                if executa_termino(fila, processos, ttc_ativo):
                    if ttc > 0:
                        if len(fila) >= 1:
                            ttc_ativo = True
                            cont_ttc = 0
                    if len(fila) > 0:
                        troca_estado(fila, ttc_ativo)
                    cont_quantum = 0
        else:
            if len(fila) > 0:
                fim_da_fila(fila, ttc_ativo)
                cont_quantum = 0
        input("\nEnter para continuar...")
    printa_fila(fila, processos, tempo, ttc_ativo)
    print("\nTempo Médio de Espera: {:.2f} u.t.".format(tempo_medio_espera(processos)))
    print("Tempo Médio de TurnAround: {:.2f} u.t.".format(tempo_medio_turnaround(processos)))


def main():
    fila = [0] * int(input("Quantidade de processos:"))
    for i in range(len(fila)):
        fila[i] = Processo(input("Nome do {}º processo: ".format(i+1)),
                           int(input("Tempo do {}º processo:".format(i + 1))))
    quantum = int(input("Valor do Quantum:"))
    ttc = int(input("Valor do Tempo de Troca de Contexto:"))

    algoritmo_circular(fila, quantum, ttc, tempo=0)


if __name__ == '__main__':
    main()
