def are_characters_hidden(word, string):
    it = iter(string.lower())
    return "Yes" if all(char in it for char in word.lower()) else "No"

first = input("")
second = input("")

print(are_characters_hidden(first, second))
