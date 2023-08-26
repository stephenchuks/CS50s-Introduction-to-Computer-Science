def main():
    # Prompt the user for the height of the pyramid
    while True:
        try:
            height = int(input("Height: "))
            if 1 <= height <= 8:
                break
        except ValueError:
            pass

    # Generate the half-pyramid
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        hashes = "#" * i
        print(spaces + hashes)


if __name__ == "__main__":
    main()
