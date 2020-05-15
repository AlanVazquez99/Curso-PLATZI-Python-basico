import os
import csv

def clear():
    os.system('clear')

def pause():
    input('Presione una tecla para continuar ...')

def tittle(text='', padding=75):
    char_num = len(text)
    board = '_' * (char_num + 2)
    print(board.center(padding, ' '))
    print('| {} |'.format(text.upper()).center(padding, ' '))
    print('|{}|'.format(board).center(padding, ' '))

class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

class ContactBook:
    def __init__(self):
        self._contacts = []

    def _print_contact(self, contact):
        print(' {} '.format(contact.name).center(50, ' '))
        print('\tNumero: {} \n\n'.format(contact.number))

    def _save(self):
        with open('schedule.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(('name', 'number'))

            for contact in self._contacts:
                writer.writerow( (contact.name, contact.number) )

    def _not_found(self, txt='contacto'):
        tittle('No se encontro el contacto {}'.format(txt), 30)

    def find(self, name):
        if len(self._contacts) == 0:
            return -1
        for idx, contact in enumerate(self._contacts):
            if name.lower() == contact.name.lower():
                self._print_contact(contact)
                return idx
        else:
            return '404'

    def update(self, name, number):
        idx = self.find(name)
        self._contacts[idx].number = number
        self._save()

    def add(self, name, number):
        clear()
        found = self.find(name)

        if  found == '404' or found == -1:
            contact = Contact(name.capitalize(), number)
            self._contacts.append(contact)
            self._print_contact(contact)
            self._save()
            return '0'
        else:
            print('El contacto {} ya existe en la agenda'.format(name))
            return '2'

    def list(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def delete(self, name):
        idx = self.find(name)

        if idx == '404':
            self._not_found(name)
            return '404'

        del self._contacts[idx]
        self._save()

def run():
    clear()
    schedule = ContactBook()

    with open('schedule.csv', newline='') as f:
        reader = csv.reader(f)
        rows = reader.line_num
        for idx, row in enumerate(reader):
            if idx == 0 or idx == rows:
                continue
            
            schedule.add(row[0], row[1])

    while True:
        clear()
        tittle('mi agenda')
        option = input('''
        [a] AGREGAR \n\t[u] ACTUALIZAR \n\t[f] BUSCAR \n\t[d] ELIMINAR \n\t[l] LISTAR TODOS \n\t[e] SALIR

        Selecciona una opcion:
        ''').lower()

        if option == 'a':
            clear()
            tittle('ADD')
            name = input('Nombre:  ')
            number = input('Numero:  ')
            schedule.add(name, number)
            pause()

        if option == 'u':
            clear()
            tittle('UPDATE')
            name = input('Nombre:  ')
            number = input('Numero:  ')
            schedule.update(name, number)
            pause()

        if option == 'f':
            clear()
            tittle('FIND')
            name = input('Buscar contacto:  ')
            schedule.find(name)
            pause()

        if option == 'd':
            clear()
            tittle('DELETE')
            name = input('Contacto a borrar:  ')
            schedule.delete(name)
            pause()

        if option == 'l':
            clear()
            tittle('LIST')
            schedule.list()
            pause()

        if option == 'e':
            clear()
            tittle('Saliendo del programa...')
            input()
            clear()
            break

if __name__ == '__main__':
    run()