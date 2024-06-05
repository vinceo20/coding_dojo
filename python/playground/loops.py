for x in range(0, 10, 2):
    print(x)
# output: 0, 2, 4, 6, 8
for x in range(5, 1, -3):
    print(x)
# output: 5, 2

# Challenge: Write a for loop to print all integers from 1 to 20, including 20.

for i in range(1,21):
    print(i)

countries = ["Uganda", "Chile", "Albania", "Saudi Arabia"]

# Challenge 1: Fix the range!
for integer in range(0, len(countries)):
    print("Index:")
    print(integer)
# Challenge 2: print the index here
    print("Country:")
    print(countries[integer])
# Challenge 3: print the country here

# Looping over values only...
for country in countries:
    print("Country: ")
    print(country)
# Challenge 4: print the country here

count = 0
while count <= 5:
    print("looping - ",count)
    count += 1

for val in "string":
    if val == "i":
        break
    print(val)
# output: s, t, r

for x in range(1,10):
    if (x%3) == 0:
        print("clap")
    else:
        print(x)

print(3%3)