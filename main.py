def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
        words = file_contents.split()
        num_words = len(words)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{num_words} words found in the document")
        print("")
        characters(file_contents)
        print("--- End report ---")

def characters(book_copy):
    char_count = {}
    list_of_dicts = []
    text = book_copy.lower()
    for char in text:
        if char.isalpha():
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1
    
    for char, count in char_count.items():
        list_of_dicts.append({'char': char, 'num': count})
    
    list_of_dicts.sort(reverse=True, key=sort_on)
    
    for item in list_of_dicts:
        char = item["char"]
        num = item["num"]
        print(f"The '{char}' character was found {num} times")

    
def sort_on(dict):
    return dict["num"]

main()