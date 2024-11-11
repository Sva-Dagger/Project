from tkinter import *
root=Tk()
var=IntVar()
for text, value in [("passing fruit", 1), ("Loganberries", 2), ("Mangoes in syrup", 3),
                   ("Oranges", 4), ("Apples", 5), ("Grapefruit", 6)]:
    Data = Radiobutton(text=text, value=value, variable=var, indicatoron=True)
    Data.pack(anchor=W)
    print(Data)
    var.set(1)
mainloop()
