class Mar():
    def __init__(self, tamanho, cores, espécie, sexo, habitat, tem_escamas):
        self.Tamanho = tamanho
        self.cores = cores
        self.espécie = espécie
        self.sexo = sexo
        self.habitat = habitat
        self.escamas = tem_escamas
        
    def vida(self):
        return print(f' Sou um(a) {self.espécie} vivendo pacificamente pelo oceano... 🪼 ')
    def perigo(self):
        return print ('Sou um animal selvagens  🦂 ')
    def especie(self):
        return print (f'Meu habitat é nos(a) {self.habitat} ')
    def pacifico(self):
        return print ('Eu sou uma espécie muito pacifica 🐟 ')