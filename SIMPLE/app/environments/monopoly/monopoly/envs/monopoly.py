# Adapted from https://mblogscode.com/2016/06/03/python-naughts-crossestic-tac-toe-coding-unbeatable-ai/

import gym
from gym.spaces import Dict, Discrete
import numpy as np

import config

from stable_baselines import logger

import random
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

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.table import Table
import numpy as np
from matplotlib.animation import FuncAnimation
import cv2
import os
from constants import property_stuff
# CONSTANTS

JAIL_FEE = 50
GO_MONEY = 200
STARTING_BALANCE = 1500
AVAILABLE_HOUSE = 32
AVAILABLE_HOTEL = 12
PROPERTY_REWARD = 1000

# TILES

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

# Deeds = [MediterraneanAvenue, BalticAvenue, OrientalAvenue, VermontAvenue, ConnecticutAvenue, CharlesPlace, StatesAvenue, VirginiaAvenue, JamesPlace, TennesseeAvenue,
#          NewYorkAvenue, KentuckyAvenue, IndianaAvenue, IllinoisAvenue, AtlanticAvenue, VentnorAvenue, MarvinGardens, PacificAvenue,
#          NorthCarolinaAvenue, PennsylvaniaAvenue, ParkPlace, Boardwalk, ReadingRR, PennsylvaniaRR, BoRR, ShortLine, ElectricCompany, WaterWorks]

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

properties_data = [
    ['Go', 'None', '0'],
    ['Mediterranean Avenue', 'None', '0'],
    ['Community Chest', 'None', '0'],
    ['Baltic Avenue', 'None', '0'],
    ['Income Tax', 'None', '0'],
    ['Reading Railroad', 'None', '0'],
    ['Oriental Avenue', 'None', '0'],
    ['Chance', 'None', '0'],
    ['Vermont Avenue', 'None', '0'],
    ['Connecticut Avenue', 'None', '0'],
    ['Jail', 'None', '0'],
    ['St. Charles Place', 'None', '0'],
    ['Electric Company', 'None', '0'],
    ['States Avenue', 'None', '0'],
    ['Virginia Avenue', 'None', '0'],
    ['Pennsylvania Railroad', 'None', '0'],
    ['St. James Place', 'None', '0'],
    ['Community Chest', 'None', '0'],
    ['Tennessee Avenue', 'None', '0'],
    ['New York Avenue', 'None', '0'],
    ['Free Parking', 'None', '0'],
    ['Kentucky Avenue', 'None', '0'],
    ['Chance', 'None', '0'],
    ['Indiana Avenue', 'None', '0'],
    ['Illinois Avenue', 'None', '0'],
    ['B&O Railroad', 'None', '0'],
    ['Atlantic Avenue', 'None', '0'],
    ['Ventnor Avenue', 'None', '0'],
    ['Water Works', 'None', '0'],
    ['Marvin Gardens', 'None', '0'],
    ['Go to Jail', 'None', '0'],
    ['Pacific Avenue', 'None', '0'],
    ['North Carolina Avenue', 'None', '0'],
    ['Community Chest', 'None', '0'],
    ['Pennsylvania Avenue', 'None', '0'],
    ['Short Line', 'None', '0'],
    ['Chance', 'None', '0'],
    ['Park Place', 'None', '0'],
    ['Luxury Tax', 'None', '0'],
    ['Boardwalk', 'None', '0']
]


