def count_words_in_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

if __name__ == "__main__":
    filename = "words.txt" 
    word_count = count_words_in_file(filename)
    print(f"Total number of words in '{filename}': {word_count}")