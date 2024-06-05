# print ("Hello world!")

# x = "Hello Python"
# print (x)

# y = 42
# print (y)

# print(42 + str(2))

# print("Hello", str(2))

# first_name = "Jihwan"
# last_name = "Eo"
# age = 31
# print(f"My name is {first_name} {last_name} and I am {age} years old")

# Practice Challenge: Correct the errors!
first_name = "Alana"
last_name = "Da Silva"
age = 36
profession = "Software Developer"
years_experience = 5
greeting = f"Hello my name is {first_name} {last_name}"
print(greeting) 
# Desired output: Hello my name is Alana Da Silva
print(f"I am {age} years old") 
# Desired output: I am 36 years old
print("I work as a {}.".format(profession))
# Desired output: I work as a Software Developer.
exp_string = "I have worked in the field for {} years."
print(exp_string.format(years_experience))
# Desired output: I have worked in the field for 5 years.
print(f"I started in the field when I was {age - years_experience} years old.")
# Desired output: I started in the field when I was 31 years old.
print(first_name.upper())

ex = "kkkkkkkkkkk"
print(ex.count("k"))

ex1 = "suwon is home of football"
print(ex1.split("is"))
print(ex1.find("w"))
print(ex1.isalpha())

ex2 = ["suwon", "is", "home of football"]
print(ex.join(ex2))

print(type(ex2))
print(ex1.endswith("l"))