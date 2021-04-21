class Atm(object):
    def __init__(self, cardNum, pin, balance, withdraw):
        self.cardNum = cardNum
        self.pin = pin
        self.balance = 10000
        self.withdraw = withdraw

    def get_card_info(self):
        self.cardNum = int(input("Card number : "))
        self.pin = int(input("Card pin : "))

    def show_details(self):
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("Card Information")
        print("Customer name : Mayank")
        print("Card number : ", self.cardNum)
        print("Card pin : ", self.pin)
        print("Account Balance : ", self.balance)
        self.withdraw = int(input("Enter amount to withdraw : "))

    def print_debit(self):
        print(self.withdraw, "is debited successfully from your bank account :) ")


card1 = Atm("1212", "1234", "10000", "2000")
card1.get_card_info()
card1.show_details()
card1.print_debit()
