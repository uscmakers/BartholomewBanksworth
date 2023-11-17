import const
# import Embedded.util as util

# from deed import Deed
# from property import Property
# from railroad import Railroad
# from utility import Utility
# from typing import List

class Player:
    def __init__(self, index: int, mIsAi: bool):
        # PLAYER INFO
        self.index = index
        self.mPos = 0
        self.mIsAi = mIsAi
        self.mPlayerName = ""

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
        self.mBalance -= const.JAIL_FEE
    
    def UseGetOutOfJailFree(self):
        print(self.mPlayerName + " used their get out of jail free card!")
        self.mTurnsInJail = 0
        self.mNumJailFree -= 1
        
    # def MotorRequest(self, deltaPos: int):
        # util.makeRequest(self.index, self.mPos, deltaPos)