#!/usr/bin/env python3
"""
cc_check.py
~~~~~~~~~~~
Python Script to Check for Valid and Invalid Credit Cards

Usage: python3 cc_check.py <card_number>
Example: python3 cc_check.py 378282246310005
"""

import sys

def cc_check():

    # Ensure proper usage
    if len(sys.argv) > 2:
        sys.exit("Usage: cc_check <card_number>")
    if len(sys.argv) == 2:
        given = sys.argv[1]
    if len(sys.argv) == 1:
        given = input("What CC would you like to check: \n")

    # Reject Impossible Lengths
    if len(given) > 16 or len(given) < 13:
        sys.exit("CC must be between 13 and 16 digits long.")

    # Reject Impossible Values
    if given[0] == '0':
        sys.exit("CC cannot start with 0.")

    # Check Given Number
    if cc_check(given):
        print("Valid")
    else:
        print("Invalid")

def cc_check(number):
    """ Given CC Number, Checks to see if Valid Card """
    # Practice Numbers to check: 4012888888881881 and 378282246310005
    # more at https://developer.paypal.com/docs/classic/payflow/payflow-pro/payflow-pro-testing/#credit-card-numbers-for-testing

    prod1, prod2 = 0, 0
    valid_checksum = False

    # Iterate through every other CC Number backwards starting with second to last number
    prod1_start = len(number) - 2
    for i in range(prod1_start, -1, -2):

        doubled = (int(number[i]) * 2)

        if doubled > 9:
            first_digit = doubled // 10
            second_digit = doubled % 10
            prod1 += (first_digit + second_digit)
        else:
            prod1 += doubled

    # Iterate through every other CC Number backwards start with the last number
    prod2_start = len(number) - 1
    for i in range(prod2_start, -1, -2):
        digit = number[i]
        prod2 += int(digit)

    # Evaluate Checksum
    check_sum = prod1 + prod2
    if check_sum % 10 == 0:
        valid_checksum = True
    else:
        return False

    if valid_checksum:
        # MasterCard
        if len(number) == 15 and \
              (number[0] == "3") and \
              (number[1] == "4" or number[1] == "7"):
            return True
        # Amex
        if len(number) == 16 and \
              (number[0] == "5" or number[0] == "2") and \
              (number[1] == "1" or \
               number[1] == "2" or \
               number[1] == "3" or \
               number[1] == "4" or \
               number[1] == "5"):
            return True
        # Visa
        if (len(number) == 16 or len(number) == 13) and number[0] == "4":
            return True
        # Discover
        if len(number) == 16 and number[0] == "6" and number[1] == "0":
            return True
        else:
            return False

if __name__=="__main__":
    cc_check()
