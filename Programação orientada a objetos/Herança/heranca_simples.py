class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Lingando o motor...")

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    pass


moto = Motocicleta("Azul", "ABC1234", 2)
moto.ligar_motor()

carro = Carro("Preto", "BCD2345", 4)
carro.ligar_motor()

caminhao = Caminhao("Branco", "CDE3456", 8)
caminhao.ligar_motor()