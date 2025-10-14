class Animal:
    def __init__(self, Espécie):
        self.Espécie = Espécie
        
    def comer(self):
        print(f"{self.Espécie} está comendo. ")
        
    def fazer_som(self):
        print(f"{self.Espécie} está fazendo um som genérico. ")