class Bicicleta:
    def __init__(self, cor, modelo, ano,valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano 
        self.valor = valor

    def buzinar(self):
        print("Plim, plim")

    def parar(self):
        print("Parando bicicleta...")
        print("3...2...1...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmmm...")

    def __str__(self):
        return f"Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"
    


b1 = Bicicleta("azul marinho", "caloi", 2023, 700)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor,b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta ("rosa", "Monark", 2022, 500)
b2.__str__()