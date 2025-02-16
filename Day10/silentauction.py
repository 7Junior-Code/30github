

def winner_bids(bidding_records):
    record_bid = 0
    winner = ""
    for bidder in bidding_records:
        bid_price = bidding_records[bidder]
        if bid_price > record_bid:
            record_bid = bid_price
            winner = bidder
    print(f"The winner is {winner} with a bid of {record_bid}!")


bids = {}
keep_bidding = True
while keep_bidding:
    name = input("What's your name:\n ")
    try:
        user_bid = int(input("Enter your bid:\n "))
    except ValueError:
        print("Error a number was supposed to be entered")
    finally:
        keep_bidding = False
    bids[name] = user_bid
    next_bidders = input("Are there any other bidders? enter 'yes' or 'no':\n ").lower()

    if next_bidders == 'yes':
        print("\n" * 35)
    elif next_bidders == 'no':
        next_bidders = False
        winner_bids(bids)
    else:
        print("Error")
