import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma.\n")
names = names_string.split(", ")

# # Get the total number of items in list
# num_items = (len(names))
# # Generate random numbers between 0 and the last index.
# random_choice = random.randint(0, num_items - 1)
# person_who_will_pay = names[random_choice]

person_who_will_pay = random.choice(names)
print(person_who_will_pay + " is going to buy the meail today")
