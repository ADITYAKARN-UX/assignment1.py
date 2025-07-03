#task1
n=input("Enter a number: ")
def factorial(n):
    if n<2:
        return 1
    else:
        return n*(factorial(n-1))
    

result=factorial(5)
print("Factorial of 5 is: ",result)

#===========================================

#task 2
import math  
n=int(input("Enter a number: "))
print("Square root:",math.sqrt(n))
print("Logarithm:",math.log(n))
print("Sine:",math.sin(n))
