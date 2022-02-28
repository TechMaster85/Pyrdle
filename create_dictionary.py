# Read a file named dictionary.txt and creates dictionary_out.txt.
# This script will make a list of 5-letter words that can be copy and pasted into a list.
# This is great if you want to condense the game into a single .py file.

# TODO: Make this make a lot more sense

dictionary_list = []
dictionary_file = open('dictionary.txt', 'r')
dictionary_out_file = open('dictionary_out.txt', 'w')
for line in dictionary_file:
    word = line.strip()
    if len(word) == 5:
        print(word)
        dictionary_list.append(word)

dictionary_out_file.write("dictionary = [")

counter = 0
for word in dictionary_list:

    if counter % 8 == 0:
        dictionary_out_file.write("\n\t")
    dictionary_out_file.write(f'"{word}", ')
    counter += 1

dictionary_out_file.write("\n]")

dictionary_file.close()
dictionary_out_file.close()
