
from sys import argv

script, filename = argv

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def count_letters():
	f = open(filename)
	filetext = f.read().lower() # once a file is read, it can be iterated through like a list
	
	letter_count = 0

# for every letter in the alphabet list, loop through the filetext list and see if it matches
# if matches, add to letter count till no more matches

	for letter in alphabet:

			for char in filetext:
				if char == letter:
					letter_count = letter_count + 1
			print letter_count

	f.close()

count_letters()

	
