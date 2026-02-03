# Program to count each character in a string

# Input string
string = input("Enter a string: ")

# Dictionary to store character counts
char_count = {}

# Loop through each character in the string
for char in string:
    if char in char_count:
        char_count[char] += 1  # Increment count if already in dictionary
    else:
        char_count[char] = 1   # Add character to dictionary with count 1

# Print the character counts
print("Character count:")
for char, count in char_count.items():
    print(f"'{char}': {count}")

        



