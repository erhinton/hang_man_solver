import string

class solver:
    """ class that provides every possible hangman solution given a .txt file of words
    
    Attributes:
        path (string): a string that contains the path to a txt containing all english words
        letter_count (dictionary): a dictionary that contains the number of a 
            particular letter present in a given word
        all_words (set): a set that contains all words in the chosen text file
        valid_words (set): a set containing every word that could be the answer 
            to the hangman problem
        word_length (int): the number from 1 - 16 that is the length of the 
            executioner's word
        guesses (list): list of letters that were determined to be correct
        chosen_letter (string): string that is the letter recommended to be guessed
        best_guess (string): string that contains correct letters and '*' as a blank space
        
    """
    def __init__(self, path, word_length):
        self.letter_count = dict.fromkeys(string.ascii_lowercase, 0)
        self.all_words = set()
        self.valid_words = set()
        self.word_length = word_length
        self.guesses = []
        self.chosen_letter = ""
        with open(path,'r',encoding='utf-8') as f:
            for item in f:
                item = item.strip()
                self.all_words.add(item.lower())
                
        self.best_guess = '*' * word_length # should be a star for each letter
        
    def word_length_check(self):
        """ Filters out all words that are not the same length as best_guess
        
        Side effect:
            All words that are the matching length are added to valid_words
        """
        
        for word in self.all_words:
            if len(word) == len(self.best_guess):
                self.valid_words.add(word)
        
    def letter_picker(self):
        """ Finds the most common letter among words that are the right length
        
        Side effects:
            Prints out the number of valid words remaining, and the letter that 
                is most frequent 
            Append the chosen letter to guesses so that script will not guess
                the same letter multiple times
            
        """
        
        self.letter_count = dict.fromkeys(string.ascii_lowercase, 0) # reset
        for word in self.valid_words:
            word = "".join(set(word)) # removes duplicate letters in valid words
            for letter in word:
                self.letter_count[letter] += 1
        for letter in self.guesses: # prevents repeating guesses
            self.letter_count[letter] = 0
        self.chosen_letter = max(self.letter_count, key=self.letter_count.get)
        self.guesses.append(self.chosen_letter)
        print(f"{self.chosen_letter} is the letter I think is right")
        
    def results_of_guess(self):
        """ Removes words from valid_words based on whether or not the guess was
            correct
        
        Side effects:
            If guess is successful, removes all words that do not have the
                guessed letter at that exact index
            If not successful, removes all words that have the guessed letter
                in them
        """
        print(self.best_guess)
        print(self.chosen_letter)
        
        #self.best_guess = input("Enter word with correct letters and stars " + "as blank spaces.")
        wrong_words = set()
        if self.chosen_letter in self.best_guess: # in case of success
            print("hit")
            list_of_indices = [i for i, value in enumerate(self.best_guess) 
                if value == self.chosen_letter]
            for word in self.valid_words:
                for index in list_of_indices:
                    if word[index] != self.chosen_letter:
                        wrong_words.add(word)
                    elif word.count(self.chosen_letter) > len(list_of_indices):
                        wrong_words.add(word)
            
        else: # in case of failure
            print("miss")
            for word in self.valid_words:
                if self.chosen_letter in word:
                    wrong_words.add(word)
        self.valid_words = self.valid_words.difference(wrong_words)
        

def main(path, word_length):
    """Creates instace of solver object and runs it while there are remaining blank spaces"""
    game = solver(path, word_length)
    game.word_length_check()
    return game