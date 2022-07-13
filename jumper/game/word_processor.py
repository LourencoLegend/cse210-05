
import random

class Word_Processor:
    """
    initializes the class
    """
    def __init__(self) -> None:
        self.word_choice = ''
        self.hidden_word = ''
        self.temp_word = ''
        
    """
    Fetches the word from document
    """
    def get_word(self):
        words = []
        with open('cse210-tc05/jumper/game/word_list.txt','r') as w:
            words = w.readlines()
        self.word_choice = words[random.randint(0,999)]
        self.word_choice = self.word_choice[:-1]
        self.temp_word = self.word_choice
        


    """
    Cross references if the user input is in the word_choice
    Assigns a self.hidden_word to a new hidden word based on correct guess
    Args: input = one letter string from user
    Returns a boolean: True for correct guess, False for incorrect
    """
    def check_input(self, letter):
        replace_dash = True
        correct_guess = False
        if letter in self.temp_word:
            while replace_dash:
                index = self.temp_word.find(letter)
                if index != -1:
                    self.hidden_word = self.hidden_word[:index] + letter + self.hidden_word[index + 1:]
                    self.temp_word = self.temp_word[:index] + "-" + self.temp_word[index + 1:]
                else:
                    replace_dash = False
            correct_guess = True
        return correct_guess


    """
    Checks to see if word_choice is guessed 
    Returns Boolean: True for a win, False for a continue
    """
    def check_complete(self):
        word_complete = False
        if self.word_choice == self.hidden_word:
            word_complete = True
        return word_complete

        
    """
    Creates and returns a hidden word from the word choice.
    Hidden word will be a string of "-" with the length of the word choice.
    NOTE: ONLY WILL CREATE HIDDEN WORD. IF USED TO UPDATE THIS WILL NULLIFY GUESSES
    input: word = the word choice
    """
    def set_hidden_word(self, word):    
        hidden_word = ""

        for i in range(len(word)):
            hidden_word += "-"
        self.hidden_word = hidden_word


