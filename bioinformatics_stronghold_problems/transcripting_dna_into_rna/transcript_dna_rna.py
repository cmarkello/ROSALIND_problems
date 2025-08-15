#!/usr/bin/env python3

"""
Script Name: transcript_dna_rna.py
Description: solves https://rosalind.info/problems/rna/. Convert a DNA string to an RNA string.
Author: Charles Markello (cjmarkello@gmail.com)
Date: 2025-08-15
"""

import argparse
import sys


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Takes in a DNA string and converts it to an RNA string."
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

        rna_string = ''

        # Go through and convert each character in the DNA string to RNA and add to final RNA string
        for nucleotide in dna_string:
            if nucleotide == 'T':
                rna_string += 'U'
            else:
                rna_string += nucleotide

        if args.verbose:
            print("Processing complete.")

        print(f"{rna_string}")

    except Exception as e:
        sys.stderr.write(f"Unexpected error: {e}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
