#Imports Needed Module
import random

#String of all possible words
words_string = ("Monkey Capybara Squirrel Alligator Armadillo Anteater "
              "Hummingbird Spider Cockroach Rattlesnake Butterfly Orangutan "
                "Axolotl Aardvark Albatross Chimpanzee Chinchilla Dolphin Flamingo "
                "Grasshopper Hedgehog Ladybug Mosquito Narwhal Partridge Penguin "
                "Rhinoceros Wildebeest Wolverine")
#Splits string into list
words_list = words_string.split()

#Chooses word, lowers it, puts it in list
random_int = random.randint(0, len(words_list) - 1)
word_chosen = words_list[random_int]
word_chosen = word_chosen.lower()
word_chosen_list = []

#Player Guesses
correct_guesses_list = []
incorrect_guesses_counter = 0
word_input = ""

#Checks if the game is ended
end_game = False

#Adds the chosen word to the list
i = 0
for count in range(len(word_chosen)):
    word_chosen_list.append(word_chosen[i])
    correct_guesses_list.append(" ")
    i+=1

#Main Class
class hangman_functions():

    #Initializes needed variables
    def __init__(self):
        self.word_chosen = word_chosen
        self.correct_guesses_list = correct_guesses_list
        self.incorrect_guesses_counter = incorrect_guesses_counter

    #Draws hangman and checks if game is over
    def draw_hangman(self):
        if end_game != True:
            print(hangman_images[self.incorrect_guesses_counter])
            guesses_left = 6 - self.incorrect_guesses_counter
            #Prints how many guesses user has
            print("You have " + str(guesses_left) + "  tries left.")
            #If user has no guesses left, executes the statements
            if guesses_left == 0:
                print("You lose. The answer is " + str(self.word_chosen) + ".")
                update_game_status()

    #Asks user input and checks if it is correct
    def ask_user_input(self, word_chosen_list, correct_guesses_list):
        print(correct_guesses_list)
        valid_input = False
        #Logic that makes sure input is valid
        while valid_input == False:
            input_type = str(input("Would you like to guess a letter or a word?"))
            input_type = input_type.lower()
            input_type = input_type.strip()

            #If Else that checks if input is valid
            if input_type == "letter" or input_type == "word":
                valid_input = True
            else:
                print("Please input letter or word.")

        #Executes if input is letter
        if input_type == "letter":

            #If Else and While loop that makes sure it is one letter
            valid_input = False
            while valid_input == False:
                letter_input = str(input("What letter would you like to guess?"))
                letter_input = letter_input.lower()
                if len(letter_input) > 1:
                    print("Please input one letter.")
                else:
                    valid_input = True

            #Iterates through list and checks if guessed letter is in word
            incorrect_amount = 0
            for count in range(len(word_chosen)):
                if letter_input == word_chosen_list[count]:
                    correct_guesses_list.pop(count)
                    correct_guesses_list.insert(count, letter_input)
                    print("You were correct.")
                    count += 1
                #Adds to total if word is not at the count spot
                elif letter_input != word_chosen_list[count]:
                    incorrect_amount += 1

            #Will execute if letter is never found, means incorrect input
            if incorrect_amount == len(word_chosen):
                print("You guessed the wrong letter.")
                self.incorrect_guesses_counter += 1

            #Will execute if list is equal to word
            if self.correct_guesses_list == word_chosen_list:
                print("You won. " + str(word_chosen) + " was the correct answer.")
                update_game_status()

        #Executes if input is word
        if input_type == "word":
            self.word_input = str(input("What is your guess?"))
            self.word_input = self.word_input.lower()

            #Checks if the word input is the correct word
            #If it is, prints congratulations message ends game
            if self.word_input == word_chosen:
               print("You are correct. " + self.word_input + " was the correct word.")
               update_game_status()

            #If it isn't, prints other message and adds to counter
            elif self.word_input != word_chosen:
                print("Your guessed word was wrong.")
                self.incorrect_guesses_counter += 1


#Updates game status globally to end the game immediately
def update_game_status():
    global end_game
    end_game = True

#List of Images
hangman_images = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#Defines Class
hangman_game = hangman_functions()

#Main Game loop that executes the game
while end_game != True:

    hangman_game.ask_user_input(word_chosen_list, correct_guesses_list)
    hangman_game.draw_hangman()