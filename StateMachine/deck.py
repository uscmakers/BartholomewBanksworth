import random
from card import Card
from typing import List
from tile import Tile

class Deck(Tile):
    def __init__(self, type, shuffle):
        self.mType = type
        self.mList : List[Card] = []
        self.mTop = 0
        if type == "Chance":
            for num in range(15):
                card = Card(num)
                self.mList.append(card)
            # Another railroad card
            card = Card(3)
            self.mList.append(card)
        elif type == "Community Chest":
            for num in range(12, 28):
                card = Card(num)
                self.mList.append(card)
        else:
            print("Only options are 'community chest' or 'chance'")
        if shuffle: random.shuffle(self.mList) # shuffle deck

    def action(self, player, board):
        self.mList[self.mTop].action(player, board)
        self.mTop = (self.mTop + 1) % len(self.mList)
