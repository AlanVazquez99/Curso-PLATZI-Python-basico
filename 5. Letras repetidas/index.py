import os

def repetido(txt):
    unique = []
    for letter in txt:
        if txt.count(letter) == 1:
            unique.append(letter)

    if len(unique) == 0:
        unique.append('_')

    return unique



if __name__ == '__main__':
    os.system('clear')
    print('Ingresa una cadena de caracteres o texto: ')
    txt = input('\t').upper()

    print('\n\tLas letras que no se repiten son: \n\t{}'.format(repetido(txt)))
    input('Presiona una tecla para continuar...')
    