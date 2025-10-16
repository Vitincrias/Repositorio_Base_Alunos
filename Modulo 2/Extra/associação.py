class Pessoa:
    def __init__(self, nome: str, disciplina: str):
        self.nome = nome
        self.disciplina = disciplina

class SalaDeAula:
    def __init__(self, numero: int, capacidade: int):
        self.numero = numero
        self.capacidade = capacidade
        print(f"Sala {self.numero} está disponível.")

class Lazaro(Pessoa):
    def dar_aula(self, sala: SalaDeAula):
        print(f"O Prof. {self.nome} de {self.disciplina} está dando aula na sala {sala.numero}.")

sala_Do_Lazaro = SalaDeAula(1, 20)
professor = Lazaro("Lázaro", "Programação em python")
professor.dar_aula(sala_Do_Lazaro)

