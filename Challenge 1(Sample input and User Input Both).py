'''Q1Problem statement: Implement a class Point that has three properties and a method. All these attributes (properties and methods) should be public. This problem can be broken down into two tasks:

Task 1: 👉 Implement a constructor to initialize the values of three properties: x, y, and z.

Task 2: 👉 Implement a method, sqSum(), in the Point class which squares x, y, and z and returns their sum.

Sample properties 1, 3, 5

Sample method output 35'''


class Point:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def sqSum(self):
        a=self.x*self.x
        b=self.y*self.y
        c=self.z*self.z
        return(a+b+c)
obj1=Point(1,3,5)
print("Sum of square of numbers is: ",(obj1.sqSum()))

#User Input

class Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def square(self):   
        a= self.x**2
        b= self.y**2
        c= self.z**2
        return a,b,c
    def sqSum(self):
        square_sum = self.x**2 + self.y**2 + self.z**2
        return square_sum
num1=int(input("Enter num 1: "))
num2=int(input("Enter num 2: "))
num3=int(input("Enter num 3: "))
obj=Point(num1,num2,num3)
print('Square of Entered Number : ',obj.square())
print('Square Sum of Entered Number :',obj.sqSum())