from tile import Tile
from player import Player

class GoToJail(Tile):
    def __init__(self, mTileName):
        super().__init__(mTileName)

    def action(self, mPlayer: Player, rollSum: int):
        mPlayer.GoToJail()
        
    def reset(self):
        pass