def display_menu():
    print('COMMAND MENU')
    print('add - add a book')
    print('delete - delete a book')
    print('search - search for a book by ISBN')
    print('modify - modify a field on an existing book')
    print('add field - add a field to an exiting book')
    print('return - return a list of books by author or genre')
    print('exit - exit program')
    return('')

def add():
    book = input('Title: ')
    isbn = input('ISBN: ')
    author = input('Author: ')
    genre = input('Genre: ')

def delete():
    print('Please list the name of the book you would like to delete.')

def search():
    print('What is the ISBN of the book you are looking for?')

def modify():
    print('what is the name of the book you would like to modify?')

def field():
    print('What is the name of the book you would like to add to?')

def return_a_list():
    print('Would you like to return a list by author or genre?')

def exit():
    print('Now exited from the system')

def error_message():
    print('Please try again')

print(display_menu())

print(input('Command: '))

user_command = (input('Command: '))
if user_command == add:
    print(add())
elif user_command == delete:
    print(delete())
elif user_command == search:
    print(search())
elif user_command == modify:
    print(modify())
elif user_command == field:
    print(field())
elif user_command == exit:
    print(exit())
else:
    print(error_message())
