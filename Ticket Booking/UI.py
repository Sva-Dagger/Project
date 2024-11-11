from tkinter import *
from tkinter import Tk
import sqlite3
from SQL import SQL
sql =SQL()

class Ui:
    def __init__(self):
        self.window = Tk()
        self.window.title("Bus Ticket Booking")
        self.window.configure(bg="grey", padx=120, pady=100)
        self.window.geometry("1366x768")
        self.connection = sqlite3.connect("Booking.db")
        self.cursor = self.connection.cursor()
        self.Booking_UI()
        self.window.mainloop()

    def Booking_UI(self):
        Welocome_Label = Label(text="Welcome to Bus Ticket Booking", bg="grey",fg="white", font=("Arial", 25, "bold"))
        Welocome_Label.grid(column=1, row=0,padx=10,pady=10)

        Pickup_Location_Label = Label(text="Pickup Location:",width=20,bg="grey", font=("Arial", 15, "bold"))
        Pickup_Location_Label.grid(column=0, row=2,padx=10,pady=10)
        self.Pickup_Location_Entry = Entry(width=20, font=("Arial", 15, "bold"))
        self.Pickup_Location_Entry.grid(column=1,row=2,padx=10,pady=10)

        Destination_Location_Label = Label(text="Destination Location:",width=20,bg="grey", font=("Arial", 15, "bold"))
        Destination_Location_Label.grid(column=0, row=3,padx=10,pady=10)
        self.Destination_Location_Entry = Entry(width=20, font=("Arial", 15, "bold"))
        self.Destination_Location_Entry.grid(column=1, row=3,padx=10,pady=10)

        button = Button(command=self.Ticket_Price_check, text="Price", width=20, bg="grey", font=("Arial", 15, "bold"))
        button.grid(column=0, row=5, padx=10, pady=10)

    def check_seat(self):
        self.DESTROY_WIDGET()
        self.window.configure(padx=50, pady=50, bg="grey")
        self.window.geometry("1600x1200")
        Availabe_Seat = [("A1", 0, 1), ("A2", 0, 2), ("A3", 0, 3),
                         ("B1", 1, 1), ("B2", 1, 2), ("B3", 1, 3),
                         ("C1", 2, 1), ("C2", 2, 2), ("C3", 2, 3),]
        for (text, column, row) in Availabe_Seat:
            create_button = Button(text=text, bg="grey", fg="white", font=("Arial", 14, "bold"),
                                   command=lambda t=text: Seat_Entry.insert(END, t))
            create_button.grid(column=column, row=row, padx=10, pady=10)
        Seat_Entry = Entry(width=5, font=("Arial", 14))
        Seat_Entry.grid(column=3, row=1, padx=10, pady=10)
        self.Your_Seat = Seat_Entry.get()

    def Ticket_Price_check(self):
        try:
            Pickup_Location = self.Pickup_Location_Entry.get().title()
            Destination_Location = self.Destination_Location_Entry.get().title()
            self.cursor.execute('''select Ticket_Price from Ticket_Price where Pickup_Location=? and Destination_Location=?''',
                                (Pickup_Location, Destination_Location))
            item = self.cursor.fetchall()
            Ticket_Price = item[0][0]
            Price_label = Label(text=f"Your Ticket Price is Rs.{Ticket_Price}", bg="grey", fg="white",
                                font=("Arial", 14, "bold"))
            Price_label.grid(column=1, row=5, padx=10, pady=10)
            Check_Seat = Button(text="Check Seat", bg="grey", fg="white", font=("Arial", 14, "bold"), command = self.check_seat)
            Check_Seat.grid(column=1, row=6, padx=10, pady=10)
        except IndexError:
            Price_label = Label(text="Please check whether the Data is correct", bg="grey", fg="white",
                                font=("Arial", 14, "bold"))
            Price_label.grid(column=1, row=5, padx=10, pady=10)

    def DESTROY_WIDGET(self):
        for widget in self.window.winfo_children():
            widget.destroy()


Ui()