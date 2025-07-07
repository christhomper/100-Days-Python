from art import logo

# Display ASCII logo and welcome message
print(logo)
print("Welcome to the silent auction program\n")

# Function to determine the highest bidder
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"\nThe winner is {winner} with a bid of ${highest_bid}.")

# Main bidding loop
bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?\n")
    price = int(input("What is your bid?\n$"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        # Clear screen between bidders (simulate privacy)
        print("\n" * 100)