property_table_colors = [['None', 'None', 'None'], 
                         ['indianred', 'None', 'None'], 
                         ['None', 'None', 'None'],
                         ['indianred', 'None', 'None'],
                         ['None', 'None', 'None'],
                         ['Silver', 'None', 'None'],
                         ['Aqua', 'None', 'None'],
                         ['None', 'None', 'None'],
                         ['Aqua', 'None', 'None'],
                         ['Aqua', 'None', 'None'],
                         ['None', 'None', 'None'],
                         ['mediumpurple', 'None', 'None'],
                         ['lightpink', 'None', 'None'],
                         ['mediumpurple', 'None', 'None'],
                         ['mediumpurple', 'None', 'None'],
                         ['Silver', 'None', 'None'],
                         ['Orange', 'None', 'None'],
                         ['None', 'None', 'None'],
                         ['Orange', 'None', 'None'],
                         ['Orange', 'None', 'None'],
                         ['None', 'None', 'None'],
                         ['Red', 'None', 'None'],
                         ['None', 'None', 'None'],
                         ['Red', 'None', 'None'],
                         ['Red', 'None', 'None'],
                         ['Silver', 'None', 'None'],
                         ['Yellow', 'None', 'None'],
                         ['Yellow', 'None', 'None'],
                         ['lightpink', 'None', 'None'],
                         ['Yellow', 'None', 'None'],
                         ['None', 'None', 'None'],
                         ['springgreen', 'None', 'None'],
                         ['springgreen', 'None', 'None'],
                         ['None', 'None', 'None'],
                         ['springgreen', 'None', 'None'],
                         ['Silver', 'None', 'None'],
                         ['None', 'None', 'None'],
                         ['cornflowerblue', 'None', 'None'],
                         ['None', 'None', 'None'],
                         ['cornflowerblue', 'None', 'None']]   

def createFrame(players_data):
    # TilesIdx = {MediterraneanAvenue: 1, BalticAvenue: 2, ReadingRR: 23, OrientalAvenue: 3, VermontAvenue: 4, ConnecticutAvenue: 5,
    #                    CharlesPlace: 6, ElectricCompany: 27, StatesAvenue: 7, VirginiaAvenue: 8, PennsylvaniaRR: 24, JamesPlace: 9, TennesseeAvenue: 10, NewYorkAvenue: 11,
    #                    KentuckyAvenue: 12, IndianaAvenue: 13, IllinoisAvenue: 14, BoRR: 25, AtlanticAvenue: 15, VentnorAvenue: 16, WaterWorks: 28, MarvinGardens: 17,
    #                    PacificAvenue: 18, NorthCarolinaAvenue: 19, PennsylvaniaAvenue: 24, ShortLine: 26, ParkPlace:21, Boardwalk: 22}
    
    for i in range(len(properties_data)):
        if property_table_colors[i][0] != None:
            for j in property_stuff.Deeds:
                if isinstance(j, Deed):
                    # updating owner
                    if j.mTileName == properties_data[i][0] and j.mOwner != None and properties_data[i][1] == None:
                        properties_data[i][1] = j.mOwner
                    # updating house count
                    if isinstance(j, Property) and j.mTileName == properties_data[i][0] and j.mNumHouse > 0 and properties_data[i][2] == 0:
                        properties_data[i][1] = j.mOwner

                     
            
    # Create DataFrames
    df_properties = pd.DataFrame(properties_data)
    df_players = pd.DataFrame(players_data)

    # Create a table for properties
    table_properties = plt.table(cellText=properties_data, bbox=[0, 0, 0.6, 1], colLabels=('Property', 'Group', 'Color Code'), cellColours=property_table_colors, cellLoc='center')
    for i, col in enumerate(df_properties.columns):
        table_properties.auto_set_column_width([i])

    # Formatting for properties table
    table_properties.auto_set_font_size(False)
    table_properties.set_fontsize(8)
    table_properties.scale(1.2, 1.2)

    # Create a table for players
    table_players = plt.table(cellText=players_data, bbox=[0.65, 0.5, 0.35, 0.45], colLabels=('Player', 'Balance', 'Other'))
    for i, col in enumerate(df_players.columns):
        table_players.auto_set_column_width([i])
            
    # Create a "table" for next action
    table_ai_action = plt.text(0.65, 0.25, f'test', wrap=True, color='blue')

    plt.suptitle('Monopoly Properties and Players', fontsize=16)

class MonopolyEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self, verbose = False, manual = False):
        super(MonopolyEnv, self).__init__()
        self.name = 'monopoly'
        self.manual = manual
        
        # Initializes players and board
        # self.n_players = int(input("How many players want to face Bartholomew Banksworth? "))
        # self.n_players += 1
        self.n_players = 2
        self.player_type_list = []
        self.mPlayers : List[Player] = []
        self.mTiles = []
        self.initPlayers()
        self.mTiles = property_stuff.Tiles
        self.n_turns = 0
        
        # Observation Space
        lower_range_values = np.array([[0]*self.n_players]*30).flatten()
        lower_range_values = np.concatenate((lower_range_values, np.array([[0]]*31).flatten()))
        upper_range_values = np.array([[39]*self.n_players]+[[999999]*self.n_players]+([[6]*self.n_players]*28)).flatten() #row 0 is player position, row 1 is player money
        upper_range_values = np.concatenate((upper_range_values, np.array([[1]]*31).flatten()))
        self.observation_space = gym.spaces.Box(low=lower_range_values, high=upper_range_values)
        self.observation_space = self.observation_space
        # Action Space, where each discrete option corresponds to one deed (purchasable property)
        self.action_space = gym.spaces.Discrete(31)
        self.verbose = verbose
        
        # Render stuff
        fig, ax = plt.subplots(figsize=(15, 8))
        ani = FuncAnimation(fig, self.render, frames=range(10), repeat=False)
        self.mNumFrames = 0
        
    def initPlayers(self):
        # # initialize players and add to player list
        # self.mPlayers.append(Player(0, True, "Bartholomew Banksworth"))
        # for i in range(1, self.n_players): # humans
        #     mPlayerName = input("Enter Player " + str(i) + " name: ")
        #     self.mPlayers.append(Player(i, False, mPlayerName))
        self.mPlayers.append(Player(0, True, "AI1"))
        self.mPlayers.append(Player(1, True, "AI2"))
        for i in range(0, self.n_players):
            self.mPlayers[i].InitPlayerList(self.mPlayers) # each player has access to list of players
    
    @property
    def observation(self):
        # 1D array of two balances (or we can also just represent in binary) OR 2D array of 2 players by 15 binary digits
        # 1D array of two positions (or we can just represent in binary) OR 2D array of 2 players by 40 possible positions
        # 2D array of 40 properties with 2 possible owners OR 3D array of 40 properties by 2 possible owners by 5 "levels" of ownership
        # and legal actions
        # and then we flatten them all and append them to each other and return

        #the balances of players represented between 0 - 1
        currentPlayer = self.current_player

        
        balances = []
        balances.append(currentPlayer.getBalance())
        for player_num in range(self.n_players-1):
            player_num = (player_num + self.current_player_num + 1)%self.n_players
            balances.append(self.mPlayers[player_num].getBalance())

        balances = np.array(balances)
        balances = balances.flatten()

        #player positions in a 2D array of 40 spaces
        
        positions = np.array([0] * self.n_players)
        positions[0] = currentPlayer.getPlayerPosition()
        
        for player_num in range(self.n_players-1):
            player_num = (player_num + self.current_player_num + 1)%self.n_players
            positions[player_num] = self.mPlayers[player_num].getPlayerPosition()
            
        positions = positions.flatten()

        #property information
        # propertyInfo = np.zeros(shape=(2,len(Tiles)))
        propertyInfo = np.zeros(shape=(self.n_players,28))

        for properties in currentPlayer.mDeedOwned:
                if (type(properties) is Property):
                    propertyInfo[self.current_player_num, property_stuff.Deeds.index(properties)] = properties.mNumHouse + 1
                else:
                    propertyInfo[self.current_player_num, property_stuff.Deeds.index(properties)] = 1

        for player_num in range(self.n_players-1):
            player_num = (player_num + self.current_player_num + 1)%self.n_players
            for properties in self.mPlayers[player_num].mDeedOwned:
                if (type(properties) is Property):
                    propertyInfo[player_num, property_stuff.Deeds.index(properties)] = properties.mNumHouse + 1
                else:
                    propertyInfo[player_num, property_stuff.Deeds.index(properties)] = 1
        propertyInfo = propertyInfo.flatten()

        la_grid = self.legal_actions
        la_grid = la_grid.flatten()

        #concatenate everything
        result = np.concatenate((positions, balances, propertyInfo, la_grid))
        return result

        # if self.players[self._player_numcurrent].token.number == 1:
        #     position = np.array([x.number for x in self.board]).reshape(self.grid_shape)
        # else:
        #     position = np.array([-x.number for x in self.board]).reshape(self.grid_shape)

        # la_grid = np.array(self.legal_actions).reshape(self.grid_shape)
        # out = np.stack([position,la_grid], axis = -1)
        # return out

    @property
    def legal_actions(self):
        # idx 0 is do nothing
        # idx 1 - 28 is deed
        # idx 29 is pay to GOOJ
        # idx 30 is GOOJ card
        #each key corresponds to the position of the tiles in the legal actions array
        tiles = property_stuff.Tiles
        TilesIdx = {property_stuff.MediterraneanAvenue: 1, property_stuff.BalticAvenue: 2, property_stuff.ReadingRR: 23, property_stuff.OrientalAvenue: 3, property_stuff.VermontAvenue: 4, property_stuff.ConnecticutAvenue: 5,
                       property_stuff.CharlesPlace: 6, property_stuff.ElectricCompany: 27, property_stuff.StatesAvenue: 7, property_stuff.VirginiaAvenue: 8, property_stuff.PennsylvaniaRR: 24, property_stuff.JamesPlace: 9, property_stuff.TennesseeAvenue: 10, property_stuff.NewYorkAvenue: 11,
                       property_stuff.KentuckyAvenue: 12, property_stuff.IndianaAvenue: 13,property_stuff.IllinoisAvenue: 14, property_stuff.BoRR: 25, property_stuff.AtlanticAvenue: 15, property_stuff.VentnorAvenue: 16, property_stuff.WaterWorks: 28, property_stuff.MarvinGardens: 17,
                       property_stuff.PacificAvenue: 18, property_stuff.NorthCarolinaAvenue: 19, property_stuff.PennsylvaniaAvenue: 24, property_stuff.ShortLine: 26, property_stuff.ParkPlace:21, property_stuff.Boardwalk: 22}
        
        # array of legal actions (i think)
        legal_actions = np.zeros(31)
        #always allwoed to do nothing
        legal_actions[0] = 1
        player = self.current_player
        # the position of the current player
        # each Player has an mPos member variable
        for deed in player.mDeedOwned:
            idx = TilesIdx[deed]
            if type(deed) is Property:
                # check if has monopoly on property
                # if monopoly then change legal_actions to 1 for color group
                if deed.BuildHouse(self.current_player):
                # 1 over here => can build a house
                    legal_actions[idx] = 1
                else:
                    legal_actions[idx] = 0
        # check current position
        if type(tiles[player.mPos]) in [Property, Railroad, Utility]:
            currDeedTile = tiles[player.mPos]
            idx = TilesIdx[currDeedTile]
            if currDeedTile.mOwner is None and self.current_player.mBalance > currDeedTile.mCost:
                legal_actions[idx] = 1
            else:
                legal_actions[idx] = 0
            # if deed owner is null (prperties, utilities, railroads)
            # can buy
            # 1 => can buy property
        
        # the ownership status of each deed
        # for each property i,
        #   if it is owned by the current player and they have a monopoly, set legal_actions[i] to 1
        #   if it is unowned by any player, set legal_actions[i] to 1
        # if in jail and have card, set legal_actions[-1] to 1
        
        # START LEGAL ACTION JAILL STUFF
        if player.mTurnsInJail > 0: # in-jail check
            if player.mNumJailFree > 0: # get out of jail free card
                # can use GOOJFC
                legal_actions[29] = 1
            else:
                legal_actions[29] = 0
            
            if player.mBalance >= JAIL_FEE:
                legal_actions[30] = 1
            else:
                legal_actions[30] = 0
        return np.array(legal_actions)

    #Adapted to our need in monopoly theoritically
    def check_game_over(self):

        num_players = self.n_players
        numberOfPlayersBankrupt = 0
        winningPlayer = 0
        
        #check each player's balance
        for playerIndex in range(num_players):
            if (self.mPlayers[num_players].mBalance) <= 0:
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
        return self.mPlayers[self.current_player_num]

    def step(self, action):
        
        # assumption: action is an integer between 0 and 27 (obtained from action space of Discrete[28])
        #print("Ai" + str(self.current_player_num) + " is about to take action: " + str(action)) 
        # if (self.observation[60+action] == 0):
        #     # print("Using illegal action")
        #     action = 0
        #     reward = [0, 0]
        #     reward[self.current_player_num] = -1
        #     done = False
        #     self.current_player_num = (self.current_player_num + 1) % self.n_players
        #     return self.observation, reward, done, {}
        #each index represents a player, so the number of indexies in reward depends on number of players
        reward = [0] * self.n_players
        
        # INITIALIZATION
        tiles = self.mTiles
        deeds = property_stuff.Deeds
        player = self.mPlayers[self.current_player_num]
        
        # UPDATE JAIL
        if player.mTurnsInJail == 3: # out-of-jail check
            print(player.mPlayerName + " is out of jail!")
            player.mTurnsInJail = 0
        if player.mTurnsInJail > 0: # in-jail check
            print(player.mPlayerName + " is in jail!")
            player.mTurnsInJail += 1 
        
        # ACTION CHOOSING
        if action is 29:
            player.UseGetOutOfJailFree()
        elif action is 30:
            player.PayJailFee()
        
        #if ((self.current_player_num+1)%2 == 1):
            #input("\nPress enter to roll!")
        self.turn((self.current_player_num+1)%2)
        
        if 1 <= action <= 28:
            if deeds[action-1].mOwner is None:
                deeds[action-1].purchase(self.current_player)
            elif (type(deeds[action-1]) is Property):
                deeds[action-1].mNumHouse += 1
                if deeds[action-1].mNumHouse == 5: 
                    player.mHotelOwned += 1
                    self.current_player.mBalance -= deeds[action-1].mHouseCost
                else: 
                    player.mHouseOwned += 1
                    self.current_player.mBalance -= deeds[action-1].mHouseCost
                    
        if action is 29:
            self.current_player.UseGetOutOfJailFree()
        
        if action is 30:
            self.current_player.PayJailFee() 
        
        # DETERMINE DONE
        done = False
        for player in self.mPlayers:
            if player.mBalance < 0:
                print("Done is True for a player!")
                done = True
        self.done = done

        if not done:
            self.current_player_num = (self.current_player_num + 1) % self.n_players
            
        # REWARD CALCULATION
        totalBalance = 0
        for player in self.mPlayers:
            totalBalance += player.mBalance
            for deed in player.mDeedOwned:
                totalBalance += deed.mCost * PROPERTY_REWARD
        
        reward = np.zeros(len(self.mPlayers))
        for playerIndex in range(len(self.mPlayers)):
            player = self.mPlayers[playerIndex]
            if (totalBalance != 0):
                reward_amount = player.getBalance()
                for deed in player.mDeedOwned:
                    reward_amount += deed.mCost * PROPERTY_REWARD
                reward[playerIndex] = (reward_amount/totalBalance - 0.5)
                
                
        #self.current_player_num = (self.current_player_num + 1) % self.n_players
        self.n_turns += 1
        if (self.n_turns > 400):
            print("Played over 300 turns! Resetting!")
            done = True
        return self.observation, reward, done, {}

    def reset(self):
        # reset self.board to empty (no properties owned)
        for tile in property_stuff.Tiles:
            tile.reset()
            
        # reset players
        for player in self.mPlayers:
            player.reset()
            
        self.n_turns = 0
        self.current_player_num = 0
        
        self.done = False
        
        # Convert PNG images to an MP4 video using OpenCV
        size = (0,0)
        frames = []
        for i in range(self.mNumFrames):
            img = cv2.imread(f'frame_{i:03d}.png')
            if (img is not None):
                height, width, layers = img.shape
                size = (width,height)
                frames.append(img)

        # Define the codec and create a VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter('output.mp4', fourcc, 1.0, size)

        # Write the frames to the video
        for frame in frames:
            out.write(frame)

        # Release the VideoWriter object
        out.release()

        # Cleanup: Remove the PNG images
        for i in range(self.mNumFrames):
            os.remove(f'frame_{i:03d}.png')
        self.mNumFrames = 0

        print("END OF GAME\n\nSTARTING NEW GAME")
         
        logger.debug(f'\n\n---- NEW GAME ----')
        return self.observation
    
    def render(self, mode='human', close=False, verbose = True):
        # self.turn(self.current_player)
        # np.set_printoptions(suppress=True,precision=3)
        # print(self.current_player_num, "POSITION:", self.observation[0:2])
        # print(self.current_player_num, "BALANCE:", self.observation[2:4])
        # print(self.current_player_num, "PROPERTY INFO:", self.observation[4:60])
        # print(self.current_player_num, "LEGAL ACTIONS:", self.observation[60:])
        # plt.clf()
        # createFrame(np.array([[1, self.mPlayers[0].getBalance(), self.mPlayers[0].getPlayerPosition()], [2, self.mPlayers[1].getBalance(), self.mPlayers[1].getPlayerPosition()]]))
        # plt.savefig(f'frame_{self.mNumFrames:03d}.png')
        # self.mNumFrames += 1

        if self.verbose:
            logger.debug(f'\nObservation: \n{self.observation}')
        
        if not self.done:
            logger.debug(f'\nLegal actions: {[i for i,o in enumerate(self.legal_actions) if o != 0]}')

