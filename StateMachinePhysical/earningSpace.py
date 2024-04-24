import const
from tile import Tile
from player import Player

class EarningSpace(Tile):
    def __init__(self, mTileName, earnings: int):
        super().__init__(mTileName)
        self.earnings = earnings
    
    def action(self, mPlayer: Player, rollSum = None):
        mPlayer.mBalance += self.earnings
        if self.earnings > 0:
            print(mPlayer.mPlayerName + " earned $" + str(self.earnings) + "!")
        elif self.earnings < 0:
            print(mPlayer.mPlayerName + " lost $" + str(-self.earnings) + "!")