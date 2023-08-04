import itertools
import random


class Deck:
    def __init__(self, carta,naipe):
        self.carta = carta
        self.naipe = naipe
    
    
    def criarCartas(self):
        baralhoCompleto = list(itertools.product(self.carta, self.naipe))
        return baralhoCompleto


    def removerCartas(self):
        removerCarta = self.comprarCarta()
        baralho = self.criarCartas()
        if removerCarta in baralho:
            baralho.remove(removerCarta)
        return baralho
        


    def embaralharDeck(self): 
        baralho = self.criarCartas()
        baralhoAtualizado = self.removerCartas()
        if baralho == baralhoAtualizado:
         random.shuffle(baralho)
         return baralho
        else: 
            return baralhoAtualizado

    
    def comprarCarta(self):
        baralho = self.criarCartas()
        comprarCartaAleatoria =  random.choice(baralho) 
        return comprarCartaAleatoria




        
# cartas = list(["ás", 2 , 3, 4, 5, 6, 7, 8, 9, 10, "rei", "dama", "valete"])
# naipe  = list(["copas", "paus", "ouros", "espadas" ])
cartas = list([1,2,3])
naipe  = list(["copas"])
cartas = Deck(cartas,naipe)
cartas.criarCartas()
print(cartas.embaralharDeck())
print("Carta comprada: ", cartas.comprarCarta())
print("Carta removida: ",cartas.removerCartas())
print(cartas.embaralharDeck())

