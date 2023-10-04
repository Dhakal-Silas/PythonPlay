import random
import asyncio

MAX_LINES = 4
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 4
#Symbols used for cards
symbol_count = {
    "A": 4,
    "K": 4,
    "Q": 4,
    "J": 4,
    "10": 4,
    "9": 4,
    "8": 4,
    "7": 4,
    "6": 4,
    "5": 4,
    "4": 4,
    "3": 4,
    "2": 4

}
#Symbols used for cards with respective values
symbol_value = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "10": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2
}

# to check which line of card has won
def check_winnings(columns, lines, symbol_value):

    points = []
    for row in range(len(columns)):
        total_point = 0
        for item in columns[row]:
            for symbol in symbol_value:
                if item == symbol:
                    point = symbol_value[symbol]

            total_point += point
        points.append(total_point)
    check_win_line= points.index(max(points))
    if (check_win_line)+1 == lines:
        
        return True
    else:
        print(f"The card line {check_win_line+1} won ")
        return False

#to get all random cards in form of rows and columns
def get_all_cards(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

#to display all cards that is returned by above function
async def display_cards(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
                await asyncio.sleep(0.5)
            else:
                print(column[row], end="")
                
        print()

#to get the bet amount
def get_bet():
    while True:
        amount = input("How much do you want to bet?$")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("please enter a number.")
    return amount

# to get the card line to put on a bet
def get_card_line():
    while True:
        lines = input(
            "Enter the number of card stack to bet on (1- "+str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number.")
    return lines

# to get the total deposit amount
def deposit():
    while True:
        amount = input("what would you like to deposit?$")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("please enter a number.")
    return amount

# to distribute card in each line, it calls get_card and display_card function
def distribute_card(balance):
    lines = get_card_line()
    while True:
        total_bet = get_bet()
        if total_bet > balance:
            print(
                f"you do not have enough to bet that amount, your current balance is:${balance}")
        else:
            break

    print(
        f"You are betting on {lines} card stack. Your bet is equal to : ${total_bet}")
    slots = get_all_cards(ROWS, COLS, symbol_count)
    asyncio.run(display_cards(slots))
    if check_winnings(slots, lines, symbol_value):
        print(f"You won ${total_bet}.")
        return total_bet
    else:
        print(f"You lost ${total_bet}")
        return - total_bet

#main function prompts and calls distribute_card function
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += distribute_card(balance)
    print(f"you left with ${balance}")


main()
