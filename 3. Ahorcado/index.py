import random
import string

HANGMAN = ['''
     ________
     |/    \|
     |      |
     o      |
    /|\     |
    / \     |
            |  
''', '''
     ________
     |/    \|
     |      |
     o      |
    /|\     |
    /       |
            |  
''', '''
     ________
     |/    \|
     |      |
     o      |
    /|\     |
            |
            |  
''', '''
     ________
     |/    \|
     |      |
     o      |
    /|      |
            |
            |  
''', '''
     ________
     |/    \|
     |      |
     o      |
    /       |
            |
            |  
''', '''
     ________
     |/    \|
     |      |
     o      |
            |
            |
            |  
''', '''
     ________
     |/    \|
     |      |
            |
            |
            |
            |  
''']

WORDS = [
    'PLUMA',
    'COMPUTADORA',
    'TECLADO',
    'MONITOR'
]


def main():
    lives = 6
    letters_entered = []

    word = select_word()
    hidden_word = ['_'] * len(word)

    while lives > 0:
        display(lives, hidden_word)
        
        current_letter = input('Ingresa una letra: ').upper()
        letters_found = []

        if current_letter in letters_entered:
            print('Ya has intentado con la letra:   {}'.format(current_letter))
            print('Intenta con una nueva.') 
            print('')
            continue           
        
        if current_letter in word:
            for i in range(len(word)):
                if (current_letter == word[i]):
                    letters_found.append(i)        
                    for idx in letters_found:
                        hidden_word[idx] = current_letter

            letters_found = []
        else:
            lives -= 1

        letters_entered.append(current_letter)

        if not '_' in hidden_word:
            print('winner')
            break
        elif lives == 0:
            print('loser')
            

    
                    

def select_word():
    index = random.randint(0, len(WORDS) - 1)
    return WORDS[index]

def display(live, hidden_word):
    print(HANGMAN[live])
    print(hidden_word)
    print('')


if __name__ == '__main__':
    main()