import note


def create_note(number):
    title = check_len_text_input(
        input('Type the note title: '), number)
    body = check_len_text_input(
        input('Type the discription: '), number)
    return note.Note(title=title, body=body)


def menu():
    print("\nWelcome to the note programm. Here are some avaliable functions:\n\n1 - show all notes\n2 - add new note\n3 - delete note\n4 - edit note\n5 - show notes by date\n6 - show note by id\n7 - exit\n\nEnter function nuber: ")


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Text must be longer than {n} symbols\n')
        text = input('Type a text: ')
    else:
        return text


def goodbuy():
    print("Thank you for using our programm! Have a nice day!")