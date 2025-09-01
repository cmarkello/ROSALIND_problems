#!/usr/bin/env python3

"""
Script Name: rev_comp_dna.py
Description: solves https://rosalind.info/problems/revc/. Reverse compliment a DNA string.
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

    # Input DNA string
    parser.add_argument(
        "-s", "--dna_string",
        help="Input sequence of DNA string"
    )

    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output."
    )

    return parser.parse_args()


def main():
    """Main script logic."""
    args = parse_args()
    dna_string = args.dna_string

    if args.verbose:
        print(f"DNA string input: {dna_string}")

    try:

        rev_comp = ''

        # Go through and convert each character in the DNA string to RNA and add to final RNA string
        for nucleotide in dna_string:
            match nucleotide:
                case "A":
                    rev_comp = 'T' + rev_comp
                case "C":
                    rev_comp = 'G' + rev_comp
                case "G":
                    rev_comp = 'C' + rev_comp
                case "T":
                    rev_comp = 'A' + rev_comp


        if args.verbose:
            print("Processing complete.")

        print(f"{rev_comp}")

    except Exception as e:
        sys.stderr.write(f"Unexpected error: {e}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
