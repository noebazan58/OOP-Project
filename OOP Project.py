import random
from abc import ABC, abstractmethod


# We will modify as needed. 
class Game(ABC):
    @abstractmethod
    def game_over():
        pass

    @abstractmethod
    def rules():
        pass

    @abstractmethod
    def player_cards():
        pass


class Card:
    def __init__(self, number, suit, color):
        self._number = number
        self._suit = suit
        self._suit = color
    


class Deck(Card):
    def __init__(self):
        pass
    
   
    
  
        
    
