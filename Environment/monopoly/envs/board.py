# import random
# import const
# from player import Player
# from tile import Tile
# from deed import Deed
# from earningSpace import EarningSpace
# from property import Property
# from railroad import Railroad
# from utility import Utility
# from goToJail import GoToJail
# from jail import Jail
# from deck import Deck
# from typing import List

# # TILES

# Go = EarningSpace("Go", 200)
# IncomeTax = EarningSpace("Income Tax", -200)
# LuxuryTax = EarningSpace("Luxury Tax", -100)
# FreeParking = EarningSpace("Free Parking", 0)
# GotoJail = GoToJail("Go To Jail")
# VisitJail = Jail("Jail")
# MediterraneanAvenue = Property("Mediterranean Avenue", 60, "brown", 2, 50, 10, 30, 90, 160, 250)
# BalticAvenue = Property("Baltic Avenue", 60, "brown", 4, 50, 20, 60, 180, 320, 450)
# ReadingRR = Railroad("Reading Railroad", 200, "railroad", 25)
# OrientalAvenue = Property("Oriental Avenue", 100, "lightblue", 6, 50, 30, 90, 270, 400, 550)
# VermontAvenue = Property("Vermont Avenue", 100, "lightblue", 6, 50, 30, 90, 270, 400, 550)
# ConnecticutAvenue = Property("Connecticut Avenue", 120, "lightblue", 8, 40, 100, 300, 450, 600, 550)
# CharlesPlace = Property("St. Charles Place", 140, "pink", 10, 100, 50, 150, 450, 625, 750)
# ElectricCompany = Utility("Electric Company", 150, "utility", None)
# StatesAvenue = Property("States Avenue", 140, "pink", 10, 100, 50, 150, 450, 625, 750)
# VirginiaAvenue = Property("Virginia Avenue", 160, "pink", 12, 100, 60, 180, 500, 700, 900)
# PennsylvaniaRR = Railroad("Pennsylvania Railroad", 200, "railroad", 25)
# JamesPlace = Property("St. James Place", 180, "orange", 14, 100, 70, 200, 550, 750, 950)
# TennesseeAvenue = Property("Tennessee Avenue", 180, "orange", 14, 100, 70, 200, 550, 750, 950)
# NewYorkAvenue = Property("New York Avenue", 200, "orange", 16, 100, 80, 220, 600, 800, 1000)
# KentuckyAvenue = Property("Kentucky Avenue", 220, "red", 18, 150, 90, 250, 700, 875, 1050)
# IndianaAvenue = Property("Indiana Avenue", 220, "red", 18, 150, 90, 250, 700, 875, 1050)
# IllinoisAvenue = Property("Illinois Avenue", 240, "red", 20, 150, 100, 300, 750, 925, 1100)
# BoRR = Railroad("B&O Railroad", 200, "railroad", 25)
# AtlanticAvenue = Property("Atlantic Avenue", 260, "yellow", 22, 150, 110, 330, 800, 975, 1150)
# VentnorAvenue = Property("Ventnor Avenue", 260, "yellow", 22, 150, 110, 330, 800, 975, 1150)
# WaterWorks = Utility("Water Works", 150, "utility", None)
# MarvinGardens = Property("Marvin Gardens", 280, "yellow", 24, 150, 120, 360, 850, 1025, 1200)
# PacificAvenue = Property("Pacific Avenue", 300, "green", 26, 200, 130, 390, 900, 1100, 1275)
# NorthCarolinaAvenue = Property("North Carolina Avenue", 300, "green", 26, 200, 130, 390, 900, 1100, 1275)
# PennsylvaniaAvenue = Property("Pennsylvania Avenue", 320, "green", 28, 200, 150, 450, 1000, 1200, 1400)
# ShortLine = Railroad("Short Line", 200, "railroad", 25)
# ParkPlace = Property("Park Place", 350, "darkblue", 35, 175, 500, 1100, 700, 1300, 1500)
# Boardwalk = Property("Boardwalk", 400, "darkblue", 50, 150, 200, 600, 1400, 1700, 2000)
# CommunityChest = Deck("Community Chest", True)
# Chance = Deck("Chance", True)

