from tkinter import * # change this to only import stuff you need


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
def on_submit():
    submission = tkvar.get()
    if submission:
        print(submission)
    
submit_button = Button(root, text='Submit',  command=on_submit)
submit_button.pack()


root.mainloop()

# longest possible word is 16
