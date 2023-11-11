import json
""""
(1) Concerned with storing and retrieving books from a list.
(2) Use csv file - format of the csv file: name,author,read
(3) Use json file
"""

# books = []
# books_file = "books.txt"
books_file = "books.json"


def create_book_table():
    with open(books_file, 'w') as file:
        json.dump([], file)
        # pass  # just to make sure the file is there


def add_book(name, author):  # ask for book name and author
    books = get_all_books()
    books.append({'name': name, 'author': author, 'read': False})
    _save_all_books(books)

    # with open(books_file, 'a') as file:
    #     file.write(f"{name},{author},0\n")

    # books.append({'name': name, 'author': author, 'read': False})


def get_all_books():  # show all the books in our list

    try:
        with open(books_file, 'r') as file:
            # lines =[line.strip().split(',') for line in file.readlines()]
            books = json.load(file)
        # for line in lines:
            # read = 'YES' if line[2] == '1' else 'NO'
            # print(f"{line[0]} by {line[1]} - read: {read}")
        for book in books:
            read = 'YES' if book['read'] else 'NO'
            print(f"{book['name']} by {book['author']} - read: {read}")

        return books
        #     [
        #     {'name': line[0], 'author': line[1], 'read': line[2]}
        #     for line in lines
        # ]

    except FileNotFoundError:
        print("There are no books ATM.")
        create_book_table()


def _save_all_books(books):
    with open(books_file, 'w') as file:
        json.dump(books, file)
        # for book in books:
        #     file.write(f"{book['name']},{book['author']},{book['read']}\n")


def mark_book_as_read(book_read):  # ask for a book name and change it to 'read' in out list
    books = get_all_books()
    for book in books:
        if book['name'] == book_read:
            book['read'] = True
            # book['read'] = 1
    _save_all_books(books)


def delete_book(book_to_delete):  # ask for a book name and remove the book from the list
    # for book in books:
    #     if book['name'] == book_to_delete:
    #         books.remove(book)

    # global books
    # books = [book for book in books if book['name'] != book_to_delete]

    books = get_all_books()
    books = [book for book in books if book['name'] != book_to_delete]
    _save_all_books(books)

