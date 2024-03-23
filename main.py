with open("books/frankenstein.txt") as f:
    file_contents = f.read()


def wc(book):
    words = book.split()
    word_count = len(words)
    return word_count

def lc(letters):
    abcds = "abcdefghijklmnopqrstuvwxyz"
    letter_count = {}
    strings = letters.lower()
    letters_split = strings.split()
    letters_joined = "".join(letters_split)
    for l in letters_joined:
        if l not in letter_count and l in abcds:
            letter_count[l] = 1
        elif l in letter_count and l in abcds:
            letter_count[l] += 1
    return letter_count

        
word_count = wc(file_contents)
letter_conut = lc(file_contents)

list_of_letters = []
for key, value in letter_conut.items():
    list_of_letters.append({"letter":key, "count": value})

def sort_on(dict):
    return dict["count"]

list_of_letters.sort(reverse=True,key=sort_on)

print("begin report of books/frankenstein")
print(f"{word_count} words found in the document")
for l_c in list_of_letters:
        print(f"The \'{l_c["letter"]}\' character was found {l_c["count"]} ") 
