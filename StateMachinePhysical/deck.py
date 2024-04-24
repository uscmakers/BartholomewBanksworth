import random
from card import Card
from typing import List
from tile import Tile
from player import Player
import const

# EACH DECK IS COMPOSED OF MANY CARDS
class Deck(Tile):
    # INITIALIZATION OF DECKS
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

    # WHAT HAPPENS WHEN A PLAYER LANDS ON A COMMUNITY CHEST OR CHANCE TILE?
    def action(self, mPlayer: Player, rollSum: int):
        getOutOfJailFree = self.mList[self.mTop].action(mPlayer, mPlayer.mPlayerList, self.mTileName == "Chance")
        if getOutOfJailFree:
            del self.mList[self.mTop] # remove get out of jail free card from deck if received
        self.mTop = (self.mTop + 1) % len(self.mList)
    
    def addGetOutOfJailFreeCard(self):
        self.mList.append(Card(13))