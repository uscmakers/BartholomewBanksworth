import random
import const
from player import Player
from tile import Tile
from earningSpace import EarningSpace

from tile import Tile
from earningSpace import EarningSpace
from deed import Deed

# TILES

Go = EarningSpace("Go", 200)
IncomeTax = EarningSpace("Income Tax", -200)
FreeParking = EarningSpace("Free Parking", 0)
Boardwalk = Deed("Boardwalk", 400, "Blue")
# TODO: Add board tiles here!

class Board:
    def __init__(self, mNumPlayers: int):
        self.mNumPlayers = mNumPlayers
        self.mPlayers = []
        self.mTiles = []
    
    # INITIALIZATION
    
    def init(self):
        self.init_players()
        self.init_board()
    
    def init_board(self):
        # TODO: initialize array using pre-defined tiles (global variables)
        self.mTiles = [Go, Boardwalk, IncomeTax]
        self.mTotalSpaces = len(self.mTiles)

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
        while True:
            print("Round " + str(round) + ":")
            player : Player
            for player in self.mPlayers:
                dice, rollSum = self.rollDice(player)
                if dice[0] == dice[1]: # doubles check
                    player.mContinuousDoubles += 1
                    if player.mContinuousDoubles == 3: # go directly to jail after 3 consecutive doubles
                        player.mPos = const.JAIL_SPACE
                        player.mInJail = True
                        continue
                if (player.mPos + rollSum) >= self.mTotalSpaces: # passed go check
                    player.mBalance += const.GO_MONEY
                    print(player.mPlayerName + " passed go!")
                player.mPos = (player.mPos + rollSum) % self.mTotalSpaces # move player appropriate number of spaces
                tile = self.mTiles[player.mPos]
                print(player.mPlayerName + " landed on " + tile.mTileName + "!")
                tile.action(player)
                if player.mBalance < 0: # bankruptcy check
                    self.mPlayers.remove(player)
                    print(player.mPlayerName + " is bankrupt!")
                    continue
                if player.mInJail: # jail check
                    continue
            round += 1
    
    def rollDice(self, player: Player): # simulates rolling two dice
        dice = (random.randint(1,6), random.randint(1,6))
        sum = dice[0] + dice[1]
        print(player.mPlayerName + " rolled a " + str(sum) + "!")
        return dice, sum