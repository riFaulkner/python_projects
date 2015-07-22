'''
Created on Jul 21, 2015

@author: Rick
'''
class Ship(object):
    postion = []
    
    def __init__(self, name, position, lives):
        self.name = name
        self.livesLeft = lives
        self.position = position.parse(",")
        self.initialLives = lives
    
    def hit(self):
        self.livesLeft -= 1
        
        if self.livesLeft == 0:
            return "You've sunk my %s" % (self.name)
        else:
            return "Thats a hit!!"
        
    def lives(self):
        return self.livesLeft