class ATM:
    def __init__(self, balance):
        self.balance = balance
        self.denominations = [100, 200, 500]

    def display_balance(self):
        print(f"Available Balance: {self.balance}")

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

def main():
    atm = ATM(balance=2000)  # Initial balance

    while True:
        atm.display_balance()
        try:
            amount = int(input("Enter amount to withdraw (or -1 to exit): "))
            if amount == -1:
                print("Thank you for using the ATM!")
                break
            atm.withdraw(amount)
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

if __name__ == "__main__":
    main()
