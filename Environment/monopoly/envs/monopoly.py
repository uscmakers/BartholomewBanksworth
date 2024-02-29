# Adapted from https://mblogscode.com/2016/06/03/python-naughts-crossestic-tac-toe-coding-unbeatable-ai/

import gym
from gym.spaces import Dict, Discrete
import numpy as np

import config

from stable_baselines import logger

import random
import const
from player import Player
from tile import Tile
from deed import Deed
from earningSpace import EarningSpace
from property import Property
from railroad import Railroad
from utility import Utility
from goToJail import GoToJail
from jail import Jail
from deck import Deck
from typing import List

# TILES

Go = EarningSpace("Go", 200)
IncomeTax = EarningSpace("Income Tax", -200)
LuxuryTax = EarningSpace("Luxury Tax", -100)
FreeParking = EarningSpace("Free Parking", 0)
GotoJail = GoToJail("Go To Jail")
VisitJail = Jail("Jail")
MediterraneanAvenue = Property("Mediterranean Avenue", 60, "brown", 2, 50, 10, 30, 90, 160, 250)
BalticAvenue = Property("Baltic Avenue", 60, "brown", 4, 50, 20, 60, 180, 320, 450)
ReadingRR = Railroad("Reading Railroad", 200, "railroad", 25)
OrientalAvenue = Property("Oriental Avenue", 100, "lightblue", 6, 50, 30, 90, 270, 400, 550)
VermontAvenue = Property("Vermont Avenue", 100, "lightblue", 6, 50, 30, 90, 270, 400, 550)
ConnecticutAvenue = Property("Connecticut Avenue", 120, "lightblue", 8, 40, 100, 300, 450, 600, 550)
CharlesPlace = Property("St. Charles Place", 140, "pink", 10, 100, 50, 150, 450, 625, 750)
ElectricCompany = Utility("Electric Company", 150, "utility", None)
StatesAvenue = Property("States Avenue", 140, "pink", 10, 100, 50, 150, 450, 625, 750)
VirginiaAvenue = Property("Virginia Avenue", 160, "pink", 12, 100, 60, 180, 500, 700, 900)
PennsylvaniaRR = Railroad("Pennsylvania Railroad", 200, "railroad", 25)
JamesPlace = Property("St. James Place", 180, "orange", 14, 100, 70, 200, 550, 750, 950)
TennesseeAvenue = Property("Tennessee Avenue", 180, "orange", 14, 100, 70, 200, 550, 750, 950)
NewYorkAvenue = Property("New York Avenue", 200, "orange", 16, 100, 80, 220, 600, 800, 1000)
KentuckyAvenue = Property("Kentucky Avenue", 220, "red", 18, 150, 90, 250, 700, 875, 1050)
IndianaAvenue = Property("Indiana Avenue", 220, "red", 18, 150, 90, 250, 700, 875, 1050)
IllinoisAvenue = Property("Illinois Avenue", 240, "red", 20, 150, 100, 300, 750, 925, 1100)
BoRR = Railroad("B&O Railroad", 200, "railroad", 25)
AtlanticAvenue = Property("Atlantic Avenue", 260, "yellow", 22, 150, 110, 330, 800, 975, 1150)
VentnorAvenue = Property("Ventnor Avenue", 260, "yellow", 22, 150, 110, 330, 800, 975, 1150)
WaterWorks = Utility("Water Works", 150, "utility", None)
MarvinGardens = Property("Marvin Gardens", 280, "yellow", 24, 150, 120, 360, 850, 1025, 1200)
PacificAvenue = Property("Pacific Avenue", 300, "green", 26, 200, 130, 390, 900, 1100, 1275)
NorthCarolinaAvenue = Property("North Carolina Avenue", 300, "green", 26, 200, 130, 390, 900, 1100, 1275)
PennsylvaniaAvenue = Property("Pennsylvania Avenue", 320, "green", 28, 200, 150, 450, 1000, 1200, 1400)
ShortLine = Railroad("Short Line", 200, "railroad", 25)
ParkPlace = Property("Park Place", 350, "darkblue", 35, 175, 500, 1100, 700, 1300, 1500)
Boardwalk = Property("Boardwalk", 400, "darkblue", 50, 150, 200, 600, 1400, 1700, 2000)
CommunityChest = Deck("Community Chest", True)
Chance = Deck("Chance", True)

