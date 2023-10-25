from deed import Deed
from player import Player
from const import AVAILABLE_HOUSE, AVAILABLE_HOTEL

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
        self.mFiveHouseRent = mFiveHouseRent  # hotel

    def CalculatePropertyRent(self, player: Player = None) -> int:
        from board import SetToDeedMap
        if self.mNumHouse == 0:
            return self.mRent
        elif len(SetToDeedMap[self.mSet]) == self.CountDeedOwned(self, player):
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
        
    def BuildHouse(self, player: Player = None) -> bool:
        from board import SetToDeedMap        
        mCanBuild = False
        if AVAILABLE_HOUSE != 0 and len(SetToDeedMap[self.mSet]) == self.CountDeedOwned(self, player) and self.mSet != "railroad" and self.mSet != "utility":
            if self.mNumHouse < 4 or (self.mNumHouse < 5 and AVAILABLE_HOTEL != 0):
                for property in SetToDeedMap[self.mSet]:
                    if self != property and (self.mNumHouse - property.mNumHouse == 0 or self.mNumHouse - property.mNumHouse == -1):
                        mCanBuild = True
        return mCanBuild
