# Challenge yourself!

person = {"first_name": "Ada", "last_name": "Lovelace", "age": 42, "is_organ_donor": True}
# Create a another person dictionary called person_2 and print it to the terminal
person_2 = {"fist_name": "Jihwan", "last_name": "Eo", "age": 31, "is_organ_doner": False}
print(person_2)

capitals = {}
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"
# Add 2 key-value pairs to this dictionary.
capitals['kor'] = "Seoul"
capitals["jap"] = "Tokyo"
# print the capitals dictionary to see how it changed!

print(capitals)


person = {"first": "Ada", "last": "Lovelace", "age": 42, "is_organ_donor": True}
# Adds a new key value pair for email to person
person["email"] = "alovelace@codingdojo.com"
        
# Changes person's "last" value to "Bobada"
person["last"] = "Bobada"
print(person)


countries_so_far = {"Mexico": 1, "Morocco": 1}
new_visits = ["Albania", "Mexico", "Togo", "Morocco"]
    
# To add Albania to the list
countries_so_far["Albania"] = 1
if "Albania" not in countries_so_far:
    countries_so_far["Albania"] = 1

print(countries_so_far)
# To add 1 to the Mexico tally
if "Mexico" not in countries_so_far:
    countries_so_far["Mexico"] = 1
else : countries_so_far["Mexico"] += 1

print(countries_so_far)

countries_so_far["Mexico"] += 1 # Changes Mexico tally to 2!
# your code here to finish updating your travel log!

my_dict = { "name": "Noelle", "language": "Python" }
for each_key in my_dict:
    print(each_key)
# output: name, language

