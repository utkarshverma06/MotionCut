def count_words(text):
    words = text.split()
    return len(words)

def main():
    user_input = input("Please enter a sentence or paragraph to count the words: ")
    if not user_input.strip():
        print("Error: Input cannot be empty")
        return

    word_count = count_words(user_input)

    print(f"Total word count: {word_count}")

if __name__ == "__main__":
    main()