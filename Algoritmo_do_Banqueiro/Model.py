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


def printa_matriz(matriz):
    for i in range(len(matriz)):
        print("    {} - p{}".format(matriz[i], i + 1))


def printa_tudo(e, a, c, r=None):
    print("\n{}\n\nE = {}".format("-" * 40, e))
    print("\nA = {}\n".format(a))
    print("C = ")
    printa_matriz(c)
    if r is not None:
        print("\nR = ")
        printa_matriz(r)
    print("\n{}\n".format("-" * 40))
