from utils import database

USER_CHOICE = """"
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice:   """


def menu():
    # database.create_book_table()
    user_input = input(USER_CHOICE)

    while user_input != 'q':

        if user_input == 'a':
            book_name = input("Enter book name: ")
            book_author = input("Enter book author: ")
            database.add_book(book_name, book_author)

        elif user_input == 'l':
            database.get_all_books()

        elif user_input == 'r':
            book_read = input("Enter book name you read: ")
            database.mark_book_as_read(book_read)

        elif user_input == 'd':
            book_to_delete = input("Enter book name you want to delete: ")
            database.delete_book(book_to_delete)

        else:
            print("Unknown command. Please try again!")

        user_input = input(USER_CHOICE)


menu()