from deed import Deed
from player import Player

class Utility(Deed):
    def __init__(self, mTileName, mCost, mSet, mRent = None):
        super().__init__(mTileName, mCost, mSet, mRent)
        self.card = False
    
    def CalculateRent(self, rollSum: int, player: Player) -> int:
        if self.card:
            self.card = False
            return rollSum * 10
        elif self.CountDeedOwned(player) == 1:
            return rollSum * 4
        elif self.CountDeedOwned(player) == 2:
            return rollSum * 10

    def reset(self):
        super().reset()