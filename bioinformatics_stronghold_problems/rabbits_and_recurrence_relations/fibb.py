#!/usr/bin/env python3

"""
Script Name: fibb.py
Description: solves https://rosalind.info/problems/fib/. Find the number of rabbit pairs after n months with rabbit birth rate k.
Author: Charles Markello (cjmarkello@gmail.com)
Date: 2025-09-1
"""

import argparse
import sys


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Takes in a DNA string to reverse compliment."
    )

    # Input number of months rabbits will breed
    parser.add_argument(
        "-n", "--num_months",
        help="Number of months"
    )

    # Rabbit offspring rate
    parser.add_argument(
        "-k", "--rabbit_rate",
        help="Number of pairs of rabbits born every generation"
    )

    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output."
    )

    return parser.parse_args()

def count_rabbits(num_months: int, rabbit_rate: int, verbose: bool ):

    if num_months == 1 or num_months == 2:
        total_rabbits = 1
    else:
        total_rabbits = count_rabbits(num_months - 1, rabbit_rate, verbose) + rabbit_rate * count_rabbits(num_months - 2, rabbit_rate, verbose)

    if verbose:
        print(f"month: {num_months}, total_rabbits: {total_rabbits}")

    return total_rabbits


def main():
    """Main script logic."""
    args = parse_args()
    num_months = args.num_months
    rabbit_rate = args.rabbit_rate

    if args.verbose:
        print(f"Input number of months: {num_months}, rabit birth rate: {rabbit_rate}")

    try:

        # Go through and count up the total number of rabbit pairs
        total_num_rabbit_pairs = count_rabbits(int(num_months), int(rabbit_rate), args.verbose)

        if args.verbose:
            print("Processing complete.")

        print(f"{total_num_rabbit_pairs}")

    except Exception as e:
        sys.stderr.write(f"Unexpected error: {e}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
