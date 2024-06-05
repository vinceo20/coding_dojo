# ninjas = ['Rozen', 'KB', 'Oliver']
# my_list = ['4', ['list', 'in', 'a', 'list'], 987]
# empty_list = []

# fruits = ['apple', 'banana', 'orange', 'strawberry']
# vegetables = ['lettuce', 'cucumber', 'carrots']
# fruits_and_vegetables = fruits + vegetables
# print(fruits_and_vegetables)
# salad = 3 * vegetables
# print(salad)

# veges_and_fruits = vegetables + fruits
# print(veges_and_fruits)

# drawers = ["documents", "envelopes", "pens"]
    
# # access the drawer with index of 0 and print value
# print(drawers[0])  #prints documents
# # access the drawer with index of 1 and print value
# print(drawers[1]) #prints envelopes
# # access the drawer with index of 2 and print value
# print(drawers[2]) #prints pens
    
# # replace "documents" with "tchotchkes"
# drawers[0] = "tchotchkes"
# print(drawers) # prints ["tchotchkes", "envelopes", "pens"]
    
# # stores the value "tchotchkes" in a temporary variable.
# top_contents = drawers[0]
    
# # Replaces the value at index 1
# # with whatever value is stored at index 0
# drawers[1] = drawers[0]
# print(drawers) # prints ["tchotchkes", "tchotchkes", "pens"]

# play around with the drawers!
drawers = ['documents', 'envelopes', 'pens']
# Print the second value from the list (envelopes)
print(drawers[1])

# Change "pens" to "useless manuals"
drawers[2] = "useless manuals"

# Change the first value to whatever is the second value
drawers[0] = drawers[1]
# What should the list look like now?
# ['envelopes', 'envelopes', 'useless manuals']

# Print the list! Does it match your prediction?
print(drawers)

#slicing : list [index(include):index(exclude)]

my_list = [1, 3, 2]
print(sorted(my_list))
# output

my_list.reverse()
print(my_list)

some_nums = [44,56,2,3,12,19,6]
print("Get started by writing your own code!")

# Some optional challenges to assess and refine your understanding:

# Print the length of the list.
print(len(some_nums))

# Use antoher python built-in function and print the result.
print(sorted(some_nums))

# Remove an item from the list. Remember to verify that it was removed.
some_nums.pop()
print(some_nums)

# Utilize a method from the documentation and print the result.

