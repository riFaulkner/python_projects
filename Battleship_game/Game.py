'''
Created on Jul 21, 2015

@author: Rick
'''


if __name__ == '__main__':
    players = 0
    print "Welcome to Battleship!"
    while True:
        players =int(raw_input("How many players are there?"))
        if(players == 1 or players == 2):
            print "%i? Alright!" % (players)
            break