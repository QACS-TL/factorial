import os
import time

def fact(num):
    factorial = 1
    if num == 0:
        print("The factorial of 0 is 1")
    else:
       for i in range(1,num + 1):
           if i == 0:
               continue
           factorial = factorial*i
       return factorial

def reverse_fact(num):
    count = 0
    for i in range(num):
        if i == 0:
            continue
        if num == 1:
            count = str(count)
            count = count + "!"
            return count
            break
        elif num < 1:
            return "NONE"
            break
        num = (num/i)
        count += 1

def main():
    while True:
        print("Welcome!")
        print("Please choose from the following options :")
        print("Calulate a factorial (1)")
        print("Find the factorial of a number (2)")
        selection = input()
        validation = False

        if selection == "1":
            while validation == False:
                num = input("Please enter number to be factorialised: ")
                validation = int_validator(num)
            num = int(num)
            result = factorial(num)
            print("The factorial of",num,"is",result)
            use_again()
        elif selection == "2":
            while validation == False:
                num = input("Please enter number to find the original factorial: ")
                validation = int_validator(num)
            num = int(num)
            result = reverse_fact(num)
            if result == "NONE":
                print(result)
            else:
                print(num,"'s factorial is: ",result)

            use_again()
        else:
            print("Invalid input!")
            continue

def use_again():
    while True:
        again = input("Do you want to enter another? (Y/N) : ").lower()
        if again == "y":
            main()
            break
        elif again == "n":
            print ("Bye!")
            exit()
        else:
            print("Invalid Input")
            continue

def int_validator(num):    #Auto validates int user inputs
    try:
        num = int(num)
        if num < 0:
            clear()
            print("Input cannot ne negative number!")
            return False
        else:
            return True
    except ValueError:
        clear()
        print("Invalid input")
        return False

def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')
    
if __name__ == "__main__":
    main()
    # a comment is a banana