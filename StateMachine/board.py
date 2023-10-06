import random
import const
from player import Player
from tile import Tile
from earningSpace import EarningSpace

class Board:
    def __init__(self, mNumPlayers: int):
        self.mNumPlayers = mNumPlayers
        self.mPlayers = [Player]
        self.mTiles = [Tile]
    
    # INITIALIZATION
    
    def init(self):
        self.init_players()
        self.init_board()
    
    def init_board(self):
        # irith just put this here as an example!
        go = EarningSpace("Go", 200)
        incomeTax = EarningSpace("Income Tax", -200)
        self.mTiles = [go, incomeTax] 

    def init_players(self):
        for i in range(self.mNumPlayers-1): # humans
            p = Player(False)
            self.mPlayers.append(p)
        self.mPlayers.append(Player(True)) # ai
        for player in self.mPlayers: # name each player
            player.NamePlayer()
    
    # RUN LOOP
    
    def run(self):
        round = 1
        gameOver = False
        while True:
            print("Round " + round + ":")
            for player in self.mPlayers:
                dice, rollSum = self.rollDice(player)
                if dice[0] == dice[1]: # doubles check
                    player.mContinuousDoubles += 1
                    if player.mContinuousDoubles == 3: # go directly to jail after 3 consecutive doubles
                        player.mPos = const.JAIL_SPACE
                        player.mInJail = True
                        continue
                if (player.mPos + rollSum) >= const.TOTAL_SPACES: # passed go check
                    player.mBalance += const.GO_MONEY
                    print(player.mPlayerName + " passed go!")
                player.mPos = (player.mPos + rollSum) % const.TOTAL_SPACES # move player appropriate number of spaces
                tile = self.mTiles[player.mPos]
                print(player.mPlayerName + " landed on " + tile.mName + "!")
                tile.action()
                if player.mBalance < 0: # bankruptcy check
                    self.mPlayers.remove(player)
                    print(player.mPlayerName + " is bankrupt!")
                    continue
            if gameOver: 
                break
            round += 1
    
    def rollDice(self, player: Player): # simulates rolling two dice
        dice = (random.randint(1,6), random.randint(1,6))
        sum = dice[0] + dice[1]
        print(player.mPlayerName + " rolled a " + sum + "!")
        return dice, sum