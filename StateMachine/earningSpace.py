import const
from tile import Tile
from player import Player

class EarningSpace(Tile):
    def __init__(self, mTileName, earnings: int):
        super().__init__(self, mTileName)
        self.earnings = earnings
    
    def action(self, mPlayer: Player):
        mPlayer.mBalance += self.earnings
        if self.earnings > 0:
            print(mPlayer.mPlayerName + " earned $" + self.earnings + "!")
        elif self.earnings < 0:
            print(mPlayer.mPlayerName + " lost $" + self.earnings + "!")