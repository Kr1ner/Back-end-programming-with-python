word_without_vowels = ""

# Prompt the user to enter a word
user_word = input("")
# and assign it to the user_word variable.
user_word = user_word.upper()


for letter in user_word:
    if letter != "A" and letter != "E" and letter != "I" and letter != "O" and letter != "U":
        word_without_vowels+=letter
    else:
        continue

# Print the word assigned to word_without_vowels.
print(word_without_vowels)