# Tiles = [Go, MediterraneanAvenue, CommunityChest, BalticAvenue, IncomeTax, ReadingRR, OrientalAvenue, Chance, VermontAvenue, ConnecticutAvenue, VisitJail,
#                        CharlesPlace, ElectricCompany, StatesAvenue, VirginiaAvenue, PennsylvaniaRR, JamesPlace, CommunityChest, TennesseeAvenue, NewYorkAvenue, FreeParking,
#                        KentuckyAvenue, Chance, IndianaAvenue, IllinoisAvenue, BoRR, AtlanticAvenue, VentnorAvenue, WaterWorks, MarvinGardens, GotoJail,
#                        PacificAvenue, NorthCarolinaAvenue, CommunityChest, PennsylvaniaAvenue, ShortLine, Chance, ParkPlace, LuxuryTax, Boardwalk]

# SetToDeedMap = {"railroad": [ReadingRR, PennsylvaniaRR, BoRR, ShortLine],
#                 "utility": [ElectricCompany, WaterWorks],
#                 "brown": [MediterraneanAvenue, BalticAvenue],
#                 "lightblue": [OrientalAvenue, VermontAvenue, ConnecticutAvenue],
#                 "pink": [CharlesPlace, StatesAvenue, VirginiaAvenue],
#                 "orange": [JamesPlace, TennesseeAvenue, NewYorkAvenue],
#                 "red": [KentuckyAvenue, IndianaAvenue, IllinoisAvenue],
#                 "yellow": [AtlanticAvenue, VentnorAvenue, MarvinGardens],
#                 "green": [PacificAvenue, NorthCarolinaAvenue, PennsylvaniaAvenue],
#                 "darkblue": [ParkPlace, Boardwalk]}

# class Board:
#     def __init__(self, mNumPlayers: int):
#         self.mNumPlayers = mNumPlayers
#         self.mPlayers : List[Player] = []
#         self.mTiles = []
    
#     # INITIALIZATION
    
#     def init(self):
#         self.initPlayers()
#         self.initBoard()
    
#     def initBoard(self):
#         self.mTiles = Tiles

#     def initPlayers(self):
#         # initialize players and add to player list
#         for i in range(self.mNumPlayers-1): # humans
#             p = Player(i, False)
#             self.mPlayers.append(p)
#         self.mPlayers.append(Player(self.mNumPlayers-1, True)) # ai
#         for i in range(len(self.mPlayers)): 
#             self.mPlayers[i].InitPlayerList(self.mPlayers) # each player has access to list of players
#             self.mPlayers[i].NamePlayer(i+1) # name each player
        
#         # self.mPlayers[0].mDeedOwned = [MediterraneanAvenue, BalticAvenue]
#         # MediterraneanAvenue.mOwner = self.mPlayers[0]
#         # BalticAvenue.mOwner = self.mPlayers[0]

