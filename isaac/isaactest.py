from tkinter import *

window = Tk()

thelabel = Label(window, text="MARQUIS")
thelabel.pack()



input_user = StringVar()
input_field = Entry(window, text=input_user)
input_field.pack(side=BOTTOM, fill=X)

def enter_pressed(event):
    input_get = input_field.get()
    print(input_get)
    label = Label(frame, text=input_get)
    input_user.set('')
    label.pack()
    return "break"

frame = Frame(window, width=300, height=300)
frame.pack_propagate(False) # prevent frame to resize to the labels size
input_field.bind("<Return>", enter_pressed)
frame.pack()

window.mainloop()




