from Model import *


def main():
    def remove_item(matriz):
        if "ok" in matriz:
            for i in range(len(matriz)):
                if matriz[i] == 'ok':
                    matriz.remove(matriz[i])
                    if len(matriz) > 1:
                        remove_item(matriz)
                    else:
                        return True
                else:
                    return True
        else:
            return True

    a = ["ok", 1, "ok"]

    remove_item(a)


if __name__ == '__main__':
    main()