Tiles = [Go, MediterraneanAvenue, CommunityChest, BalticAvenue, IncomeTax, ReadingRR, OrientalAvenue, Chance, VermontAvenue, ConnecticutAvenue, VisitJail,
                       CharlesPlace, ElectricCompany, StatesAvenue, VirginiaAvenue, PennsylvaniaRR, JamesPlace, CommunityChest, TennesseeAvenue, NewYorkAvenue, FreeParking,
                       KentuckyAvenue, Chance, IndianaAvenue, IllinoisAvenue, BoRR, AtlanticAvenue, VentnorAvenue, WaterWorks, MarvinGardens, GotoJail,
                       PacificAvenue, NorthCarolinaAvenue, CommunityChest, PennsylvaniaAvenue, ShortLine, Chance, ParkPlace, LuxuryTax, Boardwalk]

SetToDeedMap = {"railroad": [ReadingRR, PennsylvaniaRR, BoRR, ShortLine],
                "utility": [ElectricCompany, WaterWorks],
                "brown": [MediterraneanAvenue, BalticAvenue],
                "lightblue": [OrientalAvenue, VermontAvenue, ConnecticutAvenue],
                "pink": [CharlesPlace, StatesAvenue, VirginiaAvenue],
                "orange": [JamesPlace, TennesseeAvenue, NewYorkAvenue],
                "red": [KentuckyAvenue, IndianaAvenue, IllinoisAvenue],
                "yellow": [AtlanticAvenue, VentnorAvenue, MarvinGardens],
                "green": [PacificAvenue, NorthCarolinaAvenue, PennsylvaniaAvenue],
                "darkblue": [ParkPlace, Boardwalk]}    

class MonopolyEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self, verbose = False, manual = False):
        super(MonopolyEnv, self).__init__()
        self.name = 'monopoly'
        self.manual = manual
        
        # Initializes players and board
        self.mNumPlayers = 2
        self.mPlayers : List[Player] = []
        self.mTiles = []
        self.initPlayers()
        self.mTiles = Tiles
        
        # Observation Space
        lower_range_values = np.array([[0,0,0,0]]*36)
        upper_range_values = np.array([[39,39,39,39]]+[[999999,999999,999999,999999]]+[[6,6,6,6]]*28) #row 0 is player position, row 1 is player money
        self.observation_space = gym.spaces.Box(low=lower_range_values, high=upper_range_values)
        
        # Action Space, where each discrete option corresponds to one deed (purchasable property)
        self.action_space = gym.spaces.Discrete(28)
        self.verbose = verbose
        
    def initPlayers(self):
        # initialize players and add to player list
        for i in range(self.mNumPlayers): # humans
            self.mPlayers.append(Player(i, True))
            self.mPlayers[i].InitPlayerList(self.mPlayers) # each player has access to list of players
    
    # TODO: Modify for Monopoly
    @property
    def observation(self):
        # 1D array of two balances (or we can also just represent in binary) OR 2D array of 2 players by 15 binary digits
        # 1D array of two positions (or we can just represent in binary) OR 2D array of 2 players by 40 possible positions
        # 2D array of 40 properties with 2 possible owners OR 3D array of 40 properties by 2 possible owners by 5 "levels" of ownership
        # and legal actions
        # and then we flatten them all and append them to each other and return
        
        if self.players[self.current_player_num].token.number == 1:
            position = np.array([x.number for x in self.board]).reshape(self.grid_shape)
        else:
            position = np.array([-x.number for x in self.board]).reshape(self.grid_shape)

        la_grid = np.array(self.legal_actions).reshape(self.grid_shape)
        out = np.stack([position,la_grid], axis = -1)
        return out

    # TODO: Modify for Monopoly
    @property
    def legal_actions(self, player: Player):
        # array of legal actions (i think)
        # the position of the current player
        # each Player has an mPos member variable
        # the ownership status of each deed
        # legal_actions = Discrete(23)
        # legal_actions = np.zero(23)
        # for each property i,
        #   if it is owned by the current player and they have a monopoly, set legal_actions[i] to 1
        #   if it is unowned by any player, set legal_actions[i] to 1
        # if in jail and have card, set legal_actions[-1] to 1
        legal_actions = []
        for action_num in range(len(self.board)):
            if self.board[action_num].number==0: #empty square
                legal_actions.append(1)
            else:
                legal_actions.append(0)
        return np.array(legal_actions)





    #Adapted to our need in monopoly theoritically
    def check_game_over(self):

        num_players = self.n_players
        numberOfPlayersBankrupt = 0
        winningPlayer = 0
        
        #check each player's balance
        for playerIndex in range(num_players):
            if (self.mPlayers[num_players].mBalance) == 0:
                numberOfPlayersBankrupt += 1
            else:
                winningPlayer = playerIndex
            #only one player has money and everyone else has no money
            if numberOfPlayersBankrupt + 1 == num_players:
                logger.debug(f"Only player {winningPlayer+1} has money left")
                #return tuple value, the first value is used in the Step funciton which can be used to punish models
                return 0, True
            
        return 0, False
                        
    @property
    def current_player(self):
        return self.players[self.current_player_num]


    # TODO: Modify for Monopoly
    def step(self, action):
        
        #each index represents a player, so the number of indexies in reward depends on number of players
        reward = [0] * self.mNumPlayers
        
        # check move legality
        board = self.mTiles
        player = self.mPlayers[self.current_player_num]
        
        # JAIL STUFF BEGIN
        # # print(player.mPlayerName + "'s turn:")
        if player.mTurnsInJail == 3: # out-of-jail check
            player.mTurnsInJail = 0
            # # print(player.mPlayerName + " is out of jail!")
        elif player.mTurnsInJail > 0: # in-jail check
            # # print(player.mPlayerName + " is in jail!")
            if player.mNumJailFree > 0: # get out of jail free card
                # if player.mIsAi:
                player.UseGetOutOfJailFree() # TODO: we will want to change this so that they don't use GOOJ every time
                # else:
                #     choice = input("Would you like to use your get out of jail free card? (yes/no) ")
                #     if choice == "yes":
                #         player.UseGetOutOfJailFree()
                #     else:    
                #         player.mTurnsInJail += 1
                #         continue
            elif player.mBalance >= const.JAIL_FEE:
                # if player.mIsAi:
                player.PayJailFee() # TODO: we will want to change this too
                # else:
                #     choice = input("Would you like to pay the $" + str(const.JAIL_FEE) + " jail fee? (yes/no) ")
                #     if choice == "yes":
                #         player.PayJailFee()
                #     else:    
                #         player.mTurnsInJail += 1
                #         continue
            else:
                player.mTurnsInJail += 1
                # should we return here?
                # continue
        # JAIL STUFF END
        
        
        if player.mIsAi:
            done = (len(self.mPlayers) <= 1)
            self.turn(player)
            # TODO: AI can build
            # TODO: AI can trade
            # self.stats(player) # TODO: render?
        # else:
        #     rolled = False
        #     while True:  
        #         command = input("Type a command, or type help: ")
        #         if command == "help":
        #             self.helpMenu()
        #         elif command == "end":
        #             if rolled: break
        #             # print("You haven't rolled yet!")
        #         elif command == "roll":
        #             if rolled:
        #                 pass
        #                 # print("You already rolled!")
        #             else:
        #                 rolled = True
        #                 self.turn(player)
        #         elif command == "stats":
        #             self.stats(player)
        #         # TODO: future implementation
        #         elif command == "trade":
        #             pass
        #         # LOGIC IS DOWN BUT NOT ABLE TO ACCESS CHILD CLASS FUNCTIONS
        #         elif command == "build":
        #             # pick property to build on from property list
        #             # if len(player.mDeedOwned) == 0:
        #                 # # print("No houses to build on")
        #                 # exit()
        #                 # self.helpMenu()
        #             # else:
        #                 # d : Deed
        #             count: int = 1
        #             for d in player.mDeedOwned:
        #                 if d.mSet != "utility" and d.mSet != "railroad":
        #                     # print(str(count) + ". " + str(d.mTileName)) 
        #                     pass
        #                 else:
        #                     # print(str(count) + ". " + str(d.mTileName) + " (can not build house)")
        #                     pass
        #                 count += 1
        #             select = int(input("Enter corresponding number to select property: "))
        #             developProperty: property = player.mDeedOwned[select - 1]
        #             # check if can build on selected property
        #             # # print(developProperty.BuildHouse(player))
        #             # # print("This is house cost", developProperty.mHouseCost, "This is player balance", player.mBalance)
        #             if player.mBalance >= developProperty.mHouseCost and developProperty.BuildHouse(player):
        #                 # if can build, check if enough balance, then build, increment house count
        #                 ans = input("Do you want to build here (y/n)? ")
        #                 if ans in "Yy":
        #                     developProperty.mNumHouse += 1
        #                     if developProperty.mNumHouse == 5: player.mHotelOwned += 1
        #                     else: player.mHouseOwned += 1
        #                     # print("You have built a house")
        #             else:
        #                 # print("Cannot build a house here.")
        #                 pass
        #         elif command == "quit":
        #             ans = input("Are you sure you want to quit the game? Your progress won't be saved. (y/n) ")
        #             if ans in "Yy":
        #                 done = True
        #         else:
        #             # print("Not a valid command. Type help to see list of valid commands.")
        #             pass
        #         if player.mBalance < 0: # bankruptcy check
        #             self.mPlayers.remove(player)
        #             # print(player.mPlayerName + " is bankrupt!")
        #             break
        player.mContinuousDoubles = 0
        
        # if (board[action].number != 0):  # not empty
        #     done = True
        #     reward = [1, 1]
        #     reward[self.current_player_num] = -1
        # else:
        #     board[action] = self.current_player.token
        #     self.turns_taken += 1
        #     r, done = self.check_game_over()
        #     reward = [-r,-r]
        #     reward[self.current_player_num] = r

        self.done = done

        if not done:
            self.current_player_num = (self.current_player_num + 1) % self.mNumPlayers

        return self.observation, reward, done, {}

    # TODO: Modify for Monopoly
    def reset(self):
        # TODO
        self.board = [Token('.', 0)] * self.num_squares # reset self.board to empty (no properties owned)
        self.players = [Player('1', Token('X', 1)), Player('2', Token('O', -1))] # reset self.players to array of two players: Player 1 and Player 2. Both without properties, both at GO (pos=0)
        self.current_player_num = 0
        self.turns_taken = 0
        self.done = False
        logger.debug(f'\n\n---- NEW GAME ----')
        return self.observation


    # TODO: Modify for Monopoly
    def render(self, mode='human', close=False, verbose = True):
        logger.debug('')
        if close:
            return
        if self.done:
            logger.debug(f'GAME OVER')
        else:
            logger.debug(f"It is Player {self.current_player.id}'s turn to move")
        r"""
        # print board
        # some unique identifier, if a player is on it, and property ownership
        # print rewards and selected action
        # print stats() for each player
        
        
        +---------+-----------+-----------------+-----------+-------------+
        |    GO   |  BROWN    | COMMUNITY CHEST  |  BROWN    | INCOME TAX  |
        |   1 2   |           |
        +---------+-----------+-----------------+-----------+-------------+
        |   JAIL  | LIGHT BLUE|      CHANCE      | LIGHT BLUE| LIGHT BLUE  |
        +---------+-----------+-----------------+-----------+-------------+
        | FREE    |   PINK    |    UTILITY      |   PINK    |    PINK     |
        | PARKING |           |                 |           |  RAILROAD   |
        +---------+-----------+-----------------+-----------+-------------+
        |  ORANGE |   CHANCE  |     ORANGE      |   ORANGE  |  RAILROAD   |
        +---------+-----------+-----------------+-----------+-------------+
        | GO TO   |    RED    |      RED        |  UTILITY  |     RED     |
        |  JAIL   |           |                 |           |             |
        +---------+-----------+-----------------+-----------+-------------+
        |  YELLOW |  YELLOW   | COMMUNITY CHEST  |  YELLOW   |  RAILROAD   |
        +---------+-----------+-----------------+-----------+-------------+
        |  CHANCE |   GREEN   |      GREEN      |  UTILITY  |    GREEN    |
        +---------+-----------+-----------------+-----------+-------------+
        | LUXURY  |   BLUE    |   INCOME TAX    |   BLUE    |  RAILROAD   |
        |   TAX   |           |                 |           |             |
        +---------+-----------+-----------------+-----------+-------------+
        """
        
        # logger.debug(' '.join([x.symbol for x in self.board[:self.grid_length]]))
        # logger.debug(' '.join([x.symbol for x in self.board[self.grid_length:self.grid_length*2]]))
        # logger.debug(' '.join([x.symbol for x in self.board[(self.grid_length*2):(self.grid_length*3)]]))

        if self.verbose:
            logger.debug(f'\nObservation: \n{self.observation}')
        
        if not self.done:
            logger.debug(f'\nLegal actions: {[i for i,o in enumerate(self.legal_actions) if o != 0]}')


    def rules_move(self):
        if self.current_player.token.number == 1:
            b = [x.number for x in self.board]
        else:
            b = [-x.number for x in self.board]

        # Check computer win moves
        for i in range(0, self.num_squares):
            if b[i] == 0 and testWinMove(b, 1, i):
                logger.debug('Winning move')
                return self.create_action_probs(i)
        # Check player win moves
        for i in range(0, self.num_squares):
            if b[i] == 0 and testWinMove(b, -1, i):
                logger.debug('Block move')
                return self.create_action_probs(i)
        # Check computer fork opportunities
        for i in range(0, self.num_squares):
            if b[i] == 0 and testForkMove(b, 1, i):
                logger.debug('Create Fork')
                return self.create_action_probs(i)
        # Check player fork opportunities, incl. two forks
        playerForks = 0
        for i in range(0, self.num_squares):
            if b[i] == 0 and testForkMove(b, -1, i):
                playerForks += 1
                tempMove = i
        if playerForks == 1:
            logger.debug('Block One Fork')
            return self.create_action_probs(tempMove)
        elif playerForks == 2:
            for j in [1, 3, 5, 7]:
                if b[j] == 0:
                    logger.debug('Block 2 Forks')
                    return self.create_action_probs(j)
        # Play center
        if b[4] == 0:
            logger.debug('Play Centre')
            return self.create_action_probs(4)
        # Play a corner
        for i in [0, 2, 6, 8]:
            if b[i] == 0:
                logger.debug('Play Corner')
                return self.create_action_probs(i)
        #Play a side
        for i in [1, 3, 5, 7]:
            if b[i] == 0:
                logger.debug('Play Side')
                return self.create_action_probs(i)


    # [0.01, 0.01, 0.01, 0.92, 0.01, 0.01]
    def create_action_probs(self, action):
        action_probs = [0.01] * self.action_space.n
        action_probs[action] = 0.92
        return action_probs   


    def checkWin(b, m):
        return ((b[0] == m and b[1] == m and b[2] == m) or  # H top
                (b[3] == m and b[4] == m and b[5] == m) or  # H mid
                (b[6] == m and b[7] == m and b[8] == m) or  # H bot
                (b[0] == m and b[3] == m and b[6] == m) or  # V left
                (b[1] == m and b[4] == m and b[7] == m) or  # V centre
                (b[2] == m and b[5] == m and b[8] == m) or  # V right
                (b[0] == m and b[4] == m and b[8] == m) or  # LR diag
                (b[2] == m and b[4] == m and b[6] == m))  # RL diag


    def checkDraw(b):
        return 0 not in b

    def getBoardCopy(b):
        # Make a duplicate of the board. When testing moves we don't want to 
        # change the actual board
        dupeBoard = []
        for j in b:
            dupeBoard.append(j)
        return dupeBoard

    def testWinMove(b, mark, i):
        # b = the board
        # mark = 0 or X
        # i = the square to check if makes a win 
        bCopy = getBoardCopy(b)
        bCopy[i] = mark
        return checkWin(bCopy, mark)


    def testForkMove(b, mark, i):
        # Determines if a move opens up a fork
        bCopy = getBoardCopy(b)
        bCopy[i] = mark
        winningMoves = 0
        for j in range(0, 9):
            if testWinMove(bCopy, mark, j) and bCopy[j] == 0:
                winningMoves += 1
        return winningMoves >= 2

    def turn(self, player: Player):
            while True:
                tile, doubles, rollSum = self.roll(player) # roll dice and move player to appropriate space
                # player.MotorRequest(rollSum) # physically move player to tile
                # print(player.mPlayerName + " landed on " + tile.mTileName + "!")
                if player.mTurnsInJail == 0: tile.action(player, rollSum) # execute action when land on space
                if (not doubles) or (player.mTurnsInJail > 0): break
        
    def roll(self, player: Player): # roll dice and move player to appropriate space
        doubles = False
        dice, rollSum = self.rollDice(player)
        if dice[0] == dice[1]: # doubles check
            doubles = True
            # print(player.mPlayerName + " rolled doubles!")
            player.mContinuousDoubles += 1
            if player.mContinuousDoubles == 3: # go directly to jail after 3 consecutive doubles
                player.mPos = 10
                player.mTurnsInJail = 1
                # print(player.mPlayerName + " rolled three consecutive doubles! Go to jail!")
                return None
        if (player.mPos + rollSum) >= 40: # passed go check
            player.mBalance += const.GO_MONEY
            # print(player.mPlayerName + " passed go and earned $200!")
        player.mPos = (player.mPos + rollSum) % 40 # move player appropriate number of spaces
        tile = self.mTiles[player.mPos]
        return tile, doubles, rollSum

    def rollDice(self, player: Player): # simulates rolling two dice
        dice = (random.randint(1,6), random.randint(1,6))
        sum = dice[0] + dice[1]
        # print(player.mPlayerName + " rolled " + str(sum) + "!")
        return dice, sum

    # def stats(self, player: Player): # # print stats
    #     # print(player.mPlayerName + "'s stats:")
    #     # print("Balance: $" + str(player.mBalance))
    #     # print("Properties:")
    #     if len(player.mDeedOwned) == 0:
    #         pass
    #         # print("(None)")
    #     else:
    #         d : Deed
    #         for d in player.mDeedOwned:
    #             # print(d.mTileName + " [" + d.mSet + "]")
        
    #     if (player.mNumJailFree > 0):
    #         pass
    #         # print (player.mNumJailFree, "Get out of Jail free")

    # def helpMenu(self): # # print help menu
        # print("Help menu:")
        # print("roll = roll dice")
        # print("stats = see your balance and properties")
        # print("build = build houses/hotels")
        # print("trade = trade with another player")
        # print("end = end your turn")
        # print("quit = quit the game")
        # print("help = see this list of commands")