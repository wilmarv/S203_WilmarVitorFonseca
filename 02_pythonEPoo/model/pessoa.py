class Pessoa():
    def __init__(self,nome,idade,sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
    
    def envelhecer(self):
        self.idade += 1