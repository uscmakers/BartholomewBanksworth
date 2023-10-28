import random
from card import Card
from typing import List
from tile import Tile
from player import Player

class Deck(Tile):
    def __init__(self, mTileName, shuffle):
        super().__init__(mTileName)
        self.mList : List[Card] = []
        self.mTop = 0
        if self.mTileName == "Chance":
            for num in range(15):
                card = Card(num)
                self.mList.append(card)
            # Another railroad card
            card = Card(3)
            self.mList.append(card)
        elif self.mTileName == "Community Chest":
            for num in range(12, 28):
                card = Card(num)
                self.mList.append(card)
        else:
            print("Only options are 'community chest' or 'chance'")
        if shuffle: random.shuffle(self.mList) # shuffle deck

    def action(self, mPlayer: Player, rollSum: int):
        self.mList[self.mTop].action(mPlayer, mPlayer.mPlayerList)
        self.mTop = (self.mTop + 1) % len(self.mList)