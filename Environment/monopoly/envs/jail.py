from tile import Tile
from player import Player

class Jail(Tile):
    def __init__(self, mTileName):
        super().__init__(mTileName)

    def action(self, mPlayer: Player, rollSum: int):
        print("Just visiting!")
        
    def reset(self):
        pass