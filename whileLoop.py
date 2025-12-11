# while loops = here while loops work differently 
#               if the parameter's True it continues else it exits
#               in c++ it's the opposite if the parameter's True it exits
#               if it's False it continues

number = 1
while number == 1:
  print("You are inside a while loop")  
  number = int(input("Enter any number other than 1 (one) to exit: "))
  

name = ""
while name == "":
  name = input("Enter your name: ")

print(f"Hello {name}.")