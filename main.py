def read_frankenstein(): 
	with open("books/frankenstein.txt") as f:
		file_contents = f.read()
	return file_contents

def count_words(file_contents): 
	words = file_contents.split()
	return len(words) 

def count_characters(file_contents):
	character_count = {}
	for char in file_contents:
        	lower_char = char.lower()
        	character_count[lower_char] = character_count.get(lower_char, 0) + 1
	return character_count

if __name__ == "__main__":
    file_contents = read_frankenstein()
    num_words = count_words(file_contents)
    character_counts = count_characters(file_contents)
    print("--Begin report of books/frankenstein.txt--")
    print(f"The book contains {num_words} words.")
    print("Character counts:")
    for char, count in character_counts.items():
        print(f"The character '{char}' appears {count} times") 
    print("--End report--")
