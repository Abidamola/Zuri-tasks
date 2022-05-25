# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    with open("story.txt") as f:
     contents = f.read()
    print(contents)


from collections import Counter

def count_word(file_name):
       with open("story.txt") as f: 
                return Counter(f.read().split())

print("Frequency :",count_word("story.txt"))

