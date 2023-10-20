from deed import Deed
from player import Player

class Railroad(Deed):
    def __init__(self, mTileName, mCost, mSet, mRent):
        super().__init__(mTileName, mCost, mSet, mRent)
    
    def CalculateRailroadRent(self, player: Player = None) -> int:
        if self.CountDeedOwned(self, player) == 1:
            return self.mRent
        elif self.CountDeedOwned(self, player) == 2:
            return self.mRent *2
        elif self.CountDeedOwned(self, player) == 3:
            return self.mRent * 4
        elif self.CountDeedOwned(self, player) == 4:
            return self.mRent * 8