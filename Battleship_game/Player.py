'''
Created on Jul 21, 2015

@author: Rick
'''

class Player(object):
    
    def __init__(self, playerName):
        self.playerName = playerName
        self.wins = 0
        self.shipsLeft = 5
        
    def newGame(self):
        self.shipsLeft = 5