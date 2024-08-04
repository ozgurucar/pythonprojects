import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play_again = "yes"
while play_again == "yes":
    user_hand = []
    dealer_hand = []
    total_of_user = 0
    total_of_dealer = 0


    def deal_card():
        random_number = random.choice(cards)
        return random_number


    for i in range(2):
        user_hand.append(deal_card())
        dealer_hand.append(deal_card())


    def calculate_user():
        total = 0
        for x in range(len(user_hand)):
            total += user_hand[x]
        if total > 21 and user_hand[x] == 11:
            user_hand[x] = 1
            return calculate_user()
        return total


    total_of_user = calculate_user()
    want_continue = "y"
    while total_of_user < 21 and want_continue == "y":
        want_continue = input(
            f"Dealer's hand is : [{dealer_hand[0]}, X], and your hand is : {user_hand},  less than 21 do you want to "
            f"deal new card ? [y/n]").lower()
        if want_continue == "y":
            user_hand.append(deal_card())
            total_of_user = calculate_user()


    def calculate_dealer():
        total = 0
        for x in range(len(dealer_hand)):
            total += dealer_hand[x]
        if total > 21 and dealer_hand[x] == 11:
            dealer_hand[x] = 1
            return calculate_dealer()
        return total


    total_of_dealer = calculate_dealer()

    while total_of_dealer < 17:
        dealer_hand.append(deal_card())
        total_of_dealer = calculate_dealer()


    def find_winner():
        print(f"Your hand: {user_hand}, Dealer hand: {dealer_hand}")
        if total_of_user > 21:
            print(f"You Lost, your hand is over 21!")
        elif total_of_dealer > 21:
            print("You won, dealer's hand is over 21!")
        else:
            if total_of_user == total_of_dealer:
                print("Draw!")
            elif total_of_user > total_of_dealer:
                print("You Won!")
            elif total_of_dealer > total_of_user:
                print("You Lost!")


    find_winner()
    play_again = input("If yo want to play again write : 'yes': ")

print("Thanks for playing :)")
