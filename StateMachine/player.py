class Player:
    def __init__(self, mIsAi: bool):
        # PLAYER INFO
        self.mPos = 0
        self.mIsAi = mIsAi
        self.mPlayerName = ""

        # MONEY INFO
        self.mBalance = 0  #TODO: decide starting balance 
        self.mNetWorth = self.mBalance

        # PROPERTY INFO
        self.mDeedOwned = []
        self.mHouseOwned = 0
        self.mHotelOwned = 0

        # JAIL INFO
        self.mInJail = False
        self.mNumJailFree = 0
        self.mContinuousDoubles = 0

    def CalculateNetWorth(self):
        self.mNetWorth = self.mBalance

        for deed in self.mDeedOwned:
            self.mNetWorth += deed.mCost
            if deed.mHouseCount != 0:
                self.mNetWorth += (deed.mHouseCount * deed.mHouseCost)

    def NamePlayer(self):
        if not self.mIsAi:
            self.mPlayerName = input("Enter Player Name: ")
        else :
            self.mPlayerName = "Bartholomew Banksworth"
