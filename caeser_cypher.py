import string

class Caeser_Cypher(object):

    def __init__(self, key, message):
        
        self.key = key
        self.message = message
        
    def decode_cypher(self):
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
