import random
import const
from player import Player

class Board:
    def __init__(self, mNumPlayers: int):
        self.mNumPlayers = mNumPlayers
        self.mPlayers = []
        self.mTiles = []
        for _ in range(self.mNumPlayers):
            self.mPlayers.append(Player())
    
    def init(self):
        # TODO: initialize mTiles to be a list of tiles representing the board
        # TODO: initialize mTiles to be a list of tiles representing the board
        return
    
    def run(self):
        round = 1
        while True:
            print("Round " + round + ":")
            for player in self.mPlayers:
                tile = self.mTiles[self.rollDice(player)]
                print(player.mPlayerName + " landed on " + tile.mName + "!")
                tile.action()
            round += 1
    
    def rollDice(self, player: Player):
        dice = (random.randint(1,6), random.randint(1,6))
        rollSum = dice[0] + dice[1]
        print(player.mPlayerName + " rolled a " + rollSum + "!")
        if dice[0] == dice[1]:
            player.mContinuousDoubles += 1
            if player.mContinuousDoubles == 3:        
                return const.JAIL_SPACE
        if (player.mPos + rollSum) >= const.TOTAL_SPACES:
            player.mBalance += const.GO_MONEY
            print(player.mPlayerName + " passed go!")
        player.mPos = (player.mPos + rollSum) % const.TOTAL_SPACES
        return player.mPos