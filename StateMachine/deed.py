from tile import Tile
from player import Player

class Deed(Tile):
    def __init__(self, mTileName, mCost, mSet):
        super().__init__(self, mTileName)
        self.mCost = mCost
        self.mSet = mSet
        self.mOwner = None

    def action(self, mPlayer: Player):
        if mPlayer.mIsAi: # AI, so make decisions for the player
            if self.mOwner is None: # if the deed is unowned
                if mPlayer.mBalance >= self.mCost: # if AI has enough money
                    self.purchase(mPlayer)
            elif self.mOwner == mPlayer: # deed is owned by yourself
                print("Nothing happens!")
            else: # deed is owned by another player
                self.pay(mPlayer)
        else: # user, so user should make decisions
            if self.mOwner is None:
                choice = input("Would you like to purchase the property? (yes/no)")
                if choice is "yes":
                    self.purchase(mPlayer)
            elif self.mOwner == mPlayer: # deed is owned by yourself
                print("This is your own property!")
            else: # deed is owned by another player
                self.pay(mPlayer)
                    

    def purchase(self, mPlayer: Player):
        self.mOwner = mPlayer
        mPlayer.mBalance -= self.mCost

    def pay(self, mPlayer: Player):
        # base implementation (default rent without accounting for monopolies or upgrades or railroad/utility rules)
        mPlayer.mBalance -= self.mCost
        self.mOwner.mBalance += self.mCost
        print(mPlayer.mPlayerName + " paid " + self.mOwner.mPlayerName + " $" + self.mCost + "!")
