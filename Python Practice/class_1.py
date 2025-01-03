class Bankaccount:
    def __init__(self,Account,Balance=0):
        self.Account = Account
        self.Balance = Balance
    def deposit(self,Amount):
        if Amount >= 0:
            self.Balance += Amount
            print("Amount deposited")
        else:
            print("Your amount must be Positive vaue")
    def withdraw(self,Amount):
        if Amount <= self.Balance:
            self.Balance -= Amount
            print("Amount withdrawn")
        elif Amount > self.Balance:
            print("insufficient balance")
        else:
            print("Enter positive value")
    def display(self):
        print("your account details are: ",self.Account,self.Balance)


def main():
    Account = Bankaccount("sai",2000)
    #Account1 = Bankaccount("chay",3000)
    menu_options = [ 
        "1. Deposit money",  
        "2. Withdraw money",
        "3. View account balance",
        "4. Exit" ]
    
    while True:
        for options in menu_options:
            print(options)
        try:
            Choice = int(input("Choose an option from 1 to 4  "))
            if Choice == 1:
                Amount = int(input("Enter your Amount: "))
                Account.deposit(Amount)
            elif Choice == 2:
                Amount = int(input("How much amount do you want to withdraw: "))
                Account.withdraw(Amount) 
            elif Choice == 3:
                Account.display()
            elif Choice == 4:
                print("Thank you for Banking")
                break
            else:
                print("Enter valid input")
        except ValueError:
            print("Invalid input, Enter a valid input")
        
main()
