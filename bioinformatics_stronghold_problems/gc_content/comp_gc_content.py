#!/usr/bin/env python3

"""
Script Name: comp_gc_content.py
Description: solves https://rosalind.info/problems/gc/. Calculate GC content percentage from a list of sequences.
Author: Charles Markello (cjmarkello@gmail.com)
Date: 2025-09-04
"""

import argparse
import sys


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Takes in a FASTA file and calculates and finds the sequence with the largest percentage of GC content."
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

def compute_gc_content(nucleotide_sequence: str, tmp_seq_id: str, largest_gc_seq_percent: float, largest_gc_seq_id: str, verbose: bool) -> (float, str):

    if verbose:
        print(f"Computing GC content for {tmp_seq_id}: {nucleotide_sequence}")

    gc_count = 0.0
    for nucleotide in nucleotide_sequence:
        if nucleotide in ("G", "C"):
            gc_count += 1.0

    gc_seq_percent = (gc_count / float(len(nucleotide_sequence)))
    if gc_seq_percent > largest_gc_seq_percent:
        largest_gc_seq_percent = gc_seq_percent
        largest_gc_seq_id = tmp_seq_id

    return largest_gc_seq_percent, largest_gc_seq_id

def main():
    """Main script logic."""
    args = parse_args()
    sequence_file = args.sequence_file

    if args.verbose:
        print(f"DNA string input file: {sequence_file}")

    try:
        current_seq_id = ""
        current_seq = ""
        largest_gc_seq_id = ""
        largest_gc_seq_percent = 0.0

        with open(sequence_file, 'r') as seq_file:
            for line in seq_file:
                if ">" in line:
                    # If found a seq id line and there was already a sequence gathered, calculate gc content
                    if current_seq_id != "":
                        largest_gc_seq_percent, largest_gc_seq_id = compute_gc_content(current_seq, current_seq_id,
                                                                                   largest_gc_seq_percent,
                                                                                   largest_gc_seq_id, args.verbose)
                    current_seq_id = line.strip().split(">")[1]
                    current_seq = ""
                else:
                    # gather sequence
                    current_seq += line.strip()

            largest_gc_seq_percent, largest_gc_seq_id = compute_gc_content(current_seq, current_seq_id, largest_gc_seq_percent, largest_gc_seq_id, args.verbose)

        if args.verbose:
            print("Processing complete.")

        print(f"{largest_gc_seq_id}\n{largest_gc_seq_percent}")

    except Exception as e:
        sys.stderr.write(f"Unexpected error: {e}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
