import os

KEYS = {
    "a": "3",
    "b": "r",
    "c": "1",
    "d": "h",
    "e": "?",
    "f": "~",
    "g": "7",
    "h": ">",
    "i": "f",
    "j": "l",
    "k": "v",
    "l": "&",
    "m": "/",
    "n": "y",
    "ñ": ";",
    "o": "w",
    "p": "c",
    "q": "t",
    "r": "e",
    "s": "b",
    "t": "a",
    "u": "%",
    "v": "@",
    "w": ".",
    "x": "-",
    "y": "=",
    "z": "_",
    " ": " "
}
message_list = []


def main():
    print('''

        PROGRAMA DE ENCRIPTACION

         _______________________
        |                       |
        |  (E) Encriptar        |
        |  (D) Desencriptar     |
        |  (S) Salir            |
        |_______________________|

    ''')

    option = input("Que es lo que quieres hacer:    ").upper()
    if option == 'E':
        print("Encriptar")
        message_list.append(encriptar())
        return True

    elif option == 'D':
        print("Desencriptar")
        desencriptar(''.join(message_list))
        return True

    elif option == 'S':
        return False

    else:
        print("Elige una opcion valida")
        return True


def encriptar():
    print("Ingresa el mensaje a desencriptar: ")
    message = input().lower()
    encrypted_list = []
    for letter in message:
        encrypted_list.append(KEYS.get(letter, letter))

    encrypted_message = ''.join(encrypted_list)
    print("Tu mensaje encriptado se ve asi: \n\t\"{}\"".format(encrypted_message))
    return encrypted_message


def desencriptar(encrypted):
    while True:
        os.system("clear")
        print("""
            _______________________________________
            |                                       |
            | (n) Desencriptar un nuevo mensaje     |
            | (o) Desencritar mensaje anterior      |
            | (s) Salir                             |
            |_______________________________________|

        """)
        option = input("Selecciona una opcion: \t").upper()
        if option == 'N':
            print("Palabra nueva")
            new_message = input().lower()
            encode(new_message)

            input("Presiona para continuar...")
            continue

        elif option == 'O':
            print("Mesaje cifrado: ")
            print("\t", encrypted, "\n\n")
            encode(encrypted)
            input("Presiona para continuar...")
            continue

        elif option == 'S':
            input("Esta saliendo de este menu...")
            return 0

        else:
            input("Opcion ingresada invalida")
            break


def encode(code):
    code_list = []

    for letter in code:
        if letter in KEYS.values():
            for key, value in KEYS.items():
                if letter == value:
                    code_list.append(key)
                    break
            continue
    print("\n\nSu mensaje desencriptado es: \n\t {}".format(''.join(code_list)))


if __name__ == "__main__":
    resume = True
    
    while resume:
        resume = main()
        print("")
        print("")
        input("Presiona una tecla para continuar ...")
        os.system('clear')
