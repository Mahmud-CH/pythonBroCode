# functions in python: you just type def functionName(): functionBody 
#                      thats it atleast for the functions that don't 
#                      take any parameters.
#                      You can't use overloaded functions
#                  ex: def greeting():     def greeting(name): doesn't work
#                      returns, early return and all that works the same way
#                      they do in cpp 


def greeting():
  print("Hello there.")

def greetingWithNameParameter(name):
  print(f"Hello {name}")


def add(x, y):
  z = x + y
  return z


def capitalizeFirstLetter(sentence):
  sentence = sentence.capitalize()
  return sentence

greeting()
greetingWithNameParameter("Mahmud")

print(add(1, 2))


print( capitalizeFirstLetter("mahmud") )
