#Step 1 
import random
import Hanman_art, Hanman_words

print(Hanman_art.logo)
lives = 6
end_of_game = False
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(Hanman_words.word_list)
print(f"the word is {chosen_word}")
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
display = ['_'] * len(chosen_word)
while not end_of_game:
    guess = input("Guess a letter:\n").lower()
    exist = False
    if guess in display:
            print("You have already guess this letter.")
            lives -= 1
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
            exist = True
    if not exist:
        lives -= 1
        print(f"{guess} is not in the words, you lose a life")
    print(f"{' '.join(display)}")
    if lives > 0:
        if "_" not in display:
            end_of_game = True
            print("You win.")
    else:
        end_of_game = True
        print("You lose")
    print(Hanman_art.stages[lives])