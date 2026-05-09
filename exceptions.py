import sys

x=int(input("x : "))
y=int(input("y : "))
try:
    result=x/y
except :
    print("you have ZeroDivisionError")

print(f"{x}/{y}={result}")