from blind_auction_art import logo
import os

# start
print(logo)

should_continue = True

bid_dict = {}

# input part
while should_continue:
    name = input("What is your name:\n")
    bid = int(input("How much you will bid:\n"))
    bid_dict[name] = bid
    if input("type \"yes\" to continue or \"no\" to end:\n").lower() == "no":
        should_continue = False
    os.system("clear")

# calcu part
winner_name = ""
winner_bid = 0
for key in bid_dict:
    price = bid_dict[key]
    if price > winner_bid:
        winner_bid = price
        winner_name = key