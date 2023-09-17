import json
from datetime import datetime
import os.path
note_book = []
path = 'note_book.json'

def open_file():
    if os.path.exists(path):
        with open(path, 'r', encoding='UTF-8') as file:
            data = json.load(file)
        for note in data:
            note_book.append(note)
    else: note_book.append

def save_file():
    with open(path, 'w', encoding='UTF-8') as file: 
        json.dump(note_book, file)
    file.close()
    note_book.clear()


def check_id():
    if len(note_book)==0:
        return {'id': 1} 
    
    uid_list = []
    for note in note_book:
        uid_list.append(int(note.get('id')))
    return {'id': max(uid_list) + 1}


def add_note(new: dict):
    smart_girl = check_id() # Перенастроил апдейт нового контакта как советовала умная девочка. 
    smart_girl.update(new)  # Терь индексы добавляемых записей становятся на место.
    note_book.append(smart_girl)  

def search(diapazon: str):
    result = []
    for note in note_book:
        current_datetime = datetime.strptime(note.get('current_datetime'), "%Y-%m-%d %H:%M:%S")
        if diapazon[0] <= current_datetime <= diapazon[1]:
            result.append(note)
    return result

def change(index: int, new):
    for key, field in new.items():
        if field != '':
            note_book[index - 1][key] = field

def delete_record(index: int):
    note_book.pop(index-1)
    for i in range (index-1, len(note_book)):           # Ператрахиваю нумерацию записей после удаления.
            note_book[i]['id']=str(i+1)