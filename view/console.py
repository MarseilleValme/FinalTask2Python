from .text import *
from datetime import datetime


def menu() -> int:
    print(main_menu)
    while True:
        choice = input(menu_choice)
        if choice.isdigit() and 0 < int(choice) < 8:
            return int(choice)
        print(input_error)


def print_message(message: str):
    length = len(message)
    print('\n' + '=' * length)
    print(message)
    print('=' * length + '\n')


def show_notes(book):
    if book:
        print('\n' + '=' * 127)
        for note in book:
            uid = note.get('id')
            title = note.get('title')
            text = note.get('text')
            current_datetime = note.get('current_datetime')
            print(f'{uid:>3}. {title:<20} {text:<80} {current_datetime:<20}')
        print('=' * 127 + '\n')
    else:
        print(book_error[0])


def input_note(message: str):
    print(message)
    title = input(new_note[0])
    text = input(new_note[1])
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {'title': title, 'text': text, 'current_datetime': current_datetime}


def input_diapazon(message: str):
    print(message)
    diapazon = []

    inp = input(search_diapazon[0])
    if inp == '':
        inp = '1980-01-01 00:01'
    inp = datetime.strptime(inp, "%Y-%m-%d %H:%M")
    diapazon.append(inp)

    inp = input(search_diapazon[1])
    if inp =='':
        inp = datetime.now()
    else:
        inp = datetime.strptime(inp, "%Y-%m-%d %H:%M")
    diapazon.append(inp)

    return diapazon


def input_return(message: str) -> str:
    return input(message)
