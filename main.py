from stats import number_of_text, unique_character_count,sort_on
import sys

def get_book_text(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: File not found at {file_path}"
    except Exception as e:
        return f"Error: {str(e)}"
      
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    num_words = number_of_text(book_text)

    # print(f"{num_words} words found in the document")
    # print(f"This are all the characters individually: {char}")
    char_dict = unique_character_count(book_text)    
    #print(f"This is the dictionary: {char_dict}")

    char_dict.sort(reverse=True, key=sort_on)
    #print(f"This is: {char_dict}")
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for item in char_dict:
        print(f"{item['char']}: {item['num']}")
    
    print("============= END ===============")

if __name__ == "__main__":
    main()