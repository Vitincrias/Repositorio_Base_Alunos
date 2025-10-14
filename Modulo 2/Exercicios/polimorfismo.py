def vtzin():
    x = "Olá, Mundo!"
    print(len(x))

    minha_tupla = ("Maçã", "Banana", "Cereja")
    print(len(minha_tupla))

    este_dicionário = {
        "marca": "Chevrolet",
        "modelo": "Opala",
        "ano": 1969
    }
    print(len(este_dicionário))
    
from classe_pai import Animal
from classe_pássaro import Passaro
from Classes_ex_01 import Mar

animal1 = Animal('Rasga-Mortalha')
animal2 = Passaro(70.0, ['Azul', 'Azul escuro', 'Branco', 'Preto'],'Arara azul', 'M')
animal3 = Mar(4, ['Branco', 'Azul claro'], 'Beluga', 'F', 'Águas geladas do Ártico', False)

def comunicar(qualquer_animal):
    print(f"Tentando comunicação com {qualquer_animal.Espécie}")
    qualquer_animal.fazer_som()
    
print("-"*50)
comunicar(animal1)

print("-"*50)
comunicar(animal2)

print("-"*50)
comunicar(animal3)

# HAVE MERCY