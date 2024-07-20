import random

words = ["github", "youtube", "android", "apple"]
chosen_word = random.choice(words)
displayed_word = '-' * len(chosen_word)

def main():
    print("Welcome to Hangman!")
    attempts = 10
    displayed_word_list = list(displayed_word)
    
    while attempts > 0 and '-' in displayed_word_list:
        print(''.join(displayed_word_list))
        c = input("Introduce a character: ").strip().lower()
        
        if len(c) == 1 and c in chosen_word and c not in displayed_word_list:
            for index, character in enumerate(chosen_word):
                if character == c:
                    displayed_word_list[index] = c
        else:
            attempts -= 1
            print(f"Incorrect! You have {attempts} attempts left.")
    
    if '-' not in displayed_word_list:
        print(f"Congratulations! You guessed the word: {''.join(displayed_word_list)}")
    else:
        print(f"Game over! The word was: {chosen_word}")

if __name__ == "__main__":
    main()
