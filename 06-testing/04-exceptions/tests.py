import pytest
from book import Book  # import the class


# test valid creation
@pytest.mark.parametrize("title", ["Watchmen", "Flowers for Algernon", "Ulysses"])
@pytest.mark.parametrize(
    "isbn",
    ["978-1779501127", "978-1-77-950112-7", "978 1 77 950112 7", "9780735611313"],
)
def test_valid_creation(title, isbn):
    book = Book(title, isbn)

    assert book.title == title
    assert book.isbn == isbn


# test invalid title
@pytest.mark.parametrize(
    "isbn",
    ["978-1779501127", "978-1-77-950112-7", "978 1 77 950112 7", "9780735611313"],
)
def test_creation_with_invalid_title(isbn):
    with pytest.raises(RuntimeError):
        Book("", isbn)


# test invalid isbn
@pytest.mark.parametrize("title", ["Watchmen", "Flowers for Algernon", "Ulysses"])
@pytest.mark.parametrize(
    "isbn",
    [
        "978-1779501126",
        "9780735611331",
        "978-1709571127",
        "978-1-77-950182-7",
        "97817795011271",
        "978073561131",
    ],
)
def test_creation_with_invalid_isbn(title, isbn):
    with pytest.raises(RuntimeError):
        Book(title, isbn)
