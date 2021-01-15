def Palindrome():

    n = 0

    while n < 1:

        original = str(input("Enter a Palindrome: "))

        #Here the spaces are erased
        original = original.replace(" ", "")

        #Here the word turns
        word = original[::-1]

        #And here the two words are compared
        if word == original:

            n = n + 1

            print("Your word is a Palindrome")

        else:

            print("\nYour word is NOT a Palindrome.\n")

print(Palindrome())