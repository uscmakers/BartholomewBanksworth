from BartholomewBanksworth.StateMachine.tile import Tile
from BartholomewBanksworth.StateMachine.player import Player

class Deed(Tile):
    def __init__(self, mCost, mSet):
        self.mCost = mCost
        self.mSet = mSet
        self.mOwner = None

    def action(self, name, mPlayer: Player):
        if mPlayer.mAI: # AI, so make decisions for the player
            if mPlayer.mBalance >= self.mCost:
                if self.mOwner is None: # if the deed is unowned
                    self.purchase(self, mPlayer)
                else: # deed is owned
                    self.pay(self, mPlayer)
        else: # user, so user should make decisions
            if self.mOwner is None:
                choice = input("Would you like to purchase the property? (yes/no)")
                if choice is "yes":
                    self.purchase(self, mPlayer)
            else: # deed is owned
                print(mPlayer.mPlayerName + "landed on" + super().mTileName)
                print(self.mCost + "has been paid from" + mPlayer.mPlayerName + "to" + self.mOwner)
                mPlayer.mBalance -= self.mCost
                self.mOwner.mBalance += self.mCost
                    

    def purchase(self, mPlayer: Player):
        self.mOwner = mPlayer
        mPlayer.mBalance -= self.mCost

    def pay(self, mPlayer: Player):
        pass
