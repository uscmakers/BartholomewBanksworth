import random
from player import Player
class Board:
    def __init__(self, mNumPlayers: int):
        self.mNumPlayers = mNumPlayers
        self.mPlayers = []
        for _ in range(self.mNumPlayers):
            self.mPlayers.append(Player())
    
    def run(self):
        pass
    
    def rollDice(self):
        dice = (random.randint(1,6), random.randint(1,6))
        return dice[0] + dice[1]