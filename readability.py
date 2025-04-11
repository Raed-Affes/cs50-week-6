def main():
    text = input("Text: ")

    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    L = letters / words * 100
    S = sentences / words * 100

    index = round(0.0588 * L - 0.296 * S - 15.8)

    if index < 1:
        print("Before Grade 1")
    elif index >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")

def count_letters(text):
    return sum(1 for char in text if char.isalpha())

def count_words(text):
    return len(text.split())

def count_sentences(text):
    return sum(1 for char in text if char in ".!?")

if __name__ == "__main__":
    main()
