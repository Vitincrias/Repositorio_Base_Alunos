class Pessoa():
    def __init__(self, nome, trabalho, cor_olhos, cabelo, sexo, cor_pele, tipo_cabelo):
        self._nome = nome
        self.__trabalho = trabalho
        self._cor_olhos = cor_olhos
        self._cabelo = cabelo
        self._sexo = sexo
        self._cor_pele = cor_pele
        self._cabelostips = tipo_cabelo
    
    
    
    def viver(self):
        return print(f' Sou um(a) pessoa chamada {self.nome} ')
    def trabalhar(self):
        return print (f' Eu trabalho como {self.trabalho} na fábrica de programadores')
    def olhar(self):
        return print (f' A cor dos meus olhos são {self.cor_olhos} ')
    def dizer_genero(self):
        return print (f' Meu genêro é {self.sexo}')
    def dizer_cabelo(self):
        return print (f' O tipo do meu cabelo é {self.cabelostips}')
    def dizer_pele(self):
        return print (f' A cor da minha pele é {self.cor_pele}')
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def trabalho(self):
        return self.__trabalho
    
    @property
    def cor_olhos(self):
        return self._cor_olhos
    
    @property
    def cabelo(self):
        return self._cabelo
    
    @property
    def sexo(self):
        return self._sexo
    
    @property
    def cor_pele(self):
        return self._cor_pele
    
    @property
    def tipo_cabelo(self):
        return self._cabelostips
    
    @nome.setter
    def nome(self, cor):
        self._nome = 'cor'