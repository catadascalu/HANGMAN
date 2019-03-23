'''
Created on Jan 31, 2018

@author: catad
'''
from controller.Scontroller import Scontroller
from controller.Scontroller import Validator
from csvRepo.CSVRepo import CSVRepo
from controller.Game import Board
from controller.Game import Play
import random



class UIHelper:
    def __init__(self, board, game, repo, sentence):
        self._board = board
        self._game = game
        self._repo = repo
        self._sentence = sentence
    def add(self):
        
            
        sentence = str(input("Enter sentence: "))
        self._sentence.store(sentence)
                
    def play(self):
        z = ""
        for w in self._board:
            for char in w:
                z += char
            z += " "
            
        print(z)
        while self._game.checkWin() == False and self._game.checkLoss() == False:
            letter = str(input("Enter letter: "))
            g = self._game.guess(letter)
            while g == False:
                letter = str(input("Enter letter: "))
                g = self._game.guess(letter)
                
            print(g)
                    
        if self._game.checkWin() == True:
            print("You Won ! :)")
        
        if self._game.checkLoss() == True:
            print("You lose :( .")    
                
                    
            
                
class UI:
    def __init__(self, board, game, repo, helper):
        self._board = board
        self._game = game
        self._repo = repo
        self._helper = helper
        
    def start(self):
        
        while True:
            option = str(input("Enter an option: "))
            if option == 'add sentence':
                self._helper.add()
                
            elif option == 'play':
                self._helper.play()
                
            elif option == 'play again':
                index = random.randint(0, len(repo.getAll()) - 1)
                sentence = self._repo.getAll()[index]
                board = Board(sentence)
                setBoard = board.setBoard() 
                game = Play(setBoard, sentence, 0)
                self._helper = UIHelper(setBoard, game, self._repo, sentence)
                self._helper.play()
                
            elif option == 'exit':
                break
            
            else:
                print("Invalid option. Enter add sentence/play/play again/exit.")
                
            
                
        
        
        
validator = Validator()
repo = CSVRepo('goodsentences.csv')
control = Scontroller(repo, validator)
index = random.randint(0, len(repo.getAll()) - 1)
sentence = repo.getAll()[index]
board = Board(sentence)
setBoard = board.setBoard() 
game = Play(setBoard, sentence, 0)
helper = UIHelper(setBoard, game, repo, control)
hangman = UI(setBoard, game, repo, helper) 
hangman.start()
                        
                    
                    
            