from tile import Tile
from player import Player
import board as board

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
        # from board import inputValidation
        # import board
        if mPlayer.mIsAi: # AI, so make decisions for the player
            if self.mOwner is None: # if the deed is unowned
                if mPlayer.mBalance >= self.mCost: # if AI has enough money
                    self.purchase(mPlayer)
            elif self.mOwner == mPlayer: # deed is owned by yourself
                print("Nothing happens!")
            else: # deed is owned by another player
                self.pay(mPlayer, rollSum)
        else: # user, so user should make decisions
            if self.mOwner == mPlayer: # deed is owned by yourself
                print("This is your own property!")
            elif self.mOwner is None:
                if (True): #check if can buy:
                    choice = ""
                    choice = board.inputValidation(choice, ["yes", "no"], "Would you like to purchase the property? (yes/no) ")
                    if choice == "yes":
                        self.purchase(mPlayer)
                else:
                    # you cannot buy
                    print("NO BUY")
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
        from board import SetToDeedMap

        # print("I am here")
        count = 0
        for property in SetToDeedMap[self.mSet]:
            if player == property.mOwner:
                count += 1
        # print("This is count deed owned", count)
        return count
    
    def CalculateRent(self, rollSum, player: Player = None) -> int:
        pass