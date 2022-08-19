class Pai():
    nome = "Carlos"
    sobrenome = "Oliveira"
    residencia = "Ilha Bela"
    olhos = "azuis"

class Filha(Pai):
    nome ="Luciana"
    olhos ="castanhos"

class Neta(Filha):
    nome = "Maria"

print(f"Nomes:\n{Pai.nome}\n{Filha.nome}\n{Neta.nome}\n")
print(f"Residências:\n{Pai.residencia}\n{Filha.residencia}\n{Neta.residencia}\n")
print(f"Olhos:\n{Pai.olhos}\n{Filha.olhos}\n{Neta.olhos}\n")