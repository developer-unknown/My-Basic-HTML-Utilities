def add(a,b):
    result = a+b
    return result

def divide(a,b):
    #detect divide by zero
    if b ==0:
        print("Sorry, you cannot divide by zero.")
        return 0
    else:
        result = a/b
        
    return result

def mult(a,b):
    return (a *b)

def sub(a,b):
    return(a-b)  



choice = 0
while choice != exit:
  try:
    choice = int(input(" Choose your function: [0 to add, 1 to subtract, 2 to multiply, 3 to divide]:")) 
    if choice > 3:
      print("Incorrect choice")
      break;
    else:
      if choice == 0:
          first = int(input("Enter your first number:"))
          second = int(input("Enter your second number:"))
          print("Your answer is " + str(add(first,second)))
      if choice == 1:
          first = int(input("Enter your first number:"))
          second = int(input("Enter your second number:"))
          print("Your answer is " + str(sub(first,second)))
      if choice == 2:
          first = int(input("Enter your first number:"))
          second = int(input("Enter your second number:"))
          print("Your answer is " + str(mult(first,second)))
                                            
      if choice == 3:
          first = int(input("Enter your first number:"))
          second = int(input("Enter your second number:"))
          print("Your answer is " + str(divide(first,second)))


  except ValueError:
    print("Invalid")
    continue
