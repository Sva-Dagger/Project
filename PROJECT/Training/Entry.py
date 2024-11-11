from tkinter import *

Label(text="Anagram").pack(side=LEFT, padx=5, pady=10)
e= StringVar()
Entry(width=40, textvariable=e).pack(side=LEFT)
e.set("A shroe! A shroe! My dingkom for a shroe!")
mainloop()