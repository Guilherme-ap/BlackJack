import Deck

class Dealer:
    def __init__(self, mao, pontos):
        self.mao = []
        self.deck = Deck

    def cartasMao(self):
      return self.mao
    
    def receberCarta(self, carta):
       self.mao.append(carta)