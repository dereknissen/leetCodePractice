# LEETCODE TIPS

s = "hello"

# STRING MANIPULATION

s.strip() # Removes whitespace from the beginning and end of string
s.lstrip() # Removes whitespace from beginning of string
s.rstrip() # Removes whitespace from end of string
s.strip("o") # Removes o's at the beginning and end of a string

s.find("hell") # Returns the indice of the beginning of the word (returns -1 if not found)

chars = [*[s]] # Returns a list of each character in a string (unpacking method)

# ARRAY MANIPULATION (LIST IN PYTHON)

ls = ["derek", "andrew", "blake"]
ls.sort() # Sorts by alphabetical order or numerical order
ls.reverse() # Reverses the order of elements in the list
ls = ls[::-1] # Another way to the reverse the order of elements in the list