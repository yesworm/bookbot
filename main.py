def main():
    with open("/Users/samgeyer/code/workspace/github/yesworm/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

def count_words():
    with open("/Users/samgeyer/code/workspace/github/yesworm/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        word_count = len(words)

        print(word_count)


main()
count_words() 
    
    # ...