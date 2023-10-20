from board import Board
from deed import Deed
from player import Player
from board import SetToDeedMap

class Utility(Deed):
    def __init__(self, mTileName, mCost, mSet, mRent = None):
        super().__init__(mTileName, mCost, mSet, mRent)
    
    def CalculateUtilityRent(self, rollSum, player: Player = None) -> int:
        # TODO: function for number of utility owned
        if self.CountDeedOwned(self, player) == 1:
            return rollSum * 4
        elif self.CountDeedOwned(self, player) == 2:
            return rollSum * 10