def palindrome_check():
    word = (input("Input word:").replace(" ","")).lower()
    it = 0

    while it < len(word)/2:
        if word[it]!=word[len(word)-it-1]:
            print("It's not a palindrome")
            return
        it+=1
    print("It's a palindrome")
palindrome_check()