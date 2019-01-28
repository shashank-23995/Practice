'''
2. Write a program which keeps prompting the user to guess a word .
The user is allowed up to ten guesses
Write your code in such a way that the secret word and the number of allowed guesses are
easy to change. Print messages to give the user feedback
'''

secret_word = "Shashank"
guess_count = 0

while guess_count < 10:
    word = input("Enter word: ")
    if word == secret_word:
        print("You have guessed secret word successfully");
        break
