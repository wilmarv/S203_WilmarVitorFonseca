from model.pessoa import Pessoa

class Atleta(Pessoa):
    aposentado = False

    def __init__(self, nome, idade,peso):
        super().__init__(nome, idade)
        self.peso = peso
    
    def aquecer(self):
        print(f'Atleta {self.nome} está aquecido')
    
    def aposentar(self):
        self.aposentado = True

class Corredor(Atleta):
    def correr(self):
        print(f"Corredor {self.nome} está correndo...")

class Nadador(Atleta):
    def nadar(self):
        print(f"Nadador {self.nome} está nadando...")

class Ciclista(Atleta):
    def pedalar(self):
        print(f"Ciclista {self.nome} está pedalando...")


class Triatleta(Corredor,Nadador,Ciclista):
    pass