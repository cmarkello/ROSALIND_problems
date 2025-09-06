#!/usr/bin/env python3

"""
Script Name: mendel_first_law.py
Description: solves https://rosalind.info/problems/iprb/. Calculate prob of dominant sibling from pairing samples from 3 populations.
Author: Charles Markello (cjmarkello@gmail.com)
Date: 2025-09-05
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
        "-k", "--hom_dom_samples",
        help="Input number of homozygous dominant samples."
    )

    parser.add_argument(
        "-m", "--het_samples",
        help="Input number of heterozygous samples."
    )

    parser.add_argument(
        "-n", "--hom_rec_samples",
        help="Input number of homozygous recessive samples."
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
    k = int(args.hom_dom_samples) #k
    m = int(args.het_samples) #m
    n = int(args.hom_rec_samples) #n

    if args.verbose:
        print(f"DNA string input file: {sequence_file}")

    try:
        #1st sampling
        sample_p1 = (k/(m+n+k)) * ((k-1)/(m+n+k-1))
        sample_p2 = (k/(m+n+k)) * (m/(m+n+k-1))
        sample_p3 = (m / (m + n + k)) * (k / (m + n + k - 1))
        sample_p4 = (k / (m + n + k)) * (n / (m + n + k - 1))
        sample_p5 = (n / (m + n + k)) * (k / (m + n + k - 1))
        sample_p6 = (m / (m + n + k)) * ((m-1) / (m + n + k - 1)) * 3/4
        sample_p7 = (m / (m + n + k)) * (n/ (m + n + k - 1)) * 1 / 2
        sample_p8 = (n / (m + n + k)) * (m / (m + n + k - 1)) * 1 / 2

        k_first_prob = sample_p1 + sample_p2 + sample_p4
        m_first_prob = sample_p3 + sample_p6 + sample_p7
        n_first_prob = sample_p5 + sample_p8

        final_probability = k_first_prob + m_first_prob + n_first_prob

        if args.verbose:
            print("Processing complete.")

        print(f"{final_probability}")

    except Exception as e:
        sys.stderr.write(f"Unexpected error: {e}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
