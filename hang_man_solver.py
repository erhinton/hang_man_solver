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
        correct_guesses (list): list of letters that were determined to be correct
        chosen_letter (string): string that is the letter recommended to be guessed
        best_guess (string): string that contains correct letters and '*' as a blank space
        
    """
    def __init__(self,path):
        self.letter_count = dict.fromkeys(string.ascii_lowercase, 0)
        self.all_words = set()
        self.valid_words = set()
        self.correct_guesses = []
        self.chosen_letter = ""
        with open(path,'r',encoding='utf-8') as f:
            for item in f:
                item = item.strip()
                self.all_words.add(item.lower())
                
        self.best_guess = input("Enter the word the executioner has chosen " + 
                                "with each blank as a star (*). \n")
        
    def word_length_check(self):
        for word in self.all_words:
            if len(word) == len(self.best_guess):
                self.valid_words.add(word)
        
    def letter_picker(self):
        self.letter_count = dict.fromkeys(string.ascii_lowercase, 0) # reset
        for word in self.valid_words:
            word = "".join(set(word)) # removes duplicate letters in valid words
            for letter in word:
                self.letter_count[letter] += 1
        for letter in self.correct_guesses: # prevents repeating guesses
            self.letter_count[letter] = 0
        self.chosen_letter = max(self.letter_count, key=self.letter_count.get)
        print(self.valid_words)
        print(f"There are {len(self.valid_words)} valid words remaining.")
        print(f"Try guessing {self.chosen_letter}")
        self.correct_guesses.append(self.chosen_letter)
        
        
    def results_of_guess(self):
        self.best_guess = input("Enter word with correct letters and stars " +
            "as blank spaces.")
        wrong_words = set()
        if self.chosen_letter in self.best_guess: # in case of success
            list_of_indices = [i for i, value in enumerate(self.best_guess) 
                if value == self.chosen_letter]
            for word in self.valid_words:
                for index in list_of_indices:
                    if word[index] != self.chosen_letter:
                        wrong_words.add(word)
                    elif word.count(self.chosen_letter) > len(list_of_indices):
                        wrong_words.add(word)
            
        else: # in case of failure
            for word in self.valid_words:
                if self.chosen_letter in word:
                    wrong_words.add(word)
        self.valid_words = self.valid_words.difference(wrong_words)
        

def main(path):
    x = solver(path)
    x.word_length_check()
    while "*" in x.best_guess:
        x.letter_picker()
        x.results_of_guess()
    
if __name__ == "__main__":
    main("scrabble_words.txt")