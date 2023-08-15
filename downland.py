from tkinter import *


def km_to_mi():
    number = bemenet1.get()
    print(number)


# fuggveny
win = Tk()
# az ablak neve/cime
win.title('Konverter')
# az ablak merete
win.geometry('800x800')

Label(win, text='kilometer', font='Helvetica 12 bold').grid(row=0, column=1)
Label(win, text='merfold', font='Helvetica 12 bold').grid(row=1, column=1)

Button(win, text='calculate km to mi', command=km_to_mi, font='Helvetika 12 bold').grid(row=2, column=0)

bemenet1 = Entry(win, font='Helvetika 20 bold')
bemenet1.grid(row=0, column=0)

text1 = Text(win, height=1, width=20, state=DISABLED, font='Helvetica 20 bold')
text1.grid(row=1, column=0)

win.mainloop()
