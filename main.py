def main():
    with open("/Users/samgeyer/code/workspace/github/yesworm/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
    create_report(file_contents)

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(dict):
    return dict["num"]

def create_report(text):
    word_count = count_words(text)
    char_count = count_characters(text)

    char_list = [{"char": char, "num": count} for char, count in char_count.items()]
    
    char_list.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print()
    for char_dict in char_list:
        if char_dict["char"].isalpha():
            print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")

if __name__ == "__main__":
    main()