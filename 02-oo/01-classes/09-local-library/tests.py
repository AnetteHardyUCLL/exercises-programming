from student import Book, Library

def test_library_add_book():
    library = Library("My Library")
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")

    library.add_book(book1)
    assert len(library.books) == 1
    assert book1 in library.books

    library.add_book(book2)
    assert len(library.books) == 2
    assert book2 in library.books

def test_library_remove_book():
    library = Library("My Library")
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")

    library.add_book(book1)
    library.add_book(book2)

    library.remove_book(book1)
    assert len(library.books) == 1
    assert book1 not in library.books
    assert book2 in library.books

def test_library_search_books():
    library = Library("My Library")
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("1984", "George Orwell")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Searching by title
    assert book1 in library.search_books("Gatsby")
    assert book2 in library.search_books("Mockingbird")
    assert book3 in library.search_books("1984")

    # Searching by author
    assert book1 in library.search_books("Fitzgerald")
    assert book2 in library.search_books("Lee")
    assert book3 in library.search_books("Orwell")

    # Searching by mixed string
    assert book1 in library.search_books("Gatsby")
    assert book2 in library.search_books("Harper")
    assert book3 in library.search_books("Orwell")

# Run the tests
test_library_add_book()
test_library_remove_book()
test_library_search_books()
