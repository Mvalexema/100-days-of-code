from tkinter import *
#window = tkinter.Tk() - coul bereplaced with the code below,
window=Tk()
window.title("GUI Example Program")
window.minsize(width=500,height=300)


# Labels
my_label = Label(text="This is a Label", font=("Arial",20, "italic"))
my_label.config(text="My new window")
my_label.pack()


# Buttons

def button_clicked():
    print("Click the button")
    new_text=input.get()
    my_label.config(text=new_text)

# button=tkinter.Button() - alternative entry
button=Button(text="Click Me", command=button_clicked)
button.pack()

# Entries

entry = Entry(width=20)
# Adding some text
entry.insert(END, string="Text window")
print(entry.get())
entry.pack()

# Text
text = Text(height=5, width=30)

# Puts cursor in textbox
text.focus()
# Adding some text
text.insert(END, "In this window we will entry the text.")
#Get current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10,width=5,command=spinbox_used)
spinbox.pack()

#Scale
#Colled with current scale value
def scale_used(value):
    print(value)
scale=Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On buttonchecked, otherwise 0
    print(checked_state.get())
    #variable to hold on to checked state, 0 is of, 1 is on
    checked_state=IntVar()
    checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
    checked_state.get()
    checkbutton.pack()

    ##Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
stocks = ["Apple", "Amazon", "Alphabet", "Meta"]
for item in stocks:
    listbox.insert(stocks.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()























window.mainloop()  # like while loop listens what the user is doing
