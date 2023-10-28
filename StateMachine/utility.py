from deed import Deed
from player import Player

class Utility(Deed):
    def __init__(self, mTileName, mCost, mSet, mRent = None):
        super().__init__(mTileName, mCost, mSet, mRent)
    
    def CalculateRent(self, rollSum: int, player: Player = None) -> int:
        # TODO: function for number of utility owned
        # print("IN CALCULATE RENT This is player", player, "This is rollSum", rollSum)
        if self.CountDeedOwned(player) == 1:
            print(rollSum * 4)
            return rollSum * 4
        elif self.CountDeedOwned(player) == 2:
            return rollSum * 10