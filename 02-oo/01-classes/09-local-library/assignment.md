# LOCAL LIBRARY
A new library just opened in a small town near you! They reached out to you asking for help building a system to keep track of all the books in the library!

## CHALLENGE
Complete the `Library` and `Book` classes.

## BOOK CLASS
__INIT__(SELF, TITLE, AUTHOR)

Set `.title` and `.author` to the values of the parameters.

## LIBRARY CLASS
Add the following methods.

### __INIT__(SELF, NAME)

Initialize a `.name` member variable to the value of the `name` parameter. Create a `.books` member initialized to an empty list.

### ADD_BOOK(SELF, BOOK)

Add the book to the `books` instance variable by appending it to the end of the list.

### REMOVE_BOOK(SELF, BOOK)

If the book's title and author match a library book's title and author, the `remove_book` method should remove that library book from the list.

### SEARCH_BOOKS(SELF, SEARCH_STRING)

For every book in the library check if the `search_string` is contained in the `title` or `author` field (case insensitive). Return a list of all books that match the search string, ordered in the same order as they were added to the library.

#### HINTS
You can use the `.lower()` method to convert a string to lowercase.