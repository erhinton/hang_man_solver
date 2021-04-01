from tkinter import * # change this to only import stuff you need
from hang_man_solver import *

class WordLengthDropDown:
    def __init__(self,path):
        self.path = path
    
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
        def on_submit(submission):
            if submission:
                main(self.path, int(submission))
        submit_button = Button(root, text='Submit',  command= lambda: on_submit(tkvar.get()))
        submit_button.pack()
        
        root.mainloop()
        
        
def build_ui(path):
    first_window = WordLengthDropDown(path)
    first_window.construct()

if __name__ == "__main__":
    build_ui("scrabble_words.txt")