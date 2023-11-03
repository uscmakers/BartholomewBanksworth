from deed import Deed
from player import Player

class Railroad(Deed):
    def __init__(self, mTileName, mCost, mSet, mRent):
        super().__init__(mTileName, mCost, mSet, mRent)
        self.card = False
    
    def CalculateRent(self, rollSum,  player: Player = None) -> int:
        tempRent = 0
        if self.CountDeedOwned(player) == 1:
            tempRent = self.mRent
        elif self.CountDeedOwned(player) == 2:
            tempRent = self.mRent *2
        elif self.CountDeedOwned(player) == 3:
            tempRent = self.mRent * 4
        elif self.CountDeedOwned(player) == 4:
            tempRent = self.mRent * 8
        
        if self.card:
            self.card = False
            return tempRent * 2
        else:
            return tempRent
