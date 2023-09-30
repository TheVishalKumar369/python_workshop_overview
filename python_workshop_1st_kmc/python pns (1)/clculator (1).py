def add(a,b): 
    return a+b

def sub(a,b): 
    return a-b

def multi(a,b): 
    return a*b

def div(a,b):
    if b == 0:
        print("Mathn Error")
    else:
     return a/b 
    
def repeat():
    con = input("Do you want to continue?(y/n): ")
    if con =="y":
        return True
    elif con == "n":
      return False
    else: 
       print("Error occured!!")

