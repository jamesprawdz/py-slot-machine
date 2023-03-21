Slot Machine Game
=================

This is a simple text-based slot machine game implemented in Python. The game allows users to deposit an initial amount of money, bet on a specific number of lines, and spin the slot machine. Winnings are calculated based on the symbols and their respective values.

Features
--------

-   Deposit an initial amount of money
-   Bet on a specific number of lines
-   Spin the slot machine and see the results
-   Calculate winnings based on matching symbols and their values
-   Play multiple rounds and track the user's balance

How to run
----------

Ensure you have Python 3.8+ installed on your machine. Run the game using the following command:

`python main.py`

Game Instructions
-----------------

    1.  Deposit an initial amount of money.
    2.  Choose the number of lines you want to bet on (1 to 3).
    3.  Enter the amount you want to bet on each line.
    4.  Press enter to spin the slot machine and see the results.
    5.  Continue playing by pressing enter or quit the game by entering 'q'.
    6.  When you quit the game, your final balance will be displayed.

Code Explanation
----------------

The code consists of several functions that handle different aspects of the game:

-   `get_all_symbols`: Creates a list of all symbols based on their count.
-   `check_winnings`: Calculates the winnings and winning lines based on the slot machine spin.
-   `get_slot_machine_spin`: Generates a random spin of the slot machine.
-   `print_slot_machine`: Prints the current state of the slot machine.
-   `get_positive_integer_input`: Gets a positive integer input from the user.
-   `deposit`: Gets the deposit amount from the user.
-   `get_number_of_lines`: Gets the number of lines to bet on from the user.
-   `get_bet`: Gets the bet amount for each line from the user.
-   `spin`: Performs a single spin of the slot machine and updates the user's balance.
-   `main`: Controls the game flow, including user input and game logic.

Customization
-------------

To customize the game, you can modify the global constants, symbol count, and symbol values at the beginning of the code:

```
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

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}
```
Adjust these values to change the game's difficulty, payouts, and the slot machine's configuration.
