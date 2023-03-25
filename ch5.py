class Account:
    def __init__(self,title=None,balance=0):
        self.title=title
        self.balance=balance
    def withdrawl(self,amount):
        self.balance=self.balance-amount 
    def deposit(self,amount):
        self.balance=self.balance+amount
    def getBalance(self):
        return self.balance
class SavingsAccount(Account):
    def __init__(self,title=None,balance=0,interestRate=0):
        super().__init__(title,balance)
        self.interestRate=interestRate
    def interestAmount(self):
        interestAmount=self.balance*self.interestRate/100
        return(self.balance*self.interestRate/100)

demo1=SavingsAccount("Rishav",2000,5)
print("Initial balance: ",demo1.getBalance())
demo1.deposit(500)
print("Updated balance after deposit: ",demo1.getBalance())
demo1.withdrawl(500)
print("Updated balance after withdrawal: ",demo1.getBalance())
print("Interest Rate is: 5% ")
print("Interest amount is: ",demo1.interestAmount())


#User Input


class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    def display(self): 
      return(f"Account Holder Name : {self.title}\nAccount Balance : {self.balance} Rs. Only ")
    def withdrawal(self, withdrawal_amount):
        self.withdrawal_amount = withdrawal_amount
        if self.balance>= withdrawal_amount:
           self.balance = self.balance - self.withdrawal_amount
        
        else:
            print("\nSorry !! You have Insufficient Balance","\nAvailable Balance :" ,self.balance,'Rs. Only')
            print('Try Again..!!')
            exit()
      
    def deposit(self, deposit_amount):
        self.deposit_amount = deposit_amount
        self.balance = self.balance + self.deposit_amount

    def getbalance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self,title=None,balance=0,interestRate=5):
        super().__init__(title, balance)
        self.balance = balance
        self.interestRate = interestRate

    def interestAmount(self):
        self.interest_amount = (5 * self.balance)/100
        return self.interest_amount
    def display(self): 
      return(f"Interest Rate : {self.interestRate} % ")
print("Welcome to SBI" )    
name=input('Please Enter Your Full Name : ')
print('Bank Account Details : ')
obj=Account(name,2000)
print(obj.display())
deposit_amount =int (input("Enter Amount to be Deposited : "))
obj.deposit(deposit_amount)
print("After deposit:Total Amount is : ",obj.getbalance(),'Rs.')
withdrawal_amount =int (input("Enter Amount to be Withdrawn :"))
obj.withdrawal(withdrawal_amount)
print("After withdrawal: Net Available Balance is :",obj.getbalance(),'Rs.')
print('Saving Account Details >>> ')
obj=SavingsAccount(name,2000,5)
print(obj.display())
print("Interest Amount : ",obj.interestAmount() ,'Rs. ')
