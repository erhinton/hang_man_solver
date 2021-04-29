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
        textbox = Text(root, width=23)
        textbox.place(x=15,y=0)
        
        # attach textbox to scrollbar
        textbox.config(yscrollcommand=scrollbar.set, state=DISABLED)
        scrollbar.config(command=textbox.yview)
        
        # add words into text box
        game = main(self.path, int(self.word_length))
        textbox.configure(state="normal")
        for word in game.valid_words:
            textbox.insert(END, f"{word}\n")
        textbox.configure(state="disable")
        
        # build entry boxes that allow for character entry (correctly identified letters)
        entry_boxes = dict()
        x_value_margin = 0
        for space in range(self.word_length):
            entry_boxes[space] = Entry(root, width=2)
            entry_boxes[space].place(x=300 + x_value_margin, y=50)
            x_value_margin += 18
        
        # build button that shows submits entry boxes
        def on_next(entry_boxes):
            complete_word = ""
            for box in entry_boxes:
                letter = entry_boxes[box].get()
                if letter == "":
                    letter = "*"
                complete_word = complete_word + letter
                print(complete_word)
            
        
        next_button = Button(root, text='Next Guess',  command= lambda: on_next(entry_boxes))
        next_button.pack()
        
        
        
        
        root.mainloop()



        
        
        
def build_ui(path):
    first_window = WordLengthDropDown(path)
    first_window.construct()
    
if __name__ == "__main__":
    build_ui("scrabble_words.txt")