from model.atletismo import Corredor,Nadador,Triatleta

#instanciando corredor:
print("\n-=-=-=-=-=-=-=-=-=-==-=-=-=-==-=-=-=-==-=-=-=-=\n")
corredor_1 = Corredor("Vanderlei",27,75)
corredor_1.aquecer()
corredor_1.correr()
print("\n-=-=-=-=-=-=-=-=-=-==-=-=-=-==-=-=-=-==-=-=-=-=\n")
#Instanciando nadador:

nadador_1 = Nadador("Gustavo",35,80)
print("Está aposentado?: ")
if(nadador_1.aposentado):
    print("Sim\n")
else:
    print("Não\n")

nadador_1.nadar()
nadador_1.envelhecer()
nadador_1.aposentar()
print("Agora já está aposentado?")
print( "Sim" if nadador_1.aposentado else "Não")
print("\n-=-=-=-=-=-=-=-=-=-==-=-=-=-==-=-=-=-==-=-=-=-=\n")

triatleta_1 = Triatleta("Joseane",28,72)
triatleta_1.correr()
triatleta_1.nadar()
triatleta_1.pedalar()

print("\n")