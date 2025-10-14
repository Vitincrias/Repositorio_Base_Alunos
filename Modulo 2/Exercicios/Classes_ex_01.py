class Mar():
    def __init__(self, tamanho, cores, Espécie, sexo, habitat, tem_escamas):
        self.Tamanho = tamanho
        self.cores = cores
        self.Espécie = Espécie
        self.sexo = sexo
        self.habitat = habitat
        self.escamas = tem_escamas
        
    def vida(self):
        return print(f' Sou um(a) {self.Espécie} vivendo pacificamente pelo oceano... 🪼 ')
    def perigo(self):
        return print ('Sou um animal selvagens  🦂 ')
    def especie(self):
        return print (f'Meu habitat é nos(a) {self.habitat} ')
    def pacifico(self):
        return print ('Eu sou uma Espécie muito pacifica 🐟 ')
    def fazer_som(self):
        return print(f' Sou um(a) {self.Espécie} vivendo pacificamente pelo oceano... 🪼 ')