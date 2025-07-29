import sys
from stats import word_count
from stats import character_count
from stats import sorting

# Opens the filepath
def get_book_text(filepath):
    with open(filepath) as f:
        open_file = f.read()
        return open_file

# Prints the text
def main():
    text = get_book_text(sys.argv[1])
    result = word_count(text)
    all_characters = character_count(text)
    sorted_list = sorting(all_characters)


    #Report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...") 
    print("----------- Word Count ----------")
    print(f"Found {result} total words")
    print("--------- Character Count -------")
    #Her skal listen inn. Men denne må loopes for å komme på "ny" linje hver gang.
    for dict in sorted_list:
        if dict["char"].isalpha() == True:
            print(f'{dict["char"]}: {dict["num"]}')
    print("============= END ===============")


if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)





main()



