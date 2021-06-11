import random

word_dict = {}

#filling the dictionary of words to choose from
with open("wordlist.txt") as words:
    for line in words:
        (key, val) = line.split()
        word_dict[int(key)] = val

next_game = True
words_list = []
win_count = 0

#function to generate words without repeats
def create_unique_word(my_dict, my_list):
    word = random.choice(list(my_dict.values()))
    unique = False
    
    while unique == False:
        if word in my_list:
            word = random.choice(list(my_dict.values()))
        else:
            my_list.append(word)
            unique = True
    return word

#function to show hangman progress
def print_scaffold(guesses):
    if (guesses == 0):
        print("_________")
        print("|	 |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|________")
    elif (guesses == 1):
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|")
        print("|")
        print("|")
        print("|________")
    elif (guesses == 2):
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	 |")
        print("|	 |")
        print("|")
        print("|________")
    elif (guesses == 3):
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	\|")
        print("|	 |")
        print("|")
        print("|________")
    elif (guesses == 4):
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	\|/")
        print("|	 |")
        print("|")
        print("|________")
    elif (guesses == 5):
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	\|/")
        print("|	 |")
        print("|	/ ")
        print("|________")
    elif (guesses == 6):
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	\|/")
        print("|	 |")
        print("|	/ \ ")
        print("|________")
        return
    
#loop restarts game as long as player chooses to continue
while next_game == True:
    print("New game: ")

    random_word = create_unique_word(word_dict, words_list)
                
    word_length = len(random_word)
    guesses_allowed = 7
    guesses_left = 7
    correct_guess = False
    correct_letters = []
    correct_length = 0
        
#guessingblock
    while (guesses_left > 0) and (correct_guess == False):
    
        if (word_length - correct_length) < 1:
            print("\nThat's correct.")
            correct_guess = True
            break

        print(f"\nYou have {guesses_left} guesses left.\n")

        for i in range(word_length):
            if random_word[i] in correct_letters:
                print(random_word[i], end="")
            else:
                print('_', end="")
         
        guess = input("\nPlease enter your guess: ")
        guess = guess.lower()
        if len(guess) > 1:
            if guess == random_word:
                print("\nThat's correct.")
                correct_guess = True
            else:
                guesses_left -= 1
                print("\nSorry, try again.")
        else:            
            if random_word.find(guess) != -1:
                if guess not in correct_letters:
                    correct_letters.append(guess)
                    for i in range(word_length):
                        if random_word[i] == guess:
                            correct_length += 1
                    guesses_left -= 1
                    print("\nThat's one correct letter.")
                else:
                    if (word_length - correct_length) < 1:
                        print("\nThat's correct.")
                        correct_guess = True
                    else:
                        print("\nYou've already guessed that letter.")
            else:
                print("\nThat's not a letter in the word.")
                guesses_left -= 1
        print_scaffold(guesses_allowed - (guesses_left + 1))
#end of game & stats
    if correct_guess == True:
        win_count += 1
    else:
        print(f"\nThe word was {random_word}.")

    loss_count = len(words_list) - win_count
    print(f"\nNumber of wins: {win_count}\nNumber of losses: {loss_count}")
    
    play_again = input("\nPlay again? (Y/N)")

    if play_again.upper() == 'Y':
        next_game = True
    else:
        next_game = False
