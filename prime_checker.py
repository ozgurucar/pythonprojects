number = int(input("Enter number to check if is it prime\n"))
is_prime = True

for i in range(2, number):
    if number % i == 0:
        is_prime = False
if is_prime == True:
    print("Your number is prime")
else:
    print("Your number is not prime.")
