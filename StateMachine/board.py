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
Boardwalk = Deed("Boardwalk", 400, "Blue", 50)
# TODO: Add board tiles here!

class Board:
    def __init__(self, mNumPlayers: int):
        self.mNumPlayers = mNumPlayers
        self.mPlayers = []
        self.mTiles = []
    
    # INITIALIZATION
    
    def init(self):
        self.initPlayers()
        self.initBoard()
    
    def initBoard(self):
        # TODO: initialize array using pre-defined tiles (global variables)
        self.mTiles = [Go, Boardwalk, IncomeTax]
        self.mTotalSpaces = len(self.mTiles)

    def initPlayers(self):
        for i in range(self.mNumPlayers-1): # humans
            p = Player(False)
            self.mPlayers.append(p)
        self.mPlayers.append(Player(True)) # ai
        for i in range(len(self.mPlayers)): # name each player
            self.mPlayers[i].NamePlayer(i+1)
        print()
    
    # RUN LOOP
    
    def run(self):
        round = 1
        while True:
            print("Round " + str(round) + ":")
            player : Player
            for player in self.mPlayers:
                print("\n" + player.mPlayerName + "'s turn:\n")
                if player.mTurnsInJail == 3: # out-of-jail check
                    player.mTurnsInJail = 0
                    print(player.mPlayerName + " is out of jail!")
                elif player.mTurnsInJail > 0: # in-jail check
                    print(player.mPlayerName + " is in jail!")
                    if player.mNumJailFree > 0: # get out of jail free card
                        choice = input("Would you like to use your get out of jail free card? (yes/no) ")
                        if choice == "yes":
                            player.mTurnsInJail = 0
                            player.mNumJailFree -= 1
                        else:    
                            player.mTurnsInJail += 1
                            continue
                    else:
                        player.mTurnsInJail += 1
                        continue
                rolled = False
                while True:
                    command = input("Type a command, or type help: ")
                    if command == "help":
                        self.helpMenu()
                    elif command == "end":
                        if rolled: break
                        print("You haven't rolled yet!")
                    elif command == "roll":
                        dice, rollSum = self.rollDice(player)
                        rolled = True
                        if dice[0] == dice[1]: # doubles check
                            player.mContinuousDoubles += 1
                            if player.mContinuousDoubles == 3: # go directly to jail after 3 consecutive doubles
                                player.mPos = const.JAIL_SPACE
                                player.mTurnsInJail = 1
                                break
                        if (player.mPos + rollSum) >= self.mTotalSpaces: # passed go check
                            player.mBalance += const.GO_MONEY
                            print(player.mPlayerName + " passed go and earned $200!")
                        player.mPos = (player.mPos + rollSum) % self.mTotalSpaces # move player appropriate number of spaces
                        # TODO: insert move motor code here
                        tile = self.mTiles[player.mPos]
                        print(player.mPlayerName + " landed on " + tile.mTileName + "!")
                        tile.action(player)
                    elif command == "stats":
                        print(player.mPlayerName)
                        print("Balance: $" + str(player.mBalance))
                        nw = player.CalculateNetWorth()
                        if nw == None: nw = 0
                        print("Net worth: $" + str(nw))
                        print("Properties:")
                        if len(player.mDeedOwned) == 0:
                            print("(None)")
                        else:
                            d : Deed
                            for d in player.mDeedOwned:
                                print(d.mTileName)
                    elif command == "trade":
                        pass
                    elif command == "build":
                        pass
                    else:
                        print("Not a valid command. Type help to see list of valid commands.")
                    if player.mBalance < 0: # bankruptcy check
                        self.mPlayers.remove(player)
                        print(player.mPlayerName + " is bankrupt!")
                        continue
            round += 1
    
    def rollDice(self, player: Player): # simulates rolling two dice
        dice = (random.randint(1,6), random.randint(1,6))
        sum = dice[0] + dice[1]
        print(player.mPlayerName + " rolled a " + str(sum) + "!")
        return dice, sum
    
    def helpMenu(self): # print help menu
        print("Help menu:")
        print("roll = roll dice")
        print("stats = see your balance and properties")
        print("build = build houses/hotels")
        print("trade = trade with another player")
        print("end = end your turn")
        print("help = see this list of commands")