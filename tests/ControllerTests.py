'''
Created on Jan 31, 2018

@author: catad
'''


from unittest import TestCase
from controller.Scontroller import Scontroller
from controller.Scontroller import Validator
from csvRepo.CSVRepo import CSVRepo
from controller.Game import Board
from controller.Game import Play


class SControllerTest(TestCase):
    
    def test_store(self):
        s = CSVRepo('test.csv')
        validator = Validator()
        control = Scontroller(s, validator)
        sentence = "Ana has apples"
        control.store(sentence)
        self.assertEqual(len(s.getAll()), 1, "Can't store.")
        
        sentence = "john is nice"
        control.store(sentence)
        self.assertRaises(Exception)
        
        sentence = ""
        control.store(sentence)
        self.assertRaises(Exception)
        
        
    
        
    def test_board(self):
        
        sentence = [['a', 'n', 'a'], ['h', 'a', 's'], ['a', 'p', 'p', 'l', 'e', 's']]
        b = Board(sentence)
        setBoard = b.setBoard()
        self.assertEqual(setBoard, [['a', ' __ ', 'a'], ['h', 'a', 's'], ['a', ' __ ', ' __ ', ' __ ', ' __ ', 's']], "Not set correctly.")
        
        
        
    def test_checkWin(self):
        sentence = [['a', 'n', 'a'], ['h', 'a', 's'], ['a', 'p', 'p', 'l', 'e', 's']]
        b = Board(sentence)
        setBoard = b.setBoard()
        play = Play(setBoard, sentence, 0)
        self.assertFalse(play.checkWin(), "Not okay.")
        
        play = Play(sentence, sentence, 0)
        self.assertTrue(play.checkWin(), "Not okay.")
        
        
    def test_checkLoss(self):
        sentence = [['a', 'n', 'a'], ['h', 'a', 's'], ['a', 'p', 'p', 'l', 'e', 's']]
        b = Board(sentence)
        setBoard = b.setBoard()
        play = Play(setBoard, sentence, 7)
        self.assertTrue(play.checkLoss(), "Not okay.")
        
        play = Play(sentence, sentence, 7)
        self.assertFalse(play.checkLoss(), "Not okay.")
        
        play = Play(sentence, sentence, 4)
        self.assertFalse(play.checkLoss(), "Not okay.")
        
        play = Play(setBoard, sentence, 5)
        self.assertFalse(play.checkLoss(), "Not okay.")
        
        
    def test_guess(self):
        letter = 'n'
        sentence = [['a', 'n', 'a'], ['h', 'a', 's'], ['a', 'p', 'p', 'l', 'e', 's']]
        b = Board(sentence)
        setBoard = b.setBoard()
        play = Play(setBoard, sentence, 0)
        z = play.guess(letter)
        self.assertEqual(z, 'ana has a __  __  __  __ s ', "not okay")
        
        letter = 'z'
        z = play.guess(letter)
        self.assertEqual(z, 'H', "not okay")
        
        letter = 'z'
        z = play.guess(letter)
        self.assertEqual(z, False, "not okay")
        
        
        
        
        
            
    