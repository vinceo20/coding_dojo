# Challenge 1:
#   Fill in the missing code for the full_name function.
#   Be sure to add the 2 parameters (and name them appropriately)
#   Return the full name to get the desired output!

def full_name(first_name, last_name):
    # your code here!
    return f"{first_name} {last_name}"

name1 = full_name("Eddie", "Aikau")
print(name1) # should print Eddie Aikau

# Challenge 2: 
#   Call the function again using your own name and print the results!

name2=full_name("Luan", "Zou")
print(name2)


# set defaults when declaring the parameters
def be_cheerful(name='', repeat=2):
    print(f"good morning {name}\n" * repeat)

# Function calls
be_cheerful()    # output: good morning (repeated on 2 lines)
be_cheerful("tim")    # output: good morning tim (repeated on 2 lines)
be_cheerful(name="john")    # output: good morning john (repeated on 2 lines)
be_cheerful(repeat=6)    # output: good morning (repeated on 6 lines)
be_cheerful(name="michael", repeat=5)    # output: good morning michael (repeated on 5 lines)
# NOTE: argument order doesn't matter if we are explicit when sending in our arguments!
be_cheerful(repeat=3, name="kb")    # output: good morning kb (repeated on 3 lines)


