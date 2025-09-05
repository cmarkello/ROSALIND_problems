#!/usr/bin/env python3

"""
Script Name: comp_hamm_dist.py
Description: solves https://rosalind.info/problems/hamm/. Calculate hamming distance between a pair of sequences.
Author: Charles Markello (cjmarkello@gmail.com)
Date: 2025-09-04
"""

import argparse
import sys


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Takes in sequences of DNA and calculates the hamming distance between them."
    )

    # Input DNA string
    parser.add_argument(
        "-f", "--sequence_file",
        help="Input file containing sequences of DNA."
    )

    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output."
    )

    return parser.parse_args()

def compute_hamm_dist(seq_A: str, seq_B: str, verbose: bool) -> int:

    if verbose:
        print(f"Computing hamming distance between {seq_A} and {seq_B}")

    hamm_dist = 0

    for idx in range(len(seq_A)):
        if seq_A[idx] != seq_B[idx]:
            hamm_dist += 1

    return hamm_dist

def main():
    """Main script logic."""
    args = parse_args()
    sequence_file = args.sequence_file

    if args.verbose:
        print(f"DNA string input file: {sequence_file}")

    try:

        seq_A, seq_B = "", ""

        with open(sequence_file, "r") as seq_file:
            seq_A = seq_file.readline().strip()
            seq_B = seq_file.readline().strip()

        hamm_dist = compute_hamm_dist(seq_A, seq_B, args.verbose)

        if args.verbose:
            print("Processing complete.")

        print(f"{hamm_dist}")

    except Exception as e:
        sys.stderr.write(f"Unexpected error: {e}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
