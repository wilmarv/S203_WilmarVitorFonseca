from model.pessoa import Pessoa

class Cidadao(Pessoa):
    def __init__(self, nome, idade,sexo,cpf):
        super().__init__(nome, idade,sexo)
        self.cpf = cpf

    def informacaoCidadao(self):
        print("\n-=-=-=-=-=-=-=-=-=-==-=-=-=-==-=-=-=-==-=-=-=-=\n")
        print(f"O {self.nome} com {self.idade} anos do sexo {self.sexo}")
        print(f"Cpf: {self.cpf} ")
        print("\n-=-=-=-=-=-=-=-=-=-==-=-=-=-==-=-=-=-==-=-=-=-=\n")