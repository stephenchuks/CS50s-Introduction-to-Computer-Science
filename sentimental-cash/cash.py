from cs50 import get_float


def main():
    # Get the user's input for change owed
    while True:
        change_owed = get_float("Change owed: ")
        if change_owed >= 0:
            break

    # Convert change owed to cents
    cents = round(change_owed * 100)

    # Calculate the minimum number of coins required
    coins = 0
    coins += cents // 25  # Quarters
    cents %= 25
    coins += cents // 10  # Dimes
    cents %= 10
    coins += cents // 5  # Nickels
    cents %= 5
    coins += cents  # Pennies

    # Print the minimum number of coins
    print(coins)


if __name__ == "__main__":
    main()
