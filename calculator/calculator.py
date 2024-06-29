from art import logo

print(logo)


def calculator():
    first_number = float(input("Enter the first number: "))
    operator = input("Select operator : { + - * / }: ")
    second_number = float(input("Enter the second number: "))

    def operation(first_number, operator, second_number):
        if operator == '+':
            return first_number + second_number
        if operator == '-':
            return first_number - second_number
        if operator == '*':
            return first_number * second_number
        if operator == '/':
            return first_number / second_number

    result = operation(first_number, operator, second_number)
    # For using same result as value
    continue_w_same = input(f'Result is {result} do you want to use it again, yes or no: ').lower()
    while continue_w_same == "yes":
        first_number = result
        operator = input("Select operator : { + - * / }: ")
        second_number = int(input("Enter the second number: "))
        result = operation(first_number, operator, second_number)
        continue_w_same = input(f'Result is {result} do you want to use it again, yes or no: ').lower()
    calculator()


calculator()
