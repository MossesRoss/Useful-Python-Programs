def load_file(filename):
    with open(filename, 'r') as file:
        text = file.read()
    return text

def find_similar_words(text):
    words = text.split()
    unique_words = set(words)
    similar_words = {}

    for word in unique_words:
        similar_words[word] = [w for w in words if w.lower() == word.lower()]

    return similar_words

def main():
    filename = input("Enter the filename: ")
    text = load_file(filename)
    similar_words = find_similar_words(text)

    for word, occurrences in similar_words.items():
        if len(occurrences) > 1:
            print(f"{word}: {len(occurrences)} occurrences - {occurrences}")

if __name__ == "__main__":
    main()
