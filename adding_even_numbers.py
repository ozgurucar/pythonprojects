total_of_even_numbers = 0
input_number = int(input("Enter range 0 to 1000: "))
if 0 <= input_number <= 1000:
    for i in range(input_number+1):
        if i % 2 == 0:
            total_of_even_numbers += i
    print(total_of_even_numbers)
else:
    print("Invalid range")
