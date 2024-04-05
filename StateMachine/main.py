from board import Board 

def main(): 
    numPlayers = int(input("How many players want to try their hand against Bartholomew Banksworth? "))
    b = Board(numPlayers+1) # create instance of Monopoly game
    b.init()
    b.run()

if __name__=="__main__": 
    main()

# TEST RPI STUFF
# HI