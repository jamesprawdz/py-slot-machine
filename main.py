# Import the random module for generating random numbers and choices.
import random

# Define global constants for the game.
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

# Define the count of each symbol and their respective values (multipliers).
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

# Function to create a list of all symbols based on their count.
def get_all_symbols(symbols):
    return [symbol for symbol, count in symbols.items() for _ in range(count)]

# Function to calculate the winnings and winning lines based on the slot machine spin.
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []

    # Loop through each line.
    for line in range(lines):
        # Get the first symbol in the current line.
        symbol = columns[0][line]

        # Check if the current symbol matches all symbols in the line.
        for column in columns:
            if symbol != column[line]:
                break
        else:
            # If all symbols match, calculate the winnings and store the winning line.
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

# Function to generate a random spin of the slot machine.
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = get_all_symbols(symbols)
    # Generate the slot machine columns with random symbols.
    return [[random.choice(symbols := [s for s in symbols if s != symbol]) for _ in range(rows)] for symbol in all_symbols[:cols]]

# Function to print the current state of the slot machine.
def print_slot_machine(columns):
    for row in zip(*columns):
        print(" | ".join(row))

# Function to get a positive integer input from the user.
def get_positive_integer_input(prompt):
    while True:
        value = input(prompt)
        if value.isdigit() and (num := int(value)) > 0:
            return num
        print("Please enter a positive number.")

# Function to get the deposit amount from the user.
def deposit():
    return get_positive_integer_input("What would you like to deposit? $")

# Function to get the number of lines to bet on from the user.
def get_number_of_lines():
    return get_positive_integer_input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")

# Function to get the bet amount for each line from the user.
def get_bet():
    return get_positive_integer_input(f"What would you like to bet on each line? (${MIN_BET}-${MAX_BET}): ")

# Function to perform a single spin of the slot machine and update the user's balance.
def spin(balance):
    lines = get_number_of_lines()

    # Ensure the user has enough balance to make the bet.
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet <= balance:
            break
        print(
            f"You do not have enough to bet that amount. Your current balance is: ${balance}")
        # Print the bet information.
    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    # Generate the slot machine spin and print the result.
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

    # Calculate the winnings and winning lines based on the spin.
    winnings, winning_lines = check_winnings(
        slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)

    # Return the net change in the user's balance after the spin.
    return winnings - total_bet


# Main function to control the game flow.
def main():
    # Get the initial deposit from the user.
    balance = deposit()
    # Continue playing until the user decides to quit.
    while True:
        print(f"Current balance is: ${balance}")
        if input("Press enter to play (q to quit).") == "q":
            break
        # Update the user's balance after each spin.
        balance += spin(balance)

    # Print the final balance when the user quits.
    print(f"You left with: ${balance}")


# Start the game.
main()
