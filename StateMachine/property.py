from deed import Deed
from player import Player

class Property(Deed):
    def __init__(self, mTileName, mCost, mSet, mRent, mHouseCost):
        super().__init__(mTileName, mCost, mSet, mRent)
        # HOUSE INFO
        self.mNumHouse = 0
        self.mHouseCost = mHouseCost

        # RENT BASED ON HOUSE COUNT
        self.mOneHouseRent = 0
        self.mTwoHouseRent = 0
        self.mThreeHouseRent = 0
        self.mFourHouseRent = 0
        self.mFiveHouseRent = 0 #hotel
    
    def InitRent(self, mOneHouseRent, mTwoHouseRent, mThreeHouseRent, mFourHouseRent, mFiveHouseRent):
        self.mOneHouseRent = mOneHouseRent
        self.mTwoHouseRent = mTwoHouseRent
        self.mThreeHouseRent = mThreeHouseRent
        self.mFourHouseRent = mFourHouseRent
        self.mFiveHouseRent = mFiveHouseRent
        
    
    def CalculatePropertyRent(self) -> int:
        if self.mNumHouse == 0:
            return self.mRent
        # elif CheckMonopoly()
        elif None:
            return self.mRent * 2
        elif self.mNumHouse == 1:
            return self.mOneHouseRent
        elif self.mNumHouse == 2:
            return self.mTwoHouseRent
        elif self.mNumHouse == 3:
            return self.mThreeHouseRent
        elif self.mNumHouse == 4:
            return self.mFourHouseRent
        elif self.mNumHouse == 5:
            return self.mFiveHouseRent
    
    # TODO: complete function
    # def CheckMonopoly() -> bool:
        # Brainstorm
        # use the mOwner variable and the constructed dictionary
        # Have list of lists with each set as a sub list and then check this
        # list against the deed owned list of player with a counter to compare
        # against the length of the sublist to check if a monopoly or not
        # instead of a list of lists use a dictionary to store each set