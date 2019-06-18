C = {"RED": "\033[1;31m", "BLUE": "\033[1;34m", "CYAN": "\033[1;36m",
     "YEL": "\033[1;33m", "MAG": "\033[1;35m", "RES": "\033[0;0m"}


def fim_da_fila(fila, ttc_ativo):
    primeiro = fila[0]
    for i in range(len(fila)-1):
        fila[i] = fila[i+1]
    fila[-1] = primeiro
    troca_estado(fila, ttc_ativo)


def printa_fila(fila, processos, tempo, ttc_ativo):
    atualiza_processo(fila, processos)
    if ttc_ativo:
        print(C["BLUE"] + "\n----- TEMPO ", tempo, "-----" + C["RES"] + C["MAG"] + " ### TROCA DE CONTEXTO ###" +
              C["RES"], "\n               FILA: Início <<< ", end='')
    else:
        print(C["BLUE"] + "\n----- TEMPO ", tempo, "-----" + C["RES"], "\n               FILA: Início <<< ", end='')
    for p in fila:
        print("{} | ".format(p.nome), end='')
    print("<<< Fim\nProcessos: ")
    for p in processos:
        if p.estado == "Execução":
            print(C["CYAN"] + p.nome + ": Tempo: " + str(p.tempo) + " | T.Processador: " + str(p.t_processamento) +
                  " | T.Espera: " + str(p.t_espera) + " | Estado: " + p.estado +
                  " | TurnAround: " + str(p.t_processamento + p.t_espera) + C["RES"])
        elif p.estado == "Pronto":
            print(C["YEL"] + p.nome + ": Tempo: " + str(p.tempo) + " | T.Processador: " + str(p.t_processamento) +
                  " | T.Espera: " + str(p.t_espera) + " | Estado: " + p.estado +
                  " | TurnAround: " + str(p.t_processamento + p.t_espera) + C["RES"])
        else:
            print(C["RED"] + p.nome + ": Tempo: " + str(p.tempo) + " | T.Processador: " + str(p.t_processamento) +
                  " | T.Espera: " + str(p.t_espera) + " | Estado: " + p.estado +
                  " | TurnAround: " + str(p.t_processamento + p.t_espera) + C["RES"])


def troca_estado(fila, ttc_ativo):
    if not ttc_ativo:
        for p in fila:
            if p.t_processamento != p.tempo:
                p.estado = "Pronto"
        fila[0].estado = "Execução"
    else:
        for p in fila:
            if p.t_processamento != p.tempo:
                p.estado = "Pronto"


def atualiza_processo(fila, processos):
    for p in fila:
        for p2 in processos:
            if p.nome == p2.nome:
                p2 = p


def executa_termino(fila, processos, ttc):
    if fila[0].tempo == fila[0].t_processamento:
        fila[0].estado = "Término"
        atualiza_processo(fila, processos)
        fila.remove(fila[0])
        if len(fila) > 0:
            troca_estado(fila, ttc)
        return True
    else:
        return False


def aumenta_espera_prontos(fila, ttc_ativo):
    if not ttc_ativo:
        for p in fila:
            if p.estado == "Pronto":
                p.t_espera += 1
    else:
        for p in fila:
            p.t_espera += 1


def tempo_medio_espera(processos):
    tme = 0
    for p in processos:
        tme += p.t_espera
    return tme / len(processos)


def tempo_medio_turnaround(processos):
    tmt = 0
    for p in processos:
        tmt += p.tempo + p.t_espera
    return tmt / len(processos)
