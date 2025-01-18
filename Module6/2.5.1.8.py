firstword = input("").lower()
secondword = input("").lower()
firstword = sorted(firstword)
secondword = sorted(secondword)
if secondword == firstword:
    print("Anagrams")
else:
    print("Not anagrams")
