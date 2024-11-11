from tkinter import *
root=Tk()
"""for relief in  [RAISED, SUNKEN, RIDGE, GROOVE, SOLID]:
    f = Frame(root, borderwidth=2, relief=relief)
    Label(f, text=relief, width=10).pack(side=LEFT)
    f.pack(side=LEFT, padx=5, pady=5)"""

class GUI:
    def __init__(self):

        of = [None]*5
        for bdw in range(5):
            of[bdw] = Frame(root, borderwidth=0)
            Label(of[bdw], text="borderwidth=%d " % bdw).pack(side=LEFT)
            ifx=0
            iff=[]
            for relief in [RAISED, SUNKEN, FLAT, RIDGE, GROOVE, SOLID]:
                iff.append(Frame(of[bdw], borderwidth=bdw, relief=relief))
                Label(iff[ifx],text=relief, width=10).pack(side=LEFT)
                iff[ifx].pack(side=LEFT, padx=7-bdw, pady=5+bdw)
                ifx=ifx+1
                of[bdw].pack()

        mainloop()

GUI()