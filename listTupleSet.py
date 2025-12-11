# list [] = mutable, most flexible
# tuple () = immutable, faster
# set {}   = mutable (add/remove), unordered,
#            No duplicates, best for membership testing

# these are similar to arrays but in python 
# there are different variety of them

places = ["Home", "School", "Workplace", "Park", "Gym"]
# to call a list places[enter a number] lists are the same as arrays
# they starts at 0

# places[0] = "Playground" # this changes "Home" to "Playground"
# places.append("Playground") # adds "Playground" to the end of the list
# places.remove("School") # removes "School" from the list
# places.pop(0) # pops/removes the element at index 0 ("Home")
# places.clear # removes all the elements from the list


places = ("Home", "School", "Workplace", "Park", "Gym")
# the difference between lists and tuples is that the elements
# can't be changed after they where created this makes them faster


places = {"Home", "School", "Workplace", "Park", "Gym"}
# in set arrays you can add and remove elements but you can't
# replace them. sets are unordered the order of the sets changes
# every time. sets don't allow duplicates you can't just put 
# multiple "Home"'s in there you would not get an error but it will
# only use one of the multiple "Home"'s it has.

# places.add("Playground") # this adds "Playground" somewhere in the set. it's random as well
# places.remove("Home") # this removes "Home" from the set.
# places.clear() # this clears the set

# this is a membership test
place = input("Enter a place: ")
if place in places:
  print(f"{place} was found in the set")
  
else:
  print(f"{place} was not found in the set")



for place in places:
  print(place, end=" ")