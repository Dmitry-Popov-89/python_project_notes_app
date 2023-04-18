import file_functions
import note
import ui

number = 1 


def add():
    note = ui.create_note(number)
    array = file_functions.read_file()
    for notes in array:
        if note.Note.get_id(note) == note.Note.get_id(notes):
            note.Note.set_id(note)
    array.append(note)
    file_functions.write_file(array, 'a')
    print('The note has been added')


def show(text):
    logic = True
    array = file_functions.read_file()
    if text == 'date':
        date = input('Type date as dd.mm.yyyy: ')
    for notes in array:
        if text == 'all':
            logic = False
            print(note.Note.map_note(notes))
        if text == 'id':
            logic = False
            print('ID: ' + note.Note.get_id(notes))
        if text == 'date':
            logic = False
            if date in note.Note.get_date(notes):
                print(note.Note.map_note(notes))
    if logic == True:
        print('There is no any notes')


def id_edit_del_show(text):
    id = input('Enter id of the note: ')
    array = file_functions.read_file()
    logic = True
    for notes in array:
        if id == note.Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = ui.create_note(number)
                note.Note.set_title(notes, note.get_title())
                note.Note.set_body(notes, note.get_body())
                note.Note.set_date(notes)
                print('The note has been edited')
            if text == 'del':
                array.remove(notes)
                print('The note has been deleted')
            if text == 'show':
                print(note.Note.map_note(notes))
    if logic == True:
        print('The not has not been found. Please make shure that id is correct')
    file_functions.write_file(array, 'a')