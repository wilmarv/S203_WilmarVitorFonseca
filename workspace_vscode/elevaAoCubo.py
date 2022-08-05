import math

val = int(input("Entre com o valor que sera elevado ao cubo!\n"))

valorAoCubo = math.pow(val,3)

if valorAoCubo >= 100:
    print(f'O numero {valorAoCubo} e maior que 100!')
else:
    print(f'O numero {valorAoCubo} e menor que 100!')