# Typecasting = the process of converting a variable from one data type to another
#               str(), int(), float(), bool()

name = "Mahmud"
age = 20
height = 174.69
isStudent = True


# type() gives the type of a variable
print(type(name)) # prints <class 'str'>

print(type(age)) # prints <class 'int'>

print(type(height))# prints <class 'float'>

print(type(isStudent))# prints <class 'bool'>


age = float(age) + 0.69
# age = 20.69

height = int(height)
# height = 174

name = bool(name)
# name = True
# you can check if someone entered their names or not

age = str(age) + "420"
# age = 20.69420