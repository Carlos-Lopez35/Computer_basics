from bank import BankAccount
while True:
    try:
        account1 = int(input("Create a new account by introducing a five-digit number (it cannot start with 0): "))
        if 10000 <= account1 <= 99999:
            break
        else:
            print("Please, type a valid number.") 
    except ValueError:
        print("Please enter a valid number.")
account = BankAccount(account1)
while True:
    service = input("If you want to make a deposit type 'deposit', if you want to make a withdraw, type 'withdraw', if you want to check your account balance, type 'balance', if you want to check your account number, type 'acnumber', and if you have finished using the service, type 'finish': ").lower()
    if service == "deposit":
        try:
            amount = int(input("How much do you want to deposit in your account? "))
            result = account.deposit(amount)
            print(result)
        except ValueError:
            print("Please enter a valid amount.")    
    elif service == "withdraw":
        try:
            amount = int(input("How much do you want to withdraw from your account? "))
            result = account.withdraw(amount)
            print(result)
        except ValueError:
            print("Please enter a valid amount.")
    elif service == "balance":
        print(account.get_balance())
    elif service == "acnumber":
        print(account)
    elif service == "finish":
        print("Thank you for using our service!")
        break    
    else:
        print("Invalid option, please try again.")