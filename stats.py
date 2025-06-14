def number_of_text(string):
    text_list = string.split()
    counter = 0

    for text in text_list:
        counter += 1
     
    return counter

def unique_character_count(my_list):
    # Takes a list of strings
    characters = [char.lower() for char in my_list if char.isalpha()]
    char_count = {}
    for char in characters:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

        # Make a list of dicts
        results = []
        for char, count in char_count.items():
            results.append({
                "char": char,
                "num" : count
            })

    return results

    # print(f"This are the characters: {characters}")

def sort_on(results):
    return results["num"]
