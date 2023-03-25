class Account:  #create class 
    def __init__(self,title=None,Balance=0):
        self.title=title
        self.Balance=Balance


class SavingsAccount(Account):  #create subclass e r
    def __init__(self,title,Balance,interestRate):
        self.interestRate=interestRate
        super().__init__(title,Balance)
        
    def display(self): 
      return(f" Account Holder Name : {self.title}  \n Account Balance : {self.Balance} Rs. Only \n Interest Rate : {self.interestRate} % ") 
print("We welcome you to State Bank Of India !!!  ")
print("You can check Your Balance and Respective InterestRate Here ")           
obj=SavingsAccount("Rishav Raj",5000,5)
print(obj.display())