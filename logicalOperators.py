# logical operators = evaluate multiple conditions (or, and, not)
#                     or  = the || operator in cpp
#                     and = the && operator in cpp
#                     not = the !  operator in cpp


temp = 25
sunny = False

if temp > 35 or temp < 0 or not sunny:
  print("The outdoor party is cancelled")

else:
  print("The outdoor party continues as scheduled")
