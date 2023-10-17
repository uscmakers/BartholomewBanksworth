from board import Board
from deed import Deed
from player import Player

class Utility(Deed):
    def __init__(self, mTileName, mCost, mSet, mRent):
        super().__init__(mTileName, mCost, mSet, mRent)
    
    def CalculateUtilityRent(self, rollSum) -> int:
        # TODO: function for number of utility owned
        # if utilityCount == 1:
        if None:
            return rollSum * 4
        # elif utilityCount == 2:
        elif None:
            return rollSum * 10
    
    # TODO: complete function
    # def CountUtilityOwned() -> int:
        # similar to CheckMonoPoly