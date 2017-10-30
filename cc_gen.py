"""
cc_gen.py
~~~~~~~~~~~
Python Script to Generate Valid Credit Card Numbers using cc_check.py
Generates up to max_amount Valid Cards

Usage: python cc_gen.py <card_type>
Usage: python cc_gen.py <card_type> 100

Example: python cc_gen.py Visa
Example: python cc_gen.py MasterCard 100

"""

import sys
from random import randint
from cc_check import cc_check

def cc_gen():
    """ Generates Valid Credit Cards Numbers """
    max_amount = 10
    Valid_Cards = []

    # Ensure Proper Usage
    if len(sys.argv) > 3:
        sys.exit("Usage: cc_gen.py <card_type> <quantity(optional)")
    if len(sys.argv) == 3:
        given = sys.argv[1]
        max_amount = int(sys.argv[2])
        if max_amount > 1000:
            sys.exit("Limit set to 1000 to prevent system hanging")
    if len(sys.argv) == 2:
        given = sys.argv[1]
        max_amount = max_amount
    if len(sys.argv) == 1:
        given = input("Would you like an AMEX, Discover, Visa, or MasterCard: ")
        max_amount = max_amount

    # Reject Invalid Card Types
    card_types = ["visa", "amex", "discover", "mastercard"]
    if given.lower() not in card_types:
        sys.exit("Card Type {} not found".format(given))

    # Generate Visa Card
    if given.lower() == "visa":
        card_start = 4
        card_length = 16  # can be set to 13 or 16

    # Generate AMEX Card
    if given.lower() == "amex":
        card_start = 3
        card_length = 15

    # Generate Discover Card
    if given.lower() == "discover":
        card_start = 6
        card_length = 16

    # Generate MasterCard
    if given.lower() == "mastercard":
        card_start = 5
        card_length = 16

    # Generate Numbers until Valid_Cards reaches Max_Amount
    while len(Valid_Cards) < max_amount:

        random_card = generate_number(card_start, card_length)

        # If Card is Valid And not apart of Valid_Cards
        if cc_check(random_card) and random_card not in Valid_Cards:

            # Add to Valid Cards
            print("Valid {} Generated: {}".format(given, random_card))
            Valid_Cards.append(random_card)

    # Write out to file
    # Can be set to "w" to reset file each run or "a" to append results each run
    filename = given.lower()+"_numbers.txt"
    with open(filename, "w") as f:
        for number in Valid_Cards:
            print(number, file=f)

def generate_number(start_int, length):
    """ Generates a number that starts with start_int and is length long """

    numbers = []
    numbers.append(start_int)

    for i in range(0, length-1):
        numbers.append(randint(0, 9))

    result = "".join(str(i) for i in numbers)
    return result

if __name__ == "__main__":
    cc_gen()
