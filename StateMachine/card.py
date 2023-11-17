from player import Player
import const
class Card:
    def __init__(self, inputType):
        self.mFixedPosition = -1
        self.mDeltaPosition = 0
        self.mDeltaBalance = 0
        self.mSpecial = ""
        inputType = 2
        if inputType == 0:
            self.mName = "Advance to Boardwalk"
            self.mFixedPosition = 39
        elif inputType == 1:
            self.mName = "Advance to Illinois Avenue. If you pass Go, collect $200"
            self.mFixedPosition = 24
        elif inputType == 2:
            self.mName = "Advance to St. Charles Place. If you pass Go, collect $200"
            self.mFixedPosition = 11
        elif inputType == 3: # NEED TWO OF THESE IN CHANCE
            self.mName = "Advance to the nearest Railroad. If unowned, you may buy it from the Bank. If owned, pay owner twice the rental to which they are otherwise entitled" # SPECIAL
            self.mSpecial = "NextRailroad"
        elif inputType == 4:
            self.mName = "Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times amount thrown." # SPECIAL
            self.mSpecial = "NextUtility"
        elif inputType == 5:
            self.mName = "Bank pays you dividend of $50"
            self.mDeltaBalance += 50
        elif inputType == 6:
            self.mName = "Go Back 3 Spaces"
            self.mDeltaPosition -= 3
        elif inputType == 7:
            self.mName = "Make general repairs on all your property. For each house pay $25. For each hotel pay $100" # SPECIAL
            self.mSpecial = "25 and 100"
        elif inputType == 8:
            self.mName = "Speeding fine $15"
            self.mDeltaBalance -= 15
        elif inputType == 9:
            self.mName = "Take a trip to Reading Railroad. If you pass Go, collect $200"
            self.mFixedPosition = 5
        elif inputType == 10:
            self.mName = "You have been elected Chairman of the Board. Pay each player $50" # SPECIAL
            self.mSpecial = "Chairman"
        elif inputType == 11:
            self.mName = "Your building loan matures. Collect $150"
            self.mDeltaBalance += 150
        # CHANCE EXCLUSIVE CARDS END
        # CHANCE & COMMUNITY CHANCE CARDS BEGIN
        elif inputType == 12:
            self.mName = "Advance to Go (Collect $200)"
            self.mFixedPosition = 0
        elif inputType == 13:
            self.mName = "Get Out of Jail Free" # SPECIAL
            self.mSpecial = "GetOut"
        elif inputType == 14:
            self.mName = "Go to Jail. Go directly to Jail, do not pass Go, do not collect $200" # SPECIAL
            self.mSpecial = "Jail"
        # CHANCE & COMMUNITY CHANCE CARDS END
        # COMMUNITY CHEST EXCLUSIVE CARDS BEGIN
        elif inputType == 15:
            self.mName = "Bank error in your favor. Collect $200"
            self.mDeltaBalance += 200
        elif inputType == 16:
            self.mName = "Doctor's fee. Pay $50"
            self.mDeltaBalance -= 50
        elif inputType == 17:
            self.mName = "From sale of stock you get $50"
            self.mDeltaBalance += 50
        elif inputType == 18:
            self.mName = "Holiday fund matures. Receive $100"
            self.mDeltaBalance += 100
        elif inputType == 19:
            self.mName = "Income tax refund. Collect $20"
            self.mDeltaBalance += 20
        elif inputType == 20:
            self.mName = "It is your birthday. Collect $10 from every player" # SPECIAL
            self.mSpecial = "Birthday"
        elif inputType == 21:
            self.mName = "Life insurance matures. Collect $100"
            self.mDeltaBalance += 100
        elif inputType == 22:
            self.mName = "Pay hospital fees of $100"
            self.mDeltaBalance -= 100
        elif inputType == 23:
            self.mName = "Pay school fees of $50"
            self.mDeltaBalance -= 50
        elif inputType == 24:
            self.mName = "Receive $25 consultancy fee"
            self.mDeltaBalance += 25
        elif inputType == 25:
            self.mName = "You are assessed for street repair. $40 per house. $115 per hotel" # SPECIAL
            self.mSpecial = "40 and 115"
        elif inputType == 26:
            self.mName = "You have won second prize in a beauty contest. Collect $10"
            self.mDeltaBalance += 10
        elif inputType == 27:
            self.mName = "You inherit $100"
            self.mDeltaBalance += 100
        else:
            print("INCORRECT inputType GIVEN TO CARD, should be 0-27")
        
    def action(self, player : Player, playerList):
        from board import Tiles
        print(self.mName + ".")
        oldPos = player.mPos
        if self.mFixedPosition != -1: player.mPos = self.mFixedPosition
        player.mPos += self.mDeltaPosition
        player.mBalance += self.mDeltaBalance
        if self.mSpecial == "NextRailroad":
            if player.mPos >= 5 and player.mPos < 15:
                self.mFixedPosition = 15
            elif player.mPos >= 15 and player.mPos < 25:
                self.mFixedPosition = 25
            elif player.mPos >= 25 and player.mPos < 35:
                self.mFixedPosition = 35
            else:
                self.mFixedPosition = 5
            player.mPos = self.mFixedPosition
        elif self.mSpecial == "NextUtility":
            if player.mPos >= 12 and player.mPos < 28:
                self.mFixedPosition = 28
            else:
                self.mFixedPosition = 12
            player.mPos = self.mFixedPosition
        elif self.mSpecial == "25 and 100":
            cost = player.mHotelOwned * 100 + player.mHouseOwned * 25
            player.mBalance -= cost
            print(player.mPlayerName + " had to pay $" + str(cost) + " to the bank.")
        elif self.mSpecial == "Chairman":
            for currPlayer in playerList:
                if currPlayer is not player:
                    player.mBalance -= 50
                    currPlayer.mBalance += 50
        elif self.mSpecial == "GetOut":
            player.mNumJailFree = player.mNumJailFree + 1
            # ADD A COUNTER OVER HERE TO KEEP TRACK OF CARD COUNT
        elif self.mSpecial == "Jail":
            player.GoToJail()
            return
        elif self.mSpecial == "Birthday":
            for currPlayer in playerList:
                if currPlayer is not player:
                    player.mBalance += 10
                    currPlayer.mBalance -= 10
        elif self.mSpecial == "40 and 115":
            cost = player.mHotelOwned * 115 + player.mHouseOwned * 40
            player.mBalance -= cost
            print(player.mPlayerName + " had to pay $" + str(cost) + " to the bank.")
        if self.mSpecial != "Jail" and (self.mFixedPosition != -1 or self.mDeltaPosition != 0):
            if player.mPos <= oldPos and self.mName != "Go Back 3 Spaces" and self.mName != "Advance to Go (Collect $200)": # passed go check
                player.mBalance += const.GO_MONEY
                print(player.mPlayerName + " passed go and earned $200!")
            tile = Tiles[player.mPos]

            if self.mSpecial == "NextRailroad" or self.mSpecial == "NextUtility":
                tile.card = True
            # physically move player to tile
            # if self.mDeltaPosition != 0:
                # player.MotorRequest(self.mDeltaPosition)
            # else:
                # player.MotorRequest((player.mPos-oldPos)%40)
            print(player.mPlayerName + " landed on " + tile.mTileName + "!")
            tile.action(player, (player.mPos-oldPos)%40)