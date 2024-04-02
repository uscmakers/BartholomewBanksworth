import Embedded.util as util
# from deed import Deed
# from property import Property
# from railroad import Railroad
# from utility import Utility
# from typing import List

# CONSTANTS

JAIL_FEE = 50
GO_MONEY = 200
STARTING_BALANCE = 1500
AVAILABLE_HOUSE = 32
AVAILABLE_HOTEL = 12

class Player:
    def __init__(self, index: int, mIsAi: bool):
        # PLAYER INFO
        self.index = index
        self.mPos = 0
        self.mIsAi = mIsAi

        # MONEY INFO
        self.mBalance = const.STARTING_BALANCE
        self.mNetWorth = self.mBalance

        # PROPERTY INFO
        self.mDeedOwned = []
        self.mHouseOwned = 0
        self.mHotelOwned = 0

        # JAIL INFO
        self.mTurnsInJail = 0
        self.mNumJailFree = 0
        self.mContinuousDoubles = 0

    def InitPlayerList(self, mPlayerList):
        self.mPlayerList = mPlayerList

    def CalculateNetWorth(self):
        self.mNetWorth = self.mBalance

        for deed in self.mDeedOwned:
            self.mNetWorth += deed.mCost
            if deed.mHouseCount != 0:
                self.mNetWorth += (deed.mHouseCount * deed.mHouseCost)

    def NamePlayer(self, i: int):
        if not self.mIsAi:
            self.mPlayerName = input("Enter name for Player " + str(i) + ": ")
        else :
            self.mPlayerName = "Bartholomew Banksworth"

    def GoToJail(self):
        self.mTurnsInJail = 1
        # self.MotorRequest(10-self.mPos) # TODO: physically move player to jail
        self.mPos = 10
    
    def PayJailFee(self):
        print(self.mPlayerName + " paid $" + str(const.JAIL_FEE) + " to get out of jail!")
        self.mTurnsInJail = 0
        self.mBalance -= const.JAIL_FEE
    
    def UseGetOutOfJailFree(self):
        print(self.mPlayerName + " used their get out of jail free card!")
        self.mTurnsInJail = 0
        self.mNumJailFree -= 1
        
    # def MotorRequest(self, deltaPos: int):
    #     util.makeRequest(self.index, self.mPos, deltaPos)
    def getBalance(self):
        return self.mBalance
    def getPlayerPosition(self):
        return self.mPos

    def reset(self):
        # PLAYER INFO
        self.mPos = 0

        # MONEY INFO
        self.mBalance = const.STARTING_BALANCE
        self.mNetWorth = self.mBalance

        # PROPERTY INFO
        self.mDeedOwned = []
        self.mHouseOwned = 0
        self.mHotelOwned = 0

        # JAIL INFO
        self.mTurnsInJail = 0
        self.mNumJailFree = 0
        self.mContinuousDoubles = 0