with open("books/frankenstein.txt") as f:
    file_contents = f.read()
   

def word_count(text):
    words = text.split()
    return(len(words))
print(word_count(file_contents))

def character_count(file_contents):
    char_counts = {}
    for char in file_contents:

        lower_char = char.lower()
        if lower_char.isalpha():
            if lower_char in char_counts:
                char_counts[lower_char] += 1
            else:
                char_counts[lower_char] = 1
    return char_counts
print(character_count(file_contents))

word_count = word_count(file_contents)
char_counts = character_count(file_contents)

char_list = []
for char, count in char_counts.items():
    char_dict ={
        "char": char,
        "num":count
    }
    char_list.append(char_dict)

def sort_on(dict):
    return dict["num"]
char_list.sort(reverse=True, key=sort_on)
print("--- Begin report of books/frankenstein.txt ---")
print(f"{word_count} words found in the document\n")
for char_dict in char_list:
    print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")
print("--- End report ---")




