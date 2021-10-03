language= "python3"
run = "python main.py"
import numpy
num1= int(input("Please enter number x:"))
num2= int(input("Please enter number y:"))
print("x**y:",num1**num2)
z=numpy.log2(num1)
if num1<=0:
  print("log2(x): invalid, x must be greater than zero")
else:
  print("log2(x): ", z)
print("My ID number is 75689")