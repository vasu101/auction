from os import system
from art import logo
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
print(logo)

dict = {}
play = 'yes'
while play == 'yes':
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    dict[name] = bid
    play = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if play == 'yes':
        clear()

max_key = 0
for key in dict:
    if dict[key] > max_key:
        max_key = dict[key]
        winner = key
print(f"The winner is {winner} with a bid of ${max_key}")
  





