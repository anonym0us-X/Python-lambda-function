# We will learn about the Lambda function in python.
# A lambda function is a small anonymous function that can take any number of arguments, but can only have one expression.
# the syntax of a lambda function is:
# lambda arguments : expression
# lets see an example of the lambda function in python.

# Example 1: Square a number
sq = lambda x: x**2
print(sq(5))
# output: 25

# Example 2: Add two numbers
addnum = lambda x, y: x + y 
print(addnum(10,20))
# output: 30



# Now we will use the lambda function with map(), filter() and reduce() functions.

# 1. map(function, iterable)
# applies function to each item in iterable.

# Example 3: Using lambda function with map() function.
num = [1,2,3,4,5]
sq = list(map(lambda x: x**2, num))
print(sq)


# 2. filter(function, iterable)
# applies function to item in iterable which return true

# Example 4: Even numbers among the list
num = [1,2,3,4,5,6]
eo = list(filter(lambda x: x % 2 == 0,num)) # we use list encapsulation because the lambda stores everything in memory so to display the readable output we have to use list() casting.
print(eo)

# 3. Using sorted() for sorting the list

# Example 5: Sorting the students based on marks
students = [
    ("Alice", 90),
    ("Bob", 75),
    ("Charlie", 85)
]

sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

