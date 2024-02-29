# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
total_steps = nr_letters + nr_numbers + nr_symbols
char_list = []
number_list = []
if nr_letters >= 0 and nr_symbols >= 0 and nr_numbers >= 0:
    for n in range(0, total_steps):
        number_list.append(n)
        char_list.append('')


    def getrandomnumber():
        rand_number = number_list[random.randint(0, number_list.__len__() - 1)]
        number_list.remove(rand_number)
        return rand_number


    def getrandomvalue(list):
        random_value = list[random.randint(0, list.__len__() - 1)]
        return random_value


    for n in range(0, nr_letters):
        char_list[getrandomnumber()] = getrandomvalue(letters)

    for n in range(0, nr_symbols):
        char_list[getrandomnumber()] = getrandomvalue(symbols)

    for n in range(0, nr_numbers):
        char_list[getrandomnumber()] = getrandomvalue(numbers)

    final_string = ""
    for n in range(0,char_list.__len__()-1):
        final_string += char_list[n]
    print("Generated Password: " + final_string)

else:
    print("Out of range!")