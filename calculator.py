num1=float(input("enter the first number: "))
num2=float(input("enter the second number: "))   
print("select operation:")     
print("1.addition")
print("2.substraction")
print("3.multiplication")
choice=input("enter your choice (1-3): ")
if choice=="1":
    print("result:",num1+num2)
elif choice=="2":
    print("result:",num1-num2)
elif choice=="3":
    print("result:",num1*num2)
else:
    print("invalid")