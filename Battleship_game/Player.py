'''
Created on Jul 21, 2015

@author: Rick
'''
#import random

class Player(object):
    
    def __init__(self, playerName, ai=False):
        self.playerName = playerName
        self.wins = 0
        self.shipsLeft = 5
        self.ai = ai #boolean
            
    def __str__(self, *args, **kwargs):
        return "I am %s \nI have won %s games \nI have %s ships left \nAI status = %s" % (self.playerName, self.wins, self.shipsLeft, self.ai )
    
    def initilize_boards(self):
        self.guess_board = []
        self.my_board = []
        
        i = 1
        while(i<10):
            self.guess_board.append(["O"]*10)
            self.my_board.append(["O"]*10)
            i +=1
    
    def place_pieces(self, board):
        """TODO: Ask user where to place there pieces"""
        
    def newGame(self, last_game_win):
        self.shipsLeft = {5: "Carrier", 4: "Battleship", 3: "Destroyer", 2: "Submarine", 1: "Patrol Boat"}
        if(last_game_win):
            self.wins += 1
        self.initilize_boards()
        self.place_pieces(self.my_board, self.shipsLeft)
        
    def turn(self, attempts_board):
        if not(self.ai):
            while True:
                #attack_space = raw_input("Enter the space you would like to attack:")
                #x, y = attack_space.split(",")
                x,y = raw_input("Enter the space you would like to attack:").split(",")
                
                if (self.guess_fits(x) and self.guess_fits(y)):
                    if (attempts_board(x)(y) == 'O'):
                        return x + "," + y
        
        else:
            return self.ai_attack_space_choose()
            
    def ai_attack_space_choose(self):
        """TODO:"""
        
        return ""
      
    def guess_fits(self, guess):
        valid_range = 'abcdefghij'
        if (guess in range(0,10) or str(guess) in valid_range):
            return True
        return False
        #return (1 < guess <= 10)
    
    def print_board(self, board):
        current_row = 1
        for row in board:
            print current_row, " ".join(row)
            current_row +=1
        print "  A B C D E F G H I J"
    
    def print_guess_board(self):
        print "     Guess Board"
        self.print_board(self.guess_board)
        
    def print_my_board(self):
        print "     My Board"
        self.print_board(self.my_board)

rick = Player("Rick")
rick.newGame(False)

print rick.print_guess_board()
print rick.print_my_board()
print rick.guess_fits('a')
print rick.guess_fits('k')
print rick.guess_fits(1)
