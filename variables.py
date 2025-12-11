# you don't need to add the type of a variable to
# the start like you do in c++
# there are four types string, integer, float, boolean

name = "Mahmud" # this variable is of string type

age = 20 # this variable is of integer type

height = 174.69 # this variable is of float type

isStudent = True # this variable is of boolean type
# note that we can't do isStudent = 0 like we do in cpp


print(f"Hello {name}")
# the f"" is called an f string 
# it makes it so that we can isnert a varibale in the string

print(f"My age is {age}")

print(f"I'm {height}cm tall")

if isStudent:
  print("I'm a student")

else:
  print("I'm homeless")