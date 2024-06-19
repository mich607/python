# A PYTHON PROGRAM THAT PROMPTS A USER TO ENTER A LETTER IS A VOWEL OR A CONSONANT
# a number is a prime number or not
def check_vowel_consonant(letter):
    vowels = "aeiouAEIOU"

    if letter.isalpha() and len(letter) == 1:
        if letter in vowels:
            print(f"The letter '{letter}' is a vowel.")
        else:
            print(f"The letter '{letter}' is a consonant.")
    else:
        print("Please enter a single alphabet character.")


if __name__ == "__main__":
    letter = input("Enter a letter: ")
    check_vowel_consonant(letter)
