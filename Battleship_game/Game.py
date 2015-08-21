'''
Created on Jul 21, 2015

@author: Rick
'''
from Player import Player


if __name__ == '__main__':
    players = 0
    print ("Welcome to Battleship!")
   # while True:
    #    players =int(raw_input("How many players are there?"))
     #   if(players == 1 or players == 2):
      #      print "%i? Alright!" % (players)
       #     break
    player1 = Player(raw_input("Enter your name"))
    player2 = Player("Computer", True)
    
    def game_loop():
        while(True):
            player1.turn(attempts_board)
        
        