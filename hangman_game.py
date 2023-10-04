import random
from collections import deque
import json



#gets the random word and returns the word
def get_word():
    words = json.loads(open('words.txt').read())
    game_word = random.choice(words)
    yield game_word


#displays the used letters and dashes for unmatched letters also calls display_hangman method
def display(game_word,guessed_letters,chances):
       
        print()
        display_hangman(chances,game_word)
        print('Already used letters:', ' '. join(guessed_letters))
        word_list = [letter if letter in guessed_letters else '___' for letter in game_word]
        #gets letter from gameword which are already on the guessed_letters else print dash
        if not chances == 0:
            print('Game Word:' , ' ' . join(word_list))
            print("lives: ", chances)

#to display the hangman as per lives        
def display_hangman(chances,game_word):
    if chances == 6:
        print("__________")
    if chances == 5:
        print("__________")
        print("    |     ")
    if chances == 4:
        print("__________")
        print("    |     ")
        print("    Ö     ")
    if chances == 3:
        print("__________")
        print("    |     ")
        print("    Ö     ")
        print("  / |     ")
    if chances == 2:
        print("__________")
        print("    |     ")
        print("    Ö     ")
        print("  / | \\     ")
    if chances == 1:
        print("__________")
        print("    |     ")
        print("    Ö     ")
        print("  / | \\     ")
        print("  /        ")
    if chances == 0:
        print("__________")
        print("    |     ")
        print("    Ö     ")
        print("  / | \\     ")
        print("  /   \\     ")
        print("You have lost! The word was:", game_word)
       
        
#to get the inputs from user and check them 
def check_input():
    game_word = next(get_word())
    game_word_letters = deque(game_word)#converts the selcted word in to letter in deque datatype
    guessed_letters = deque()
    alphabet = deque('abcdefghijklmnopqrstuvwxyz')
    chances = 6 
    while len(game_word_letters) > 0 and chances >=0:#check for remaining lives and the remaining letters
        display(game_word, guessed_letters, chances)
        if chances == 0: break
        entered_letter = input('guess a letter:').lower()# get input from user and converts to lowercase
        if entered_letter in alphabet and entered_letter not in guessed_letters:
                guessed_letters.append(entered_letter)#adds the entered letter into the set guessed latters
                if entered_letter in game_word_letters:#checks if the entered letter belons to the selected word
                    game_word_letters.remove(entered_letter)# removes the letter from the selected word 
                else:
                    chances -= 1 # reduces a chance if the entered letter doesnot belon to the selected letter  
                    print(f"{entered_letter} is incorrect, You have {chances} chances now, Try again")
                    
        elif entered_letter in guessed_letters:# checks if the entered letter is already on the guessed letters's set
            print("you have already entered this letter")
        else:
            print("Invalid character")
       
    else:
        print(f"Congratulations You have guessed the word - {game_word} correctly ")
            

    
def main():
    while True:
        play = input("Do you want to Play? press enter to play and q to quit: ")
        if play != "q":
            check_input()
        else:
            break
        


main()