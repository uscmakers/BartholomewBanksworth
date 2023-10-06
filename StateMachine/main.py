from board import Board 
def __main__(): 
    numPlayers = input("How many players want to try their hand against Bartholomew Banksworth? ")
    b = Board(numPlayers+1) # create instance of Monopoly game
    b.init()
    b.run()