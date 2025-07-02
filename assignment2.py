#task 1
a = int(input("Enter a number: "))
if (a%2 != 0):
    print(a," is an odd number.")
else:
    print(a, "is a even number.")

#======================================
#task 2

sum=0
for x in range(1, 51):
    sum +=x
    print("The sum of numbers from 1 to 50 is:",sum)