# OUR FUNCTIONS START
    def turn(self, playerNum: int):
        player = self.mPlayers[playerNum]
        while True:
            tile, doubles, rollSum = self.roll(player)
            doubles = False
            # if (roll is not None):
            #     tile, doubles, rollSum = roll
            # player.MotorRequest(rollSum) # physically move player to tile
            if player.mTurnsInJail == 0: 
                return tile.action(player, rollSum) # execute action when land on space
            if (not doubles) or (player.mTurnsInJail > 0): break
            
            return 0
        
    def roll(self, player: Player): # roll dice and move player to appropriate space
        doubles = False
        dice, rollSum = self.rollDice(player)
        #print (rollSum)
        if dice[0] == dice[1]: # doubles check
            #doubles = True
            # print(player.mPlayerName + " rolled doubles!")
            #player.mContinuousDoubles += 1
            if player.mContinuousDoubles == 3: # go directly to jail after 3 consecutive doubles
                player.mPos = 10
                player.mTurnsInJail = 1
                # print(player.mPlayerName + " rolled three consecutive doubles! Go to jail!")
                return None
        if (player.mPos + rollSum) >= 40: # passed go check
            player.mBalance += GO_MONEY
            # print(player.mPlayerName + " passed go and earned $200!")
        player.mPos = (player.mPos + rollSum) % 40 # move player appropriate number of spaces
        tile = self.mTiles[player.mPos]
        return tile, doubles, rollSum

    def rollDice(self, player: Player): # simulates rolling two dice
        import time
        random.seed(time.time())
        dice = (random.randint(1,6), random.randint(1,6))
        sum = dice[0] + dice[1]
        print(player.mPlayerName + " rolled " + str(sum) + "!")
        return dice, sum

    def helpMenu(self): # print help menu
        print("Help menu:")
        print("roll = roll dice")
        print("stats = see your balance and properties")
        print("build = build houses/hotels")
        print("end = end your turn")
        print("quit = quit the game")
        print("help = see this list of commands")
        
    def stats(self, player_num: int):
        player = self.current_player
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
