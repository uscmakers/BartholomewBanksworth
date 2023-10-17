import random
import const
from player import Player
from tile import Tile
from earningSpace import EarningSpace

from tile import Tile
from earningSpace import EarningSpace
from property import Property
from railroad import Railroad
from utility import Utility
from goToJail import GoToJail
from deed import Deed
from property import Property
from railroad import Railroad
from utility import Utility

# TILES

Go = EarningSpace("Go", 200)
IncomeTax = EarningSpace("Income Tax", -200)
LuxuryTax = EarningSpace("Luxury Tax", -100)
FreeParking = EarningSpace("Free Parking", 0)
GotoJail = GoToJail("Go To Jail")
MediterraneanAvenue = Property("Mediterranean Avenue", 60, "brown", 2, 50, 10, 30, 90, 160, 250)
BalticAvenue = Property("Baltic Avenue", 60, "brown", 4, 50, 20, 60, 180, 320, 450)
ReadingRR = Railroad("Reading Railroad", 200, "railroad", 25)
OrientalAvenue = Property("Oriental Avenue", 100, "lightblue", 6, 50, 30, 90, 270, 400, 550)
VermontAvenue = Property("Vermont Avenue", 100, "lightblue", 6, 50, 30, 90, 270, 400, 550)
ConnecticutAvenue = Property("Connecticut Avenue", 120, "lightblue", 8, 40, 100, 300, 450, 600, 550)
CharlesPlace = Property("St. Charles Place", 140, "pink", 10, 100, 50, 150, 450, 625, 750)
ElectricCompany = Utility("Electric Company", 150, "utility")
StatesAvenue = Utility("States Avenue", 140, "pink", 10, 100, 50, 150, 450, 625, 750)
VirginiaAvenue = Utility("Virginia Avenue", 160, "pink", 12, 100, 60, 180, 500, 700, 900)
PennsylvaniaRR = Utility("Pennsylvania Railroad", 200, "railroad", 25)
JamesPlace = Utility("St. James Place", 180, "orange", 14, 100, 70, 200, 550, 750, 950)
TennesseeAvenue = Utility("Tennessee Avenue", 180, "orange", 14, 100, 70, 200, 550, 750, 950)
NewYorkAvenue = Utility("New York Avenue", 200, "orange", 16, 100, 80, 220, 600, 800, 1000)
KentuckyAvenue = Property("Kentucky Avenue", 220, "red", 18, 150, 90, 250, 700, 875, 1050)
IndianaAvenue = Property("Indiana Avenue", 220, "red", 18, 150, 90, 250, 700, 875, 1050)
IllinoisAvenue = Property("Illinois Avenue", 240, "red", 20, 150, 100, 300, 750, 925, 1100)
BoRR = Railroad("B&O Railroad", 200, "railroad", 25)
AtlanticAvenue = Property("Atlantic Avenue", 260, "yellow", 22, 150, 110, 330, 800, 975, 1150)
VentnorAvenue = Property("Ventnor Avenue", 260, "yellow", 22, 150, 110, 330, 800, 975, 1150)
WaterWorks = Utility("Water Works", 150, "utility")
MarvinGardens = Property("Marvin Gardens", 280, "yellow", 24, 150, 120, 360, 850, 1025, 1200)
PacificAvenue = Property("Pacific Avenue", 300, "green", 26, 200, 130, 390, 900, 1100, 1275)
NorthCarolinaAvenue = Property("North Carolina Avenue", 300, "green", 26, 200, 130, 390, 900, 1100, 1275)
PennsylvaniaAvenue = Property("Pennsylvania Avenue", 320, "green", 28, 200, 150, 450, 1000, 1200, 1400)
ShortLine = Railroad("Short Line", 200, "railroad", 25)
ParkPlace = Property("Park Place", 350, "darkblue", 35, 175, 500, 1100, 700, 1300, 1500)
Boardwalk = Property("Boardwalk", 400, "darkblue", 50, 150, 200, 600, 1400, 1700, 2000)

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
        turn = 1
        while True:
            print("Turn " + str(turn) + ":")
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
                        rolled = True
                        dice, rollSum = self.rollDice(player)
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