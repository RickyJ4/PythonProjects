#OOP project 
class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def user_details(self):
        return f'Hello {self.username}'
    
    def user_pass(self):
        return self.password
    
#Prints Account Info 
class Account_Summary:
    def __init__(self):
    #Storing User Transaction History
        self.chequing_account = []
        self.savings_account = []
    #Adding User Amount to respective accounts
    def append_to_chequing(self, amount):
        self.chequing_account.append(amount)

    def append_to_savings(self, amount):
        self.savings_account.append(amount)

    def get_chequing_transactions(self):
        return self.chequing_account
    
    def get_savings_transactions(self):
        return self.savings_account
    
    def chequing_total(self):
        return sum(self.chequing_account)
    
    def savings_total(self):
        return sum(self.savings_account)
    
# Deposits money into respective accounts 
class Deposit:
    def __init__(self,amount_deposited):
        self.amount_deposited = amount_deposited
        self.account_summary = Account_Summary()
                                                                                                                                                                                                                                                                                                                                            
    def account_statement(self):
        account = input('Which account would you like to deposit in\n 1: Chequing \n2: Savings\n3 View Statement :')
        if(account =='1'):
            self.account_summary.append_to_chequing(int(self.amount_deposited))
            return f'{self.amount_deposited} deposited in Chequing Account'
        elif(account =='2'):
            self.account_summary.append_to_savings(int(self.amount_deposited))
            return f'{self.amount_deposited} deposited in Savings Account'
        elif(account =='3'):
            return f'Chequing Account: {self.account_summary.chequing_total()}\n Savings Account: {self.account_summary.savings_total()}'
        else:
            return 'No option selected'
# Withdraws money into respective accounts and calculates the total#
class Withdrawl:
    def __init__(self, amount_withdrawn):
        self.amount_withdrawn = amount_withdrawn
        self.account_summary = Account_Summary()

    def new_total(self):
        self.account = input('Which account would you like to Withdraw in\n 1: Chequing \n2: Savings :')
        if(self.account == '1'):
            self.new_cheq_total  = self.account_summary.chequing_total - self.amount_withdrawn
            return(f'Amount Left in Chequing : {self.new_cheq_total}')
        else:
            self.new_sav_total = self.account_summary.savings_total - self.amount_withdrawn
            return(f'Amount in Saving : {self.new_sav_total}')
# Estimates how much account will grow by in x years.
class estimated_savings_growth:
    def compound_intrest(principal,rate,time,compounded):
        amount = principal *(1+rate/compounded) ** (compounded * time)
        return amount
        

print('Enter Your Login Details')

user_info = input('Enter Your username : ')
user_pass = input('Enter Your password : ')

print('What would you like to do today ')
task = input('1: Deposit Money\n 2: Withdraw Money\n 3: Calculate Account Growth : ' )

if(task == '1'):
    deposited = int(input('How much would you like to deposit today : '))
    deposit_instance = Deposit(deposited)
    result = deposit_instance.account_statement()
    print(result)
elif(task == '2'):
   withdrawn = int(input('How much would you like to Withdraw today : '))
   withdraw_instance = Withdrawl(withdrawn)
   withdrawn_amount = withdraw_instance.new_total()
   print(withdrawn_amount)
elif(task =='3'):
    initial_amount = int(input(('Enter Amount : ')))
    time = int(input('Enter number of years : '))
    intrest_amount = estimated_savings_growth.compound_intrest(initial_amount,0.05,time, 12)
    print(f'$ {intrest_amount}')
    

else: 
    print('Invalid')


    









