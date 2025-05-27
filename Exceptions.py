import sys
x=int(input("X:"))
y=int(input("Y:"))
try:
    res=x/y
except ZeroDivisionError:
    print("cannot divide by zero")
    sys.exit(1)
print(f"the result of {x}/{y}={res}")

