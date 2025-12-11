# arithemtic = +, -, *, /, % these work the same way they 
#                            do on c++
#              // integer division this returns an integer
#                 rather than a float (rounded down)


money = 0

money += 100
# the ++ operator doesn't exist in python

money -= 5

money /= 2
# if you divide any number using the normal division
# it turns the integer into a float
# and you can't just use the integer division after
# to turn it back to an integer

money //= 2

money *= 100000

money %= 1


print(money) # prints 0.0