#         # self.mPlayers[1].mDeedOwned = [OrientalAvenue, VermontAvenue, ConnecticutAvenue]
#         # OrientalAvenue.mOwner = self.mPlayers[1]
#         # VermontAvenue.mOwner = self.mPlayers[1]
#         # ConnecticutAvenue.mOwner = self.mPlayers[1]
    
    # RUN LOOP
    
    def run(self):
        turn = 1
        while True:
            print("Turn " + str(turn) + ":")
            player : Player
            for player in self.mPlayers:
                current_player_num = player.index
                print(player.mPlayerName + "'s turn:")
                if player.mTurnsInJail == 3: # out-of-jail check
                    player.mTurnsInJail = 0
                    print(player.mPlayerName + " is out of jail!")
                elif player.mTurnsInJail > 0: # in-jail check
                    print(player.mPlayerName + " is in jail!")
                    if player.mNumJailFree > 0: # get out of jail free card
                        if player.mIsAi:
                            player.UseGetOutOfJailFree()
                        else:
                            choice = input("Would you like to use your get out of jail free card? (yes/no) ")
                            if choice == "yes":
                                player.UseGetOutOfJailFree()
                            else:    
                                player.mTurnsInJail += 1
                                continue
                    elif player.mBalance >= const.JAIL_FEE:
                        if player.mIsAi:
                            player.PayJailFee()
                        else:
                            choice = input("Would you like to pay the $" + str(const.JAIL_FEE) + " jail fee? (yes/no) ")
                            if choice == "yes":
                                player.PayJailFee()
                            else:    
                                player.mTurnsInJail += 1
                                continue
                    else:
                        player.mTurnsInJail += 1
                        continue
                if player.mIsAi:
                    self.turn(player)
                    # TODO: AI can build
                    # TODO: AI can trade
                    self.stats(player)
                else:
                    rolled = False
                    while True:  
                        command = input("Type a command, or type help: ")
                        if command == "help":
                            self.helpMenu()
                        elif command == "end":
                            if rolled: break
                            print("You haven't rolled yet!")
                        elif command == "roll":
                            if rolled:
                                print("You already rolled!")
                            else:
                                rolled = True
                                self.turn(player)
                        elif command == "stats":
                            self.stats(player)
                        # TODO: future implementation
                        elif command == "trade":
                            pass
                        # LOGIC IS DOWN BUT NOT ABLE TO ACCESS CHILD CLASS FUNCTIONS
                        elif command == "build":
                            # pick property to build on from property list
                            # if len(player.mDeedOwned) == 0:
                                # print("No houses to build on")
                                # exit()
                                # self.helpMenu()
                            # else:
                                # d : Deed
                            count: int = 1
                            for d in player.mDeedOwned:
                                if d.mSet != "utility" and d.mSet != "railroad":
                                    print(str(count) + ". " + str(d.mTileName)) 
                                else:
                                    print(str(count) + ". " + str(d.mTileName) + " (can not build house)")
                                count += 1
                            select = int(input("Enter corresponding number to select property: "))
                            developProperty: property = player.mDeedOwned[select - 1]
                            # check if can build on selected property
                            # print(developProperty.BuildHouse(player))
                            # print("This is house cost", developProperty.mHouseCost, "This is player balance", player.mBalance)
                            if player.mBalance >= developProperty.mHouseCost and developProperty.BuildHouse(player):
                                # if can build, check if enough balance, then build, increment house count
                                ans = input("Do you want to build here (y/n)? ")
                                if ans in "Yy":
                                    developProperty.mNumHouse += 1
                                    if developProperty.mNumHouse == 5: player.mHotelOwned += 1
                                    else: player.mHouseOwned += 1
                                    print("You have built a house")
                            else:
                                print("Cannot build a house here.")
                        elif command == "quit":
                            ans = input("Are you sure you want to quit the game? Your progress won't be saved. (y/n) ")
                            if ans in "Yy":
                                return
                        else:
                            print("Not a valid command. Type help to see list of valid commands.")
                        if player.mBalance < 0: # bankruptcy check
                            self.mPlayers.remove(player)
                            print(player.mPlayerName + " is bankrupt!")
                            break
                player.mContinuousDoubles = 0
            turn += 1
    
    def turn(self, player: Player):
        while True:
            tile, doubles, rollSum = self.roll(player) # roll dice and move player to appropriate space
            # player.MotorRequest(rollSum) # physically move player to tile
            print(player.mPlayerName + " landed on " + tile.mTileName + "!")
            if player.mTurnsInJail == 0: tile.action(player, rollSum) # execute action when land on space
            if (not doubles) or (player.mTurnsInJail > 0): break
    
    def roll(self, player: Player): # roll dice and move player to appropriate space
        doubles = False
        dice, rollSum = self.rollDice(player)
        if dice[0] == dice[1]: # doubles check
            doubles = True
            print(player.mPlayerName + " rolled doubles!")
            player.mContinuousDoubles += 1
            if player.mContinuousDoubles == 3: # go directly to jail after 3 consecutive doubles
                player.mPos = 10
                player.mTurnsInJail = 1
                print(player.mPlayerName + " rolled three consecutive doubles! Go to jail!")
                return None
        if (player.mPos + rollSum) >= 40: # passed go check
            player.mBalance += const.GO_MONEY
            print(player.mPlayerName + " passed go and earned $200!")
        player.mPos = (player.mPos + rollSum) % 40 # move player appropriate number of spaces
        tile = self.mTiles[player.mPos]
        return tile, doubles, rollSum
    
    def rollDice(self, player: Player): # simulates rolling two dice
        dice = (random.randint(1,6), random.randint(1,6))
        sum = dice[0] + dice[1]
        print(player.mPlayerName + " rolled " + str(sum) + "!")
        return dice, sum
    
    def stats(self, player: Player): # print stats
        print(player.mPlayerName + "'s stats:")
        print("Balance: $" + str(player.mBalance))
        print("Properties:")
        if len(player.mDeedOwned) == 0:
            print("(None)")
        else:
            d : Deed
            for d in player.mDeedOwned:
                print(d.mTileName + " [" + d.mSet + "]")
        
        if (player.mNumJailFree > 0):
            print (player.mNumJailFree, "Get out of Jail free")
    
    def helpMenu(self): # print help menu
        print("Help menu:")
        print("roll = roll dice")
        print("stats = see your balance and properties")
        print("build = build houses/hotels")
        print("trade = trade with another player")
        print("end = end your turn")
        print("quit = quit the game")
        print("help = see this list of commands")