# for loops = works the same way it does in c++
#             in the range of the for loop the
#             first number is inclusive, the
#             second number is exclusive and the
#             third number is the amount it adds
#             on each eteration

# this prints i from 0 to 10
# in c++ this would be for(int i = 0; i < 11; i++)
for i in range(11):
  print(i)

print("")

# this prints i like this 1 <= i < 11
for i in range(1, 11):
  print(i)

print("")

# in c++ this would be for(int i = 0; i < 11; i+= 2)
for i in range(0, 11, 2):
  print(i)

print("")

# in c++ this would be for(int i = 10; i > 0; i--)
for i in range(10, 0, -1):
  print(i)