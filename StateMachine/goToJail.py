import const
from tile import Tile
from player import Player

class GoToJail(Tile):
    def __init__(self, mTileName):
        super().__init__(self, mTileName)

    def action(self, mPlayer: Player):
        mPlayer.mPos = const.JAIL_SPACE
        mPlayer.mInJail = True