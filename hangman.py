import hangman_body
import hangman_words
import random
import string

def get_letter_index(word, letter):
    '''
    Function returns indexes of letters in word.
    '''
    indeksy = []
    if letter in word:
        for indeks, value in enumerate(word):
            if value == letter:
                indeksy.append(indeks)
    return indeksy

def change_hide_word(indeksy, hide_word, letter):
    '''
    Function changes floors to letters.
    '''
    for indeks in indeksy:
        hide_word[indeks] = letter
    

def show_hide_word(hide_word):
    print(' '.join(hide_word))        

def main():
    alphabet = string.ascii_lowercase
    print(alphabet)
    word = random.choice(hangman_words.words) 
    print(word)
    hide_word = list(len(word) * "_")
    
    mistakes = 0
    show_hide_word(hide_word)
    while "_" in hide_word:
        print(f"Dostępne litery: {alphabet}")
        letter = input("Podaj literę ")
        if letter in alphabet:
            alphabet = alphabet.replace(letter, "")

            if letter in word:
                change_hide_word(get_letter_index(word, letter), hide_word, letter)
                show_hide_word(hide_word)

                if "_" not in hide_word:
                    print("Hurra! Udało Ci się wygrać!")
            elif mistakes < len(hangman_body.HANGMAN_BODY):
                print(hangman_body.HANGMAN_BODY[mistakes])
                mistakes += 1
                show_hide_word(hide_word)
                if mistakes == len(hangman_body.HANGMAN_BODY):
                    print("Nie udało Ci się wygrać :(")
                    break
        else:
            print("Litera już wykorzystana")        
            print(hangman_body.HANGMAN_BODY[mistakes])
            show_hide_word(hide_word)
 
    
main()