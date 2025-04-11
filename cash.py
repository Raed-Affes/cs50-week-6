def main():
    # Prompt user for change owed
    while True:
        try:
            dollars = float(input("Change owed: "))
            if dollars >= 0:
                break
        except ValueError:
            continue

    # Convert dollars to cents
    cents = round(dollars * 100)

    # Initialize coin counter
    coins = 0

    # Calculate number of quarters
    coins += cents // 25
    cents %= 25

    # Calculate number of dimes
    coins += cents // 10
    cents %= 10

    # Calculate number of nickels
    coins += cents // 5
    cents %= 5

    # Calculate number of pennies
    coins += cents

    # Print total number of coins
    print(coins)

if __name__ == "__main__":
    main()
