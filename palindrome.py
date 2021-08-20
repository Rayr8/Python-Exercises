def is_palindrome(word):
    reversed_word = word[::-1]
    status = 1
    if(word!=reversed_word):
        status = 0
    return status

word = input("Enter the word: ")
status = is_palindrome(word)
if(status):
    print("True")
else:
    print("False")