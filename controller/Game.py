'''
Created on Jan 31, 2018

@author: catad
'''

from csvRepo.CSVRepo import CSVRepo
from controller.Scontroller import Scontroller
from controller.Scontroller import Validator
import random

class Board:
    def __init__(self, sentence):
        self._sentence = sentence
        self._hangman = 'HANGMAN'
        self._turns = 0
        
    def setBoard(self):
        self._board = []
        words = len(self._sentence)
        for i in range(0, words):
            self._board.append([])
        i = 0
        for w in self._sentence:
            self._board[i].append(w[0])
            for l in range(1, len(w)-1):
                self._board[i].append(" __ ")
                
            self._board[i].append(w[-1])
            
            i += 1
            
        for i in range(0, words):
            a = self._board[i][0]
            b = self._board[i][-1]
            
            for l in range (0, words):
                word = self._sentence[l]
                wordList = list(word)
                if a in wordList:
                    
                    for c in range(1, len(wordList) - 1):
                        if a in wordList[c]:
                            self._board[l][c] = a 
                if b in wordList:
                    
                    for c in range(1,len(wordList) - 1):
                        if b in wordList[c]:
                            self._board[l][c] = b 
                            
                            
        return self._board
    

class Play:
    def __init__(self, board, sentence, turns):
        self._board = board
        self._sentence = sentence
        self._turns = turns
        self._missedL = []
        self._hangman = 'HANGMAN'
    def checkWin(self):
        for c in self._board:
            if ' __ ' in c:
                return False
            
        return True
    
    def checkLoss(self):
        if self.checkWin() == False and self._turns == 7:
            return True
        
        return False
    
    def guess(self, letter):
        ok = False
        if letter not in self._missedL:
            for w in range(0, len(self._board)):
                for l in range (0, len(self._board)):
                    word = self._sentence[l]
                    wordList = list(word)
                    if letter in wordList:
                        
                        for c in range(1, len(wordList) - 1):
                            if letter in wordList[c]:
                                self._board[l][c] = letter
                                ok = True
                                
            if ok == True:
                
                z = ""
                for w in self._board:
                    for char in w:
                        z += char
                    z += " "
                    
                return z
        else:
            return False
        if ok == False:
            self._missedL.append(letter)
            self._turns += 1
            hang = self._hangman[0:self._turns]
            return hang
            
            
            
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
'''    
repo = CSVRepo('goodsentences.csv')
validator = Validator()
sentences = Scontroller(repo, validator)

index = random.randint(0, len(repo.getAll()) - 1)
sentence = repo.getAll()[index]

board = Board(sentence)
setB = board.setBoard()
for b in setB:
    print(b)
    
game = Play(setB, sentence, 0)
letter = str(input("Enter letter: "))
g = game.guess(letter)
if g is False:
    letter = str(input("Enter a new letter: "))
    g = game.guess(letter)
else:
    print(g)
'''   

                        
                