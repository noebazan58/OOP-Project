import random

class Card:
    def __init__(self, number, suit, color):
        self._number = number
        self._suit = suit
        self._suit = color
    


class Deck(Card):
    def __init__(self):
        self.num_cards = []
    
    def sym(self, num):
        if (self.num < 11 and self.num > 1):
            return str(self.num)
        elif (self.num == 1):
            return "Ace"
        elif (self.num == 11):
            return "Jack"
        elif (self.num == 12):
            return "Queen"
        else:
            return "King"
        
    def rank(self):
        return random(1, 13)
        
    def deck(self):
        for i in range(0, self.num_cards):
            rank = rank()
            symbol = sym(rank)
            shade = col()
            super().__init__(rank, sym, col)
    
   
    
  
        
    
