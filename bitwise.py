# # sum of two numbers
a = 10
b = 20
print(" Addition of two numbers:",a+b)

# # DIFFERENCE BETWEEN TOW NUMBERS
a = int(input())
b = int(input())
print("difference between:",a-b)

# # PRODUT OF THREE NUMBERS
a = int(input())
b = int(input())
c = int(input())
print("product of a,b,c:",a*b*c)

# # REMAINDER AND QUOTITENT OF A,B
a = int(input)
b = int(input)
print("reminder of a,b is:",a%b)
print("quotitent of a,b:", a/b)

# SWAPING TWO NUMBERS
a = 4
b = 6
temp = a
a = b
b = temp
print(f"a = {a}")
print(f"b = {b}")

# TO FIND EVEN OR ODD
n = int(input())
if n % 2 == 0:
    print("The n is even")
else:
    print("The n is odd number")

# FIND A AREA AND PERIMETER OF RECTANGLE
l = 5
b = 6
print(f"Area of rectangle: {l*b}")
print(f"perimeter of rectangle: {2*(l*b)}")

# Celsius to Fahrenheit
c = 3
f = (c * 9/5)+32
print(f)

# CHECK THE NUMBER DIVISIBLE BY BOTH 3 AND 5

n = int(input("Enter the number: "))
if n % 3 == 0 and n % 5 == 0:
    print(f"{n} number is divisible by 3 and 5")
else:
    print(f"{n} Not divisible by 3 and 5")