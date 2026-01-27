print("ola mundo".capitalize())
print("OLA MUNDO".capitalize())
print("OLA MUNDO".isupper())

from modelos import Carro
from pessoa import Pessoa

c1 = Carro("BMW", "X1", cor="Azul", ano=2010)
c2 = Carro("Ford", "Focus", cor="Amarelo", ano=2015)

print(c1.marca)
c1.marca = "Baverische Motoren Werke"

print(c1.marca)
print(c2.marca)

print("------------------")
print(c1.cor)
c1.mudarCor("Vermelho")
print(c1.cor)

print("Velocidade: 100 km/h\nTempo: 2 minutos\nDistancia percorrida -> ", c1.andar(100, 2))

p1 = Pessoa("joao", 1.75, 70000)
print(f"Nome: {p1.nome}\nAltura: {p1.altura}\n\nPeso: {p1.peso}g")
print("Depois de comer:", p1.comer(["arroz", "feijao", "carne"]), "g")

print("Idade antes de envelhecer:", p1.idade)
for _ in range(20):
    p1.envelhecer()
print("Idade depois de envelhecer:", p1.idade)
print("Altura depois de envelhecer:", p1.altura)
print("------------------")