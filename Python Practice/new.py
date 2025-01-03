def deposit(Amount):
    if Amount <= 0:
        print("Deposited amount should be a positive value")
    else:
        print("Your amount has been deposited to your account")
def withdraw(Amount):
    if Amount <= 0:
        print("Deposited amount should be a positive value")
    elif Amount > 1000:
        print("insufficient balance")
    else:
        print("Amount has been withdrwan")

def viewaccount(Account):
    print("Account name : {}".format(Account['name']))
    print("Balance Amount : {}".format(Account['balance']))

def main():
    Account = {'name': input("Enter your name : "),'balance': 0}
    menu_options = [
        "1. View account balance",  
        "2. Deposit money",  
        "3. Withdraw money", 
        "4. Exit" ]
    while True:
        for options in menu_options:
            print(options)
        try:
            Choice = int(input("Choose an option from 1 to 4  "))
            if Choice == 1:
                Amount = int(input("Enter your Amount: "))
                deposit(Amount)
            elif Choice == 2:
                Amount = int(input("How much amount do you want to withdraw: "))
                withdraw(Amount)
            elif Choice == 3:
                viewaccount(Account)
            elif Choice == 4:
                print("Thank you for Banking")
                break
            else:
                print("Enter valid input")
        except ValueError:
            print("Invalid input, Enter a valid input")
        
main()
