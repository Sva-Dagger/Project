from tkinter import *

root = Tk()
root.title("TOP LEVEL")
t1 = Toplevel(root)
Label(t1, text="HI...").pack(padx=10, pady=10)
t2 = Toplevel(root)
Label(t2, text="HI...").pack(padx=10, pady=10)
t2.transient(root)
t3 = Toplevel(root, borderwidth=6, bg="blue")
Label(t3, text="No warm decorations", bg="blue", fg="white").pack(padx=10, pady=10)
t3.overrideredirect(1)
t3.geometry("200x70+150+150")
root.mainloop()