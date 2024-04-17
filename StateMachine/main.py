from board import Board 
from colorama import Fore, Back, Style
import os

def main(): 
    os.system('clear')
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