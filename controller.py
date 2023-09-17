from view import menu, show_notes, print_message, input_note, input_return, input_diapazon
import model
from view import text


def start():
    while True:
        choice = menu()
        if choice == 1:
            if not model.note_book:        # Дабы при повторном открытии файла не дублировать список дописыванием в самого себя
                model.open_file()
                if not model.note_book:
                    print_message(text.book_error[1])
                else:
                    print_message(text.open_successful[0])
            else:
                print_message(text.open_successful[1])
        elif choice ==2:
            model.save_file()
        elif choice ==3:
            new = input_diapazon(text.search_word)
            result = model.search(new)
            show_notes(result)
        elif choice == 4:
            new = input_note(text.input_new_note)
            model.add_note(new)
            print_message(text.note_saved(new.get('title')))
        elif choice == 5:
            show_notes(model.note_book)
            index = input_return(text.input_index)
            new = input_note(text.input_change_note)
            model.change(int(index), new)
            old_name = model.note_book[int(index)-1].get('title')
            print_message(text.note_changed(new.get('title') if new.get('title') else old_name))

        elif choice == 6:
            index = input_return(text.input_delete_index[0])
            if int(index)>len(model.note_book):
                print_message(text.input_delete_index[1])
            else:
                model.delete_record(int(index))

        elif choice == 7:
            break
