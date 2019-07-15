C = {"RED": "\033[1;31m", "BLUE": "\033[1;34m", "CYAN": "\033[1;36m",
     "YEL": "\033[1;33m", "MAG": "\033[1;35m", "RES": "\033[0;0m"}


def cria_matriz(linha, coluna):
    matriz = [[0 for i in range(coluna)] for j in range(linha)]
    return matriz


def preenche_matriz(matriz, vetor_a, povoar_c):
    for i in range(len(matriz)):
        print("A =", vetor_a)
        for j in range(len(matriz[i])):
            matriz[i][j] = int(input("Processo {}: Qtd de recurso do tipo {}:".format(i + 1, j + 1)))
            if povoar_c:
                if matriz[i][j] <= vetor_a[j]:
                    vetor_a[j] -= matriz[i][j]
                else:
                    while matriz[i][j] > vetor_a[j]:
                        print("\n   # Qtd do recurso ultrapassa o valor permitido. Informe outro valor:")
                        matriz[i][j] = int(input("\nProcesso {}: Qtd de recurso do tipo {}:".format(i + 1, j + 1)))
                    vetor_a[j] -= matriz[i][j]

    return matriz


def printa_matriz(matriz, matriz_final):
    for i in range(len(matriz)):
        if not matriz_final:
            print("    {} - p{}".format(matriz[i], i + 1))
        else:
            print("    {}".format(matriz[i]))


def printa_tudo(e, a, c, r=None, matriz_final=False):
    print("\n{}\n\nE = {}".format("-" * 40, e))
    print("\nA = {}\n".format(a))
    print("C = ")
    printa_matriz(c, matriz_final)
    if r is not None:
        print("\nR = ")
        printa_matriz(r, matriz_final)
    print("\n{}\n".format("-" * 40))


def executa_processo(a_disponivel, corrente, requisito):
    deadlock = False
    qtd_processos = len(corrente)
    qtd_recursos = len(corrente[0])
    a_anterior = list(a_disponivel)
    for i in range(qtd_processos):  # Verifica se o processo conseguiu executar.
        if corrente[i] != 'ok':
            for j in range(qtd_recursos):
                if requisito[i][j] > a_disponivel[j]:
                    deadlock = True
                    break
                else:
                    deadlock = False
            if not deadlock:
                for l in range(qtd_recursos):
                    a_disponivel[l] += corrente[i][l]
                corrente[i] = "ok"
                requisito[i] = "ok"
    while "ok" in corrente:  # Remove o processo que executou com sucesso.
        corrente.remove("ok")
        requisito.remove("ok")
    return a_anterior


def algoritmo_do_banqueiro(a_disponivel, corrente, requisito):
    a_anterior = []
    while a_disponivel != a_anterior and len(corrente) != 0:
        a_anterior = executa_processo(a_disponivel, corrente, requisito)
    if len(corrente) == 0:
        return True
    elif a_disponivel == a_anterior:
        return False
