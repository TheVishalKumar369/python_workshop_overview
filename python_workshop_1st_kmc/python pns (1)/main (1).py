from clculator import add,sub,multi,div,repeat

a = int(input("Enter a number: "))
b = int(input("Enter a second number: "))
operator = input("Enter a operator +,-,*,/ :")

while True:
    if operator == "+":
        print(add(a,b))
    elif operator == "-":
        print(sub(a,b))

    elif operator == "*":
         print(multi(a,b))

    elif operator == "/":
         print(div(a,b)) 

    else: 
        print("invalid Input")
