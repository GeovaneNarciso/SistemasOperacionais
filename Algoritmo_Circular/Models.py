class Processo:
    def __init__(self, nome, tempo):
        self.nome = nome
        self.tempo = tempo
        self.estado = "Pronto"
        self.t_espera = 0
        self.t_processamento = 0
