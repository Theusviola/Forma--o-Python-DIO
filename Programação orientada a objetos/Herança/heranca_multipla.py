class Animal:
    def __init__(self, numero_patas):
        self.numero_patas = numero_patas
        super().__init__(numero_patas)


class Mamifero(Animal):
    def __init__(self, numero_patas, cor_pelo):
        self.cor_pelo = cor_pelo
        super().__init__(numero_patas)

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Ave(Animal):
    def __init__(self, numero_patas):
        self.numero_patas = numero_patas
        super().__init__(numero_patas)

class Ornitorrinco(Mamifero, Ave):
    pass


gato = Gato(4, "Preto")
print(gato)

ornitorrinco = Ornitorrinco(2, "Vermelho")
print(ornitorrinco)