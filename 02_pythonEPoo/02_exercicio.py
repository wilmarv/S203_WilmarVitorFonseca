from model.cidadao import Cidadao

nomeCidadao =input("Informe o nome do cidadao:\n")
idadeCidadao =input("Informe a idade do cidadao:\n")
sexoCidadao =input("Informe o sexo do cidadao:\n")
cpfCidadao =input("Informe o cpf do cidadao:\n")

cadastroCidado = Cidadao(nomeCidadao,idadeCidadao,sexoCidadao,cpfCidadao)
cadastroCidado.informacaoCidadao()
