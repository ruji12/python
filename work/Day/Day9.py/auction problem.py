
print("Welcome to the secret auction program")
bid={}

bidding_finished=False
def find_highest_number(bids):
    highest_amount=0
    for bidder in bids:
        bidder_amount=bids[bidder]
        if bidder_amount>highest_amount:
            highest_amount=bidder_amount
            winner=bidder
    print(f" the winner is {winner} with ${highest_amount}")        


while not bidding_finished:
    name=input("what is your name?:")
    price=int(input("what's your bid?:&"))
    bid[name]=price
    check=input("Are there other bidders?Type 'yes' or 'no'.")
    if check=='no':
        bidding_finished=True
        find_highest_number(bid)

    elif check=='yes':
        print(" go ahead")
