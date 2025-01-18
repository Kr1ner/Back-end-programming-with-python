birthday = input("")

while len(birthday)>1:
    birthsum = 0
    for char in birthday:
        birthsum+=int(char)
    birthsum = str(birthsum)
    birthday = birthsum
print(birthday)