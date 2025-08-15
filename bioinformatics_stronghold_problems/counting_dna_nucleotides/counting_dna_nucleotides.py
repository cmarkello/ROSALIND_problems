#!/usr/bin/env python3

"""
Script Name: counting_dna_nucleotides.py
Description: solves https://rosalind.info/problems/dna/. Count a list of nucleotides within a DNA string.
Author: Charles Markello (cjmarkello@gmail.com)
Date: 2025-08-15
"""

import argparse
import sys


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Takes in a DNA string and counts the number of A, C, G, and Ts and outputs a count for each."
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

        nucleotide_count = {"A": 0, "C": 0, "G": 0, "T": 0}

        # Go through and count the number of A, C, G, and Ts
        for nucleotide in dna_string:
            match nucleotide:
                case "A":
                    nucleotide_count["A"] += 1
                case "C":
                    nucleotide_count["C"] += 1
                case "G":
                    nucleotide_count["G"] += 1
                case "T":
                    nucleotide_count["T"] += 1

        if args.verbose:
            print("Processing complete.")

        print(f"{nucleotide_count['A']} {nucleotide_count['C']} {nucleotide_count['G']} {nucleotide_count['T']}")

    except Exception as e:
        sys.stderr.write(f"Unexpected error: {e}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
