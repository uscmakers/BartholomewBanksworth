from deed import Deed
from player import Player

class Property(Deed):
    def __init__(self, mTileName, mCost, mSet, mRent, mHouseCost, mOneHouseRent, mTwoHouseRent, mThreeHouseRent, mFourHouseRent, mFiveHouseRent):
        super().__init__(mTileName, mCost, mSet, mRent)
        # HOUSE INFO
        self.mNumHouse = 0
        self.mHouseCost = mHouseCost

        # RENT BASED ON HOUSE COUNT
        self.mOneHouseRent = mOneHouseRent
        self.mTwoHouseRent = mTwoHouseRent
        self.mThreeHouseRent = mThreeHouseRent
        self.mFourHouseRent = mFourHouseRent
        self.mFiveHouseRent = mFiveHouseRent #hotel
    
    
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
    
    def BuildHouse(self):
        mCanBuild = False
        if None:
        # if CheckMonopoly():
            if (self.mNumHouse < 5):
        # Treat fifth house as hotel
    
    # TODO: complete function
    # def CheckMonopoly() -> bool:
        # Brainstorm
        # use the mOwner variable and the constructed dictionary
        # Have list of lists with each set as a sub list and then check this
        # list against the deed owned list of player with a counter to compare
        # against the length of the sublist to check if a monopoly or not
        # instead of a list of lists use a dictionary to store each set