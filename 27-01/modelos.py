
"""
marca
modelo
ano
num_km
"""

class Carro:
    def __init__(self, marca: str, modelo: str, ano: int, cor: str):
        self.marca = marca.title()
        self.modelo = modelo.title()
        self.ano = ano
        self.num_km = 0
        self.cor = cor

    def mudarCor(self, cor:str):
        self.cor = cor.title()

    """
    assuma que o carro se desloca a uma velocidade constante
    
    a velocidade deve ser expressa em km/h
    o tempo em minutos
    
    a funcao deve atualizar o num_km do carro
    """
    def andar(self, velocidade: int, tempo: float):
        distancia = (velocidade * tempo) / 60
        self.num_km += distancia
        return distancia

    # calcule o consumo de combustivel total do carro
    # assuma que o consumo e constante (xL por km)
    # define o x onde fizer mais sentido
    def consumo_combustivel(self, consumo_por_km: float):
        total_consumo = self.num_km * consumo_por_km
        return total_consumo

# Crie a classe  livro (defina apenas os atributos)
class Livro:
    def __init__(self, titulo: str, autor: str, ano: int, num_paginas: int, genero: str):
        self.titulo = titulo.title()
        self.autor = autor.title()
        self.ano = ano
        self.num_paginas = num_paginas
        self.genero = genero.title()