from tile import Tile
from player import Player
from abc import abstractmethod

# A DEED IS A TILE THAT CAN BE PURCHASED! 
class Deed(Tile):
    def __init__(self, mTileName, mCost, mSet, mRent):
        super().__init__(mTileName)
        self.mCost = mCost
        self.mSet = mSet
        self.mOwner = None
        # TODO: add rent calculate function
        self.mRent = mRent

    # WHAT HAPPENS WHEN A PLAYER LANDS ON A DEED?
    def action(self, mPlayer: Player, rollSum: int):
        if mPlayer.mIsAi: # AI, so make decisions for the player
            if self.mOwner == mPlayer: # deed is owned by yourself
                print("Nothing happens!")
            elif self.mOwner is not None:
                self.pay(mPlayer, rollSum)
        else: # user, so user should make decisions
            if self.mOwner is None:
                choice = input("Would you like to purchase the property? (yes/no) ")
                if choice == "yes":
                    self.purchase(mPlayer)
            elif self.mOwner == mPlayer: # deed is owned by yourself
                print("This is your own property!")
            else: # deed is owned by another player
                self.pay(mPlayer, rollSum)
                    

    def purchase(self, mPlayer: Player):
        self.mOwner = mPlayer
        mPlayer.mBalance -= self.mCost
        self.mOwner.mDeedOwned.append(self)
        print(mPlayer.mPlayerName + " purchased " + self.mTileName + " for $" + str(self.mCost) + "!")

    # update pay function with rent calc functions
    def pay(self, mPlayer: Player, rollSum: int):
        mRentToPay = self.CalculateRent(rollSum, self.mOwner)
        # print("This is mRentToPay", mRentToPay, "This playerBalance", mPlayer.mBalance)
        mPlayer.mBalance -= mRentToPay
        self.mOwner.mBalance += mRentToPay
        print(mPlayer.mPlayerName + " paid " + self.mOwner.mPlayerName + " $" + str(mRentToPay) + "!")

    # find number of deeds owned from a set
    # to check for monopoly use
    # if (len(SetToDeedMap[self.mSet]) == CountDeedOwned(self, player)) then is a monopoly
    def CountDeedOwned(self, player: Player) -> int:
        # fix circular import
        from constants import property_stuff, const

        # print("I am here")
        count = 0
        for property in property_stuff.SetToDeedMap[self.mSet]:
            if player == property.mOwner:
                count += 1
        # print("This is count deed owned", count)
        return count
    
    @abstractmethod
    def CalculateRent(self, rollSum, player: Player) -> int:
        pass
    
    def reset(self):
        self.mOwner = None