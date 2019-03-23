'''
Created on Jan 31, 2018

@author: catad
'''
from controller import * 

class CSVRepo:
    def __init__(self, filename):
        self._filename = filename
        self._sentences = []
        self.loadFromFile()
        
        
    def store(self, sentence):
        words = sentence.split()
        self._sentences.append(words)
        self.writeToFile()
        
    def getAll(self):
        return self._sentences
    
    def loadFromFile(self):
        
        file = open(self._filename, 'r')
        
        for line in file:
            
            attributes = line.split()
            
            if len(attributes) < 1:
                continue
            
            #words = len(attributes)
            self._sentences.append(attributes)
            
        file.close()
        
    def writeToFile(self):
        
        file = open(self._filename, 'w')
        
        for s in self._sentences:
            words = len(s)
            for i in range(0, words):
                file.write(str(s[i])+" ")
            file.write("\n")
            
            
'''
repo = CSVRepo('goodsentences.csv')
 
for s in repo.getAll():
    print(s)
    
sentence = str(input("Enter a sentence: "))
repo.store(sentence)

for s in repo.getAll():
    print(s)
'''  