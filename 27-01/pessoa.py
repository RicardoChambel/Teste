class Pessoa:
    def __init__(self, nome: str, altura: float, peso:float, idade:int=0):
        self.nome = nome.title()
        self.idade= idade
        self.altura = altura
        self.peso = peso # peso em gramas
        self.energia = 100
        self.acordado = True
    
    # por cada coisa que comer engorda 100g
    def comer(self, alimento: list[str]):
        self.peso += 100 * len(alimento)
        return self.peso

    def falar(self):
        return "bla bla bla"
    
    def andar(self):
        return "A pessoa esta a andar..."
    
    # Até aos 21 anos por cada ano que envelhece cresce 2.5 cm
    def envelhecer(self, anos: int=1):
        if self.idade < 21:
            self.crescer()
        self.idade += anos
        return self.idade
    
    def crescer(self, cm: float = 2.5):
        self.altura += cm
        
    def dormir(self):
        if self.acordado:
            self.acordado = False
            return "A dormir..."
        return "Ja esta a dormir"
        self.energia = 100
    
    # crie um metodo para acordar, garanta que so acorda se estiver a dormir
    def acordar(self):
        if not self.acordado:
            self.acordado = True
            return "Acordou"
        return "Ja esta acordado"