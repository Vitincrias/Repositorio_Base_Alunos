class Passaro():
    def __init__(self, Tamanho, Cores, Espécie, Sexo):
        self.Tamanho = Tamanho
        self.Cores = Cores
        self.Espécie = Espécie
        self.Sexo = Sexo
    def cantar(self):
        return print(f' Sou um {self.Espécie} cantando uma bela canção 🎶 ')
    def voar(self):
        return print ('Batendo as asas e: voando...')
    def medo(self):
        return print(f' Sou um {self.Espécie} cantando uma melodia mortal 🩸 ')
    def colorido(self):
        return print(f' Sou um {self.Espécie} com as penas coloridas 🌈 ')
    def comendo(self):
        return print(f' Sou um {self.Espécie} que come as migalhas de pão 🥖 ')
    def cores(self):
        return print(f' A cor da minhas penas são {self.Cores} ')
    def fazer_som(self):
         return print(f' Sou um {self.Espécie} cantando uma bela canção 🎶 ')
    
Passaro1 = Passaro (0.14,['Marrom', 'Branco', 'Cinza'], 'Pardal', 'M')
Passaro1.cantar()
Passaro1.voar()

Passaro2 = Passaro (70.0,['Preto'], 'Corvo', 'M')
Passaro2.medo()
Passaro2.voar()

Passaro3 = Passaro (55.0,['Vermelho', 'Azul', 'Amarelo', 'Verde','Branco','Preto'], 'Arara', 'F')
Passaro3.colorido()
Passaro3.voar()

Passaro4 = Passaro (55.0,['Preto', 'Cinza', 'Azul escuro', 'Marrom', 'Branco'], 'Pombo', 'M')
Passaro4.comendo()
Passaro4.cores()
Passaro4.voar()