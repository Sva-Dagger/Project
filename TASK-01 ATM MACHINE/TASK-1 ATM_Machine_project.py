from tkinter import *
import smtplib
import time

THEME_COLOR ="#375362"

class ATM:
    def __init__(self):
        self.window = Tk()
        self.window.title("ATM MACHINE")
        self.balance = 10000
        self.denominations = [100, 200, 500]
        self.balance = 1000
        self.my_email = "hackersiva847@gmail.com"
        self.password = "ccnffohqpwivwijz"

        self.welcome()
        self.window.mainloop()
    def display_balance(self):
        Bank_having= Label(text = f"Available Balance: {self.balance}")
        Bank_having.grid()
    def validate_withdrawal(self, amount):
        if amount % 100 != 0:
            return False
        if amount > self.balance:
            return False
        return True

    def withdraw(self, amount):
        if self.validate_withdrawal(amount):
            self.balance -= amount
            print(f"Withdrawal Successful: {amount}")
            self.display_balance()
        else:
            print("Withdrawal Failed: Check amount or balance.")

    def welcome(self):
        time.sleep(3)
        self.Balance_check_pin = False
        self.Withdraw_check_pin = False
        for widget in self.window.winfo_children():
            widget.destroy()
        self.window.configure(padx=300, pady=150, bg=THEME_COLOR)
        self.Welcome_label = Label(text="Welcome to our ATM Machine",
                                   width = 25, bg=THEME_COLOR, fg="white",
                                   font=("Ariel", 20 , "bold"))
        self.Welcome_label.grid(column=1, row=0, pady=20)

        self.Insert_label = Label(text="Please insert your card",
                                  width=20, bg=THEME_COLOR, fg="white",
                                  font=("Ariel", 28, "bold"))
        self.Insert_label.grid(column=1, row=1, pady=20)

        self.Card_button = Button(text="Insert card",
                                  width=30, bg=THEME_COLOR, fg="white",
                                  font=("Ariel", 28, "bold"), command=self.show_pin_entry)
        self.Card_button.grid(column=1, row=2, pady=20)

    def show_pin_entry(self):

        for widget in self.window.winfo_children():
            widget.destroy()
        self.window.configure(padx=200, pady=100, bg=THEME_COLOR)

        self.pin_entry_label = Label(text="PLEASE ENTER YOUR PIN",
                               bg=THEME_COLOR,fg="white",
                               font=("Ariel", 20,"bold"))
        self.pin_entry_label.grid(column=4, row=1, pady=20)

        # Create an Entry widget for the PIN
        self.pin_entry = Entry(width=13, show="*", font=("Ariel", 20))
        self.pin_entry.grid(column=4, row=2, pady=20)

        # Create buttons for numbers
        self.create_number_buttons()

        # Create buttons for actions
        self.cancel_button = Button(text="CANCEL", width=10,
                                    fg="black", bg=THEME_COLOR,
                                    font=("Ariel", 28, "bold"))
        self.cancel_button.grid(column=5, row=2, padx=20, pady=20, columnspan=2)

        self.clear_button = Button(text="CLEAR", width=10, fg="black", bg=THEME_COLOR, font=("Ariel", 28, "bold"), command=self.clear_pin)
        self.clear_button.grid(column=5, row=3, padx=20, pady=20, columnspan=2)

        self.enter_button = Button(text="ENTER", width=10, fg="black", bg=THEME_COLOR, font=("Ariel", 28, "bold"), command=self.check_pin)
        self.enter_button.grid(column=5, row=4, padx=20, pady=20, columnspan=2)

        if self.Balance_check_pin == True:
            self.enter_button.configure(command=self.balance_check_pin)
        elif self.Withdraw_check_pin == True:
            self.enter_button.configure(command=self.withdraw_check_pin)

    def create_number_buttons(self):
        buttons = [
            ("1", 0, 2), ("2", 1, 2), ("3", 2, 2),
            ("4", 0, 3), ("5", 1, 3), ("6", 2, 3),
            ("7", 0, 4), ("8", 1, 4), ("9", 2, 4),
            ("0", 1, 5)
        ]
        for (text, col, row) in buttons:
            button = Button(text=text, fg="black",
                            bg=THEME_COLOR, font=("Ariel", 28, "bold"),
                            command=lambda t=text: self.pin_entry.insert(END, t))
            button.grid(column=col, row=row, padx=20, pady=20)


    def clear_pin(self):
        self.pin_entry.delete(0, END)

    def clear_amount(self):
        self.withdrawal_entry.delete(0, END)

    def check_pin(self):
        pin = self.pin_entry.get()
        if pin == "1234":  # Example PIN check
            self.user_choice_section()
        else:
            self.pin_entry.delete(0, END)
            self.Incorrect_pin_message()

    def balance_check_pin(self):
        pin = self.pin_entry.get()
        if pin == "1234":  # Example PIN check
            self.show_balance()
        else:
            self.pin_entry.delete(0, END)
            self.show_message("Incorrect Pin")

    def withdraw_check_pin(self):
        pin = self.pin_entry.get()
        if pin == "1234":  # Example PIN check
            self.withdraw_section()
        else:
            self.pin_entry.delete(0, END)
            self.show_message("Incorrect Pin")

    def user_choice_section(self):
        # Clear existing widgets
        for widget in self.window.winfo_children():
            widget.destroy()
        self.window.configure(padx=400, pady=50, bg=THEME_COLOR)

        # Display user choices
        self.pin_label = Label(text="YOUR_BANK",
                               bg=THEME_COLOR, fg="white",
                               font=("Ariel", 60, "bold"))
        self.pin_label.grid(column=1, row=0, pady=20)
        self.pin_label = Label(text="Main Menu",
                               bg=THEME_COLOR, fg="white",
                               font=("Ariel", 28, "bold"))
        self.pin_label.grid(column=1, row=1, pady=20)
        self.pin_label = Label(text="Choose an option:",
                               bg=THEME_COLOR, fg="white",
                               font=("Ariel", 28, "bold"))
        self.pin_label.grid(column=1, row=2, pady=20)

        self.balance_button = Button(text="Check Balance",
                                     width=20, command=self.check_balance_pin,
                                     bg=THEME_COLOR, fg="white",
                                     font=("Ariel", 24))
        self.balance_button.grid(column=1, row=3, pady=20)

        self.withdraw_button = Button(text="Withdraw",
                                      width=20, command=self.withdraw_section_pin,
                                      bg=THEME_COLOR, fg="white",
                                      font=("Ariel", 24))
        self.withdraw_button.grid(column=1, row=4, pady=20)

        self.exit_button = Button(text="Exit",
                                  width=20, command=self.welcome,
                                  bg=THEME_COLOR, fg="white",
                                  font=("Ariel", 24))
        self.exit_button.grid(column=1, row=5, pady=20)

    def check_balance_pin(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        self.Balance_check_pin = True
        self.show_pin_entry()

    def show_balance(self):
        pin = self.pin_entry.get()
        if pin == "1234":
            balance_message = f"Your balance is: ${self.balance:.2f}"
            self.show_message(balance_message)
        else:
            self.show_message("Invalid PIN!")

    def withdraw_section_pin(self):
        # Clear existing widgets
        for widget in self.window.winfo_children():
            widget.destroy()
        self.Withdraw_check_pin = True
        self.show_pin_entry()

    def withdraw_section(self):
        pin = self.pin_entry.get()
        if pin == "1234":
            # Clear existing widgets
            for widget in self.window.winfo_children():
                widget.destroy()
            amount = 0
            self.withdrawal_entry = Entry(width=15, font=("Ariel", 30))
            self.withdrawal_entry.grid(column=4, row=2, pady=20, padx=20)

            buttons = [
                ("1", 0, 2), ("2", 1, 2), ("3", 2, 2),
                ("4", 0, 3), ("5", 1, 3), ("6", 2, 3),
                ("7", 0, 4), ("8", 1, 4), ("9", 2, 4),
                ("0", 1, 5)
            ]
            for (text, col, row) in buttons:
                button = Button(text=text, fg="black",
                                bg=THEME_COLOR, font=("Ariel", 28, "bold"),
                                command=lambda t=text: self.withdrawal_entry.insert(END, t))
                button.grid(column=col, row=row, padx=20, pady=20)

            self.pin_label = Label(text="Enter available amount to withdraw\n$100\n$200\n$500", width=28, bg=THEME_COLOR, fg="white", font=("Ariel", 14, "bold"))
            self.pin_label.grid(column=4, row=0, pady=20, padx=20)

            # Create an Entry widget for the withdrawal amount

            self.confirm_button = Button(text="Confirm",width=10, command=self.process_withdrawal, bg=THEME_COLOR, fg="white", font=("Ariel", 24))
            self.confirm_button.grid(column=5, row=2, padx=20, pady=10)

            self.clear_button = Button(text="CLEAR", width=10, fg="black", bg=THEME_COLOR, font=("Ariel", 28, "bold"),
                                       command=self.clear_amount)
            self.clear_button.grid(column=5, row=3, padx=20, pady=20, columnspan=2)

            back_button = Button(text="Back",  width=10, command=self.user_choice_section, bg=THEME_COLOR, fg="white", font=("Ariel", 24))
            back_button.grid(column=5, row=4, pady=20, padx=20)
        else:
            self.show_message("Invalid PIN!")

    def process_withdrawal(self):
        self.amount = self.withdrawal_entry.get()
        self.withdrawal_entry.delete(0, END)
        self.amount = int(self.amount)
        if self.amount % 100 == 0:
            self.withdraw_amount()
        else:
            self.show_message("Invalid amount entered")

    def withdraw_amount(self):
        try:
            self.amount = float(self.amount)
            if self.amount <= 0:
                self.show_message("Please enter a valid amount!")
            elif self.amount > self.balance:
                self.show_message("Insufficient funds!")
            else:
                self.balance -= self.amount
                with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                    connection.starttls()
                    connection.login(self.my_email, self.password)
                    print("connected")
                    connection.sendmail(from_addr=self.my_email,
                                        to_addrs="sivam4266@gmail.com",
                                        msg=f"subject:Amount debited\n\n${self.amount} Withdrawal successful! Your balance: ${self.balance:.2f}")
                self.show_message(f"Withdrawal successful! Your balance: ${self.balance:.2f}")
        except ValueError:
            self.show_message("Invalid amount!")

    def Incorrect_pin_message(self):
        # Clear existing widgets
        for widget in self.window.winfo_children():
            widget.destroy()

        message_label = Label(text="Incorrect Pin", bg=THEME_COLOR, fg="white", font=("Ariel", 28, "bold"))
        message_label.pack(pady=20)

        back_button = Button(text="Back", command=self.show_pin_entry, bg=THEME_COLOR, fg="white", font=("Ariel", 24))
        back_button.pack(pady=10)

    def show_message(self, message):
        # Clear existing widgets
        for widget in self.window.winfo_children():
            widget.destroy()

        message_label = Label(text=message, width=100, bg=THEME_COLOR, fg="white", font=("Ariel", 28, "bold"))
        message_label.pack(pady=20)

        back_button = Button(text="Back", command=self.welcome, bg=THEME_COLOR, fg="white", font=("Ariel", 24))
        back_button.pack(pady=10)

ATM()
