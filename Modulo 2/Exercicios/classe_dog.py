from classe_pai import Animal
from classes_ex_03 import Pessoa
from classe_gato import Gato

class Cachorro (Animal):
    def __init__(self, nome, raça):
        super().__init__(nome)
        self.raça = raça
    
    def fazer_som(self):
        print(f"{self.nome} está latindo: Au Au!")
        
    def abanar_rabo(self):
        print(f"{self.nome} está abanando o rabo. ")
        
scooby_Doo  = Cachorro('Scooby Doo', 'Lulu-da-pomerânia')
scooby_Doo.fazer_som()
scooby_Doo.abanar_rabo()

humano1 = Pessoa('Salcicha','CLT', 'Verdes', 'Castanho', 'M', 'Branco','Ondulado')
humano1.trabalhar()
humano1.dizer_cabelo()

Garfield = Gato('Garfield')
Garfield.fazer_som()