from tkinter import * # change this to only import stuff you need
from hang_man_solver import *

class WordLengthDropDown:
    def __init__(self,path):
        self.path = path
        self.word_length = 0
        
    def construct(self):
        # set up window
        root = Tk()
        root.title("Choose Word Length")
        root.geometry('700x500')
        
        # Create Instructions label
        dropdown_label = Label(root,text="Select the number of letters in the executioner's word", justify=CENTER,padx=10)
        dropdown_label.config(font=("Courier", 10))
        dropdown_label.pack(side=TOP)
        
        # buliding length menu (proves options about what length word the exectioner has chosen) 
        tkvar = StringVar(root) 
        possible_lengths = range(1,17)
        length_menu = OptionMenu(root,  tkvar, *possible_lengths)
        length_menu.configure(background="white")
        length_menu.pack()
        
        # building submit button
        def on_submit(tkvar, root):
            submission = tkvar.get()
            if submission:
                root.destroy()
                self.word_length = int(submission)
                self.build_second_frame()
                
        submit_button = Button(root, text='Submit',  command= lambda: on_submit(tkvar,root))
        submit_button.pack()
        

        
        root.mainloop()
        
    def build_second_frame(self):
        root = Tk()
        root.title("Choose Word Length")
        root.geometry('700x500')
        scrollbar = Scrollbar(root)
        scrollbar.pack(side=LEFT, fill=Y)
        valid_words_textbox = Text(root, width=23)
        valid_words_textbox.place(x=15,y=0)
        
        # attach valid_words_textbox to scrollbar
        valid_words_textbox.config(yscrollcommand=scrollbar.set, state=DISABLED)
        scrollbar.config(command=valid_words_textbox.yview)
        
        # add instructions
        instructions = ("Instructions:To use the hangman solver, follow the letter recommendation of the ‘best guess’ textbox.\n"
        "\nIf the executioner confirms that the letter is present in their selected word, then insert that letter into the box corresponding to the position of the letter (for example if the letter ‘a’ is the third and fifth letter in a word type ‘a’ into the third and fifth boxes). After inserting the letter click next guess and repeat the process until the word is filled out.\n"
        "\nIf the execution states that the letter is not present in their selected word do not enter anything into the boxes and instead simply click next guess.\n")
        intruction_box = Text(root, height=15, width=55)
        intruction_box.place(x = 220, y = 210)
        intruction_box.insert(END,instructions)
        intruction_box.configure(state="disable")
        
        # create instance of solver class
        game = main(self.path, int(self.word_length))
        game.letter_picker()

        # add words into text box
        def update_valid_words_textbox (valid_words_textbox, game):
            valid_words_textbox.configure(state="normal")
            valid_words_textbox.delete('1.0',END)
            for word in game.valid_words:
                valid_words_textbox.insert(END, f"{word}\n")
            valid_words_textbox.configure(state="disable")
        update_valid_words_textbox (valid_words_textbox, game)
        
        # add dynamic text that changes based on what you should guess
        chosen_letter_label = Text(root, height=2, width=18)
        chosen_letter_label.place(x = 300, y = 130)
        chosen_letter_label.insert(END, f"Best guess is {game.chosen_letter}")
        chosen_letter_label.configure(state="disable")


        

        
        # build entry boxes that allow for character entry (correctly identified letters)
        entry_boxes = dict()
        x_value_margin = 0
        for space in range(self.word_length):
            entry_boxes[space] = Entry(root, width=2)
            entry_boxes[space].place(x=300 + x_value_margin, y=70)
            x_value_margin += 18
        
        # build button that shows submits entry boxes
        def on_next(entry_boxes, game):
            complete_word = ""
            for box in entry_boxes:
                letter = entry_boxes[box].get()
                letter = letter.lower()
                if letter == "":
                    letter = "*"
                complete_word = complete_word + letter
                
            if '*' in complete_word:
                game.best_guess = complete_word
                
                game.results_of_guess()
                update_valid_words_textbox(valid_words_textbox, game)
                
                game.letter_picker()
                
                chosen_letter_label.configure(state="normal")
                chosen_letter_label.delete('1.0',END)
                chosen_letter_label.insert(END, f"Best guess is {game.chosen_letter}")
                chosen_letter_label.configure(state="disable")

            else:
                # if the game is over
                chosen_letter_label.configure(state="normal")
                chosen_letter_label.delete('1.0',END)
                chosen_letter_label.insert(END, f"The final word is {complete_word}!")
                chosen_letter_label.configure(state="disable")

                

            
        
        next_button = Button(root, text='Next Guess',  command= lambda: on_next(entry_boxes,game))
        next_button.place(x = 300, y = 100)
        
        
        
        
        root.mainloop()



        
        
        
def build_ui(path):
    first_window = WordLengthDropDown(path)
    first_window.construct()
    
if __name__ == "__main__":
    build_ui("scrabble_words.txt")