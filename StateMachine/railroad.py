from deed import Deed
from player import Player

class Railroad(Deed):
    def __init__(self, mTileName, mCost, mSet, mRent):
        super().__init__(mTileName, mCost, mSet, mRent)
        self.mNumRail = 1
    
    def CalculateRailroadRent(self) -> int:
        if self.mNumRail == 1:
            return self.mRent
        elif self.mNumRail == 2:
            return self.mRent *2
        elif self.mNumRail == 3:
            return self.mRent * 4
        elif self.mNumRail == 4:
            return self.mRent * 8
    
    # TODO: complete function
    # def CountRailroadOwned() -> int:
        # similar to CheckMonoPoly