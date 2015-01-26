import string
from nltk.corpus import wordnet
import re
from random import randint
from time import time

class Caeser_Cypher(object):
    '''A Caeser Cypher decoder as well as cracker.'''
    
    def __init__(self, key=None, message = None):
        
        self.key = key
        self.message = message
           
    def decode_cypher(self):
        '''decode a instances file, when the instances key has a value'''

        if self.key == None:
            return 'You must crack the cypher first.'
        
        alphabet = string.ascii_lowercase        
        with open (self.message, "r") as myfile:
            data=myfile.read().replace('\n', '')
        unencrypted = ''
        for letter in data.lower():            
            if letter != '.' and letter != ' ':
                if alphabet.index(letter) - self.key + 1 < 0:
                    val = alphabet[alphabet.index(letter) - self.key + 26]
                else:                    
                    val = alphabet[alphabet.index(letter) - self.key]
                unencrypted+=val
            else:
                unencrypted+=letter
        return unencrypted
                
          
    def crack_cypher(self):        
        '''crack a caeser cypher for the instances text file, when the key is unkown,
        will also handle if there are different keys for each line of text'''
        
        with open (self.message, "r") as myfile:
            data= myfile.read()
        unclean_data = re.sub('[.!@#$?]', '', data).split('\n')

        decoded_text = ''
        for line in unclean_data:            
            data = [x for x in line.split() if len(x) > 1]            
            sample_size = 3                
            if len(data) < 3:
                sample_size = len(data)
            
            is_same = False            
            while is_same == False:
                sample_words = [data[randint(0, len(data)-1)] for i in range(sample_size)]                
                test_consistent_values = Caeser_Cypher.crack_cypher_match_keys(sample_words)
                is_same = all(x==test_consistent_values[0] for x in test_consistent_values)            
            decoded_text+=Caeser_Cypher.decode_line(line, test_consistent_values[0]) + '. '
        return decoded_text
            
        
    @staticmethod
    def decode_line(data, key):
        '''Decode's a string of text when the key is known.'''
        
        alphabet = string.ascii_lowercase
        unencrypted = ''
        for letter in data.lower():            
            if letter != '.' and letter != ' ':
                if alphabet.index(letter) - key + 1 < 0:
                    val = alphabet[alphabet.index(letter) - key + 26]
                else:                    
                    val = alphabet[alphabet.index(letter) - key]
                unencrypted+=val
            else:
                unencrypted+=letter
        return unencrypted
        

    @staticmethod
    def crack_cypher_match_keys(sample_words):
        '''Finds the keys for a list of words. Will not return key for a single letter word.
        make sure to test several words, 2 and 3 letter words will return false positives sometimes
        so it is better to use the crack cypher method in most cases.'''

        sample_words = [x.replace('.','') for x in sample_words if len(x) > 1]        
        sample_words_cracked = []        
        for word in sample_words:
            key = 0
            is_word = False
            starting = time()
            key_list = []
            while is_word == False:
                if not wordnet.synsets(Caeser_Cypher.test_crack(word, key)):
                    key_list.append(key)
                    key+=1
                    if time() - starting > 20:                        
                        break                    
                else:                    
                    is_word = True                    
                    sample_words_cracked.append(key)
                                        
        return sample_words_cracked
                
    @staticmethod
    def test_crack(word, key):
        '''Returns a decoded word when the key is known.'''
        
        alphabet = string.ascii_lowercase     
        unencrypted = ''
        for letter in word.lower():            
            if alphabet.index(letter) - key + 1 < 0:
                try:                    
                    val = alphabet[alphabet.index(letter) - key + 26]
                    unencrypted+=val
                except IndexError:
                    continue
            else:                    
                val = alphabet[alphabet.index(letter) - key]
                unencrypted+=val
        return unencrypted
                           
           
        

        
        
    
