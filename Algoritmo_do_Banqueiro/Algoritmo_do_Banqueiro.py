def main():
    def cria_matriz(linha, coluna):
        matriz = [[int(input("Processo {}: Qtd de recurso do tipo {}:".format(j+1, i+1)))
                   for i in range(coluna)] for j in range(linha)]
        return matriz

    def printa_matriz(matriz):
        print("C =")
        for i in range(len(matriz)):
            print("   p{} - {}".format(i+1, matriz[i]))

    vetor_e = [0] * int(input("Qtd de recursos distintos: "))
    print()

    for i in range(len(vetor_e)):
        vetor_e[i] = int(input("Qtd de recursos do tipo {}:".format(i + 1)))

    vetor_a = list(vetor_e)

    qtd_processos = int(input("\nQtd de processos: "))
    matriz_c = cria_matriz(qtd_processos, len(vetor_e))

    print("\nE =", vetor_e)
    print("\nA =", vetor_a)
    print()
    printa_matriz(matriz_c)


if __name__ == '__main__':
    main()
