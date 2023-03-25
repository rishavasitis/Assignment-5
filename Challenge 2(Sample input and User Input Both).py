'''Sample Output 
The sum is:  104
The difference is:  84
The product is:  940
The division is:  9.4 '''

class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return(self.num1+self.num2)
    def subtract(self):
        return(self.num2-self.num1)
    def multiply(self):
        return(self.num1*self.num2)
    def divide(self):
        return(self.num2/self.num1)

obj=Calculator(10,94)
print("The sum is: ",obj.add())
print("The difference is: ",obj.subtract())
print("The product is: ",obj.multiply())
print("The division is: ",obj.divide())



#user Input

class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        sum = self.num2 + self.num1
        return sum
    def subtract(self):
        substraction = self.num2 - self.num1
        return substraction
    def multiply(self):
        multiplication = self.num2 * self.num1
        return multiplication
    def divide(self):
        division = self.num2 / self.num1
        return division
num1=int(input("Enter num 1: "))
num2=int(input("Enter num 2: "))
obj = Calculator(num1,num2)
print('Addition of Entered two Numbers : ',obj.add())
print('Subtrction of Entered two Numbers : ',obj.subtract())
print('Multiplication of Entered two Numbers : ',obj.multiply())
print('Division of Entered two Numbers : ',obj.divide())