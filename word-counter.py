def count_words(text):
    
    # Splitting the text by spaces to count words
    words = text.split()
    return len(words)

def main():
    # Prompting the user to enter a sentence or paragraph
    user_input = input("Enter a sentence or paragraph: ")
    
    # Error handling for empty input
    if not user_input.strip():
        print("Error: Input cannot be empty. Please enter some text.")
        return
    
    # Counting the number of words in the input
    word_count = count_words(user_input)
    
    # Displaying the word count
    print(f"The number of words in the given text is: {word_count}")

# Ensuring the main function runs when the script is executed
if __name__ == "__main__":
    main()
