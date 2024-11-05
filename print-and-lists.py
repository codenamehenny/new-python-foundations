# Python Fundamentals

# Task 1: Hello World Program: Write and run a simple program that prints Hello, World! (Chapter 2).
print("Hello World!")

# Task 2: 2. Working with Lists:
#Create a list of your favorite hobbies and print each one using a for loop.
# Modify the list by adding, removing, and sorting the items using list methods (e.g., append(), pop(), sort()).

# initial hobbies list
hobbies = ["Reading", "Studying", "Gaming"]

# adding a hobby using the append function
hobbies.append("Knitting")

# removing reading from the list by using the pop function with index at 0
hobbies.pop(0)

# sort the list by aphlabetical order 
hobbies.sort()

# iterating over each hobby in the list
print("My hobbies are:")
for hobby in hobbies:
    print(hobby)