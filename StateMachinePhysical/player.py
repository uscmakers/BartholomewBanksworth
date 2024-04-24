import const
import Embedded.util as util

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
        self.mCJailFree = 0
        self.mCCJailFree = 0
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
        oldPos = self.mPos
        self.mPos = 10
        self.MotorRequest(10-oldPos) # physically move player to jail
    
    def PayJailFee(self):
        print(self.mPlayerName + " paid $" + str(const.JAIL_FEE) + " to get out of jail!")
        self.mBalance -= const.JAIL_FEE
        self.mTurnsInJail = 0
    
    def UseGetOutOfJailFree(self):
        if self.mCJailFree > 0:
            self.mCJailFree -= 1
        elif self.mCCJailFree > 0:
            self.mCCJailFree -= 1
        self.mTurnsInJail = 0
        print(self.mPlayerName + " used their get out of jail free card!")
        
    def MotorRequest(self, deltaPos: int):
        pass
    #     util.makeRequest(self.index, deltaPos, self.mPos)