import random

names = input("Enter names separated by ',': ")
names = names.split(", ")
print(names[random.randint(0, len(names) - 1)] + " will pay the bill!")

