import random

# constant global values
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
# multipliers for each symbol
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        # first symbol we want to check is in the first column of whatever row
        symbol = columns[0][line]
        # loop thru every column and check for that symbol
        for column in columns:
            # check at column of current row
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                # if symbol is not the same as previous symbol then break
                break
        # if they are the same symbol, dont break and give them their winnings
        else:
            # multiplier for that symbol * bet on each line
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    # define colums list
    columns = []
    # generate a column for every column present
    for _ in range(cols):
        column = []
        # copy all_symbols so that symbols arent taken away from main list
        current_symbols = all_symbols[:]
        # loop thru # of values we need to generate which is = to # of rows
        for _ in range(rows):
            # first value will be random symbol for copied list of symbols
            value = random.choice(current_symbols)
            # remove that picked value from list so we cannot pick it again
            current_symbols.remove(value)
            # add value to our column
            column.append(value)
        # add column to empty columns list
        columns.append(column)

    return columns


def print_slot_machine(columns):
    # transposing
    for row in range(len(columns[0])):
        # gives index as you loop thru as well as the item
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        # print a new line character after each row is printed
        print()


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        # check if amount is actually a  + number
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount


def get_number_of_lines():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines


def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        # check if amount is actually a  + number
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount your current balance is: ${balance}")
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    # unpack operator
    print(f"You won on lines:", *winning_lines)
    # tell us how much player won or lost
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is: ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            # this break will end game
            break
        balance += spin(balance)

    print(f"You left with: ${balance}")


main()
