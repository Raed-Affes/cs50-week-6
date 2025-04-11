import csv
import sys

def main():

    # Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py database.csv sequence.txt")
        sys.exit(1)

    # Read database file into a variable
    database_file = sys.argv[1]
    with open(database_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        database = list(reader)

    # Read DNA sequence file into a variable
    sequence_file = sys.argv[2]
    with open(sequence_file, 'r') as file:
        sequence = file.read().strip()

    # Find longest match of each STR in DNA sequence
    str_matches = {}
    for str in database[0].keys():
        if str != "name":
            str_matches[str] = longest_match(sequence, str)

    # Check database for matching profiles
    for person in database:
        match = True
        for str in str_matches:
            if int(person[str]) != str_matches[str]:
                match = False
                break
        if match:
            print(person["name"])
            return

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

    # After checking for runs at each character in sequence, return longest run found
    return longest_run


if __name__ == "__main__":
    main()
