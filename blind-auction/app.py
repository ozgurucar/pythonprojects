from art import logo

print(logo)

want_continue = "true"
names = []
bids = []

while want_continue == "true":
    name = input("What is your name ?: ")
    price = int(input("What is your bid? $: "))
    names.append(name)
    bids.append(price)
    want_continue = input("If there is another player please write 'true' ").lower()

max_value = 0
index = -1
for i in range(len(bids)):
    if bids[i] > max_value:
        max_value = bids[i]
        index = i

print(f"The winner is {names[index]}, and whose bid is: {bids[index]}$")
