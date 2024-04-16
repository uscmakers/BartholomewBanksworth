from board import Board 
from colorama import Fore, Back, Style

def main(): 
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(Fore.GREEN + Style.BRIGHT + "-----------------------------------------------------------------")
    print("                      BARTHOLOMEW BANKSWORTH")
    print("-----------------------------------------------------------------\n")
    numPlayers = int(input("How many players want to try their hand against Bartholomew Banksworth? "))
    b = Board(numPlayers+1) # create instance of Monopoly game
    b.init()
    b.run()

if __name__=="__main__": 
    main()

# TEST RPI STUFF
# HI