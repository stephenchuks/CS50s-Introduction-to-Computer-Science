import csv
import sys


def main():
    # Check for correct command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)

    # Get filenames from command-line arguments
    database_file = sys.argv[1]
    sequence_file = sys.argv[2]

    # Read database file into a dictionary
    database = {}
    with open(database_file, "r") as db_file:
        reader = csv.DictReader(db_file)
        for row in reader:
            database[row["name"]] = {k: int(v) for k, v in row.items() if k != "name"}

    # Read DNA sequence file into a variable
    with open(sequence_file, "r") as seq_file:
        sequence = seq_file.read()

    # Initialize dictionary to keep track of STR counts
    str_counts = {k: 0 for k in database[list(database.keys())[0]]}

    # Find longest match of each STR in DNA sequence
    for str_name in str_counts:
        str_counts[str_name] = longest_match(sequence, str_name)

    # Check database for matching profiles
    for name, profile in database.items():
        if profile == str_counts:
            print(name)
            return

    # If no match found
    print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:
            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
