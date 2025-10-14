class personagem():
    def __init__(self, altura, olhos, nome, sexo, comida, emoção, odeio):
        self.altura = altura
        self.olhos = olhos
        self.nome = nome
        self.sexo = sexo
        self.comidas = comida
        self.estado = emoção
        self.affs = odeio
        
    def vida(self):
        return print(f' Meu nome é {self.nome} ')
    def comida(self):
        return print (f'Minha comida favorita é {self.comidas} 🍡 ')
    def papai_hytalo(self):
        return print(f'Estou {self.estado}, pois papai Hytalo foi preso')
    def chato(self):
        return print(f'Eu odeio o {self.affs} 😡 ')
    def eyes(self):
        return print(f'Meus olhinos são {self.olhos} 👁️ ')
    