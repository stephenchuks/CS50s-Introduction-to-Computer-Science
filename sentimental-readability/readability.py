from cs50 import get_string


def main():
    text = get_string("Text: ")
    letters = num_letters(text)
    words = num_words(text)
    sentences = num_sentences(text)

    L = (letters / words) * 100
    S = (sentences / words) * 100

    index = 0.0588 * L - 0.296 * S - 15.8

    grade_level = round(index)

    if grade_level >= 16:
        print("Grade 16+")
    elif grade_level < 1:
        print("Before Grade 1")
    else:
        print(f"Grade {grade_level}")


def num_letters(text):
    count = 0
    for char in text:
        if char.isalpha():
            count += 1
    return count


def num_words(text):
    count = 1  # Start with 1 because the first word is counted
    for char in text:
        if char == " ":
            count += 1
    return count


def num_sentences(text):
    count = 0
    for char in text:
        if char in [".", "!", "?"]:
            count += 1
    return count


if __name__ == "__main__":
    main()
