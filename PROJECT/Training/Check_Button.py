from tkinter import *
root=Tk()
var=IntVar()
for text, value in [("passing fruit", 1), ("Loganberries", 2), ("Mangoes in syrup", 3),
                   ("Oranges", 4), ("Apples", 5), ("Grapefruit", 6)]:
    Checkbutton(text=text, indicatoron=True, state=NORMAL, anchor=W,
    variable=var).grid(row=value, column=value)
    var.set(3)
mainloop()
