from Model import *


def main():
    vetor_e = [0] * int(input("Qtd de recursos distintos: ")+"\n")  # Cria vetor de recursos existentes
    for l in range(len(vetor_e)):                                             # Preenche vetor
        vetor_e[l] = int(input("Qtd de recursos do tipo {}:".format(l + 1)))  #
    vetor_a = list(vetor_e)  # Cria vetor de recursos disponíveis
    qtd_processos = int(input("\nQtd de processos: "))   # Cria matriz de alocação corrente
    matriz_c = cria_matriz(qtd_processos, len(vetor_e))  #
    print("\nPovoar a matriz de alocação corrente:")  # Preenche matriz corrente
    preenche_matriz(matriz_c, vetor_a, True)          #
    printa_tudo(vetor_e, vetor_a, matriz_c)           # Exibe informações
    matriz_r = cria_matriz(qtd_processos, len(vetor_e))  # Cria matriz de requisições
    print("\nPovoar a matriz de requisições:")         # Preenche matriz de requisições
    preenche_matriz(matriz_r, vetor_a, False)          #
    printa_tudo(vetor_e, vetor_a, matriz_c, matriz_r)  # Exibe informações
    if algoritmo_do_banqueiro(vetor_a, matriz_c, matriz_r):  # ALGORITMO DO BANQUEIRO
        print(C["CYAN"] + "Não existe deadlock." + C["RES"])
    else:
        print(C["RED"] + "Existe deadlock." + C["RES"])
    printa_tudo(vetor_e, vetor_a, matriz_c, matriz_r, True)


if __name__ == '__main__':
    main()
