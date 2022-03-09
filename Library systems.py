class Book:
    def __init__(self, title, author, dewey, isbn):
        self.title = title.title()  # strin
        self.author = author  # string
        self.dewey = dewey  # string
        self.isbn = isbn  # string
        self.available = True
        self.borrower = None
        book_list.append(self)  # Holds book objects as created - main routine

    def book_details(self):
        print(self.title)
        print(self.author)
        print(self.dewey)
        print(self.isbn)
        print(self.available)
        print(self.borrower)
        print("##################")


# Print list of books
def print_info():
    for book in book_list:
        book.book_details()


class User:
    def __init__(self, name, address):
        self.name = name  # string
        self.address = address  # string
        self.fees = 0.0  # float
        self.borrowed_books = []
        user_list.append(self)

    def user_details(self):
        print("Name", self.name)
        print("Address", self.address)
        print("Fee: $", self.fees)
        print("##################")


def print_user():
    for user in user_list:
        user.user_details()


def add_user():
    name = input("Enter the new users name: ").title()
    address = input("Enter the new users address: ")
    User(name, address)
    print(name, address, "has been added to the user list")


def add_book():
    title = input("Enter the new books title: ").title()
    author = input("Who is the books author: ").title()
    dewey = input("Enter the books dewey code: ").upper()
    isbn = input("Enter the books ISBN number: ")
    Book(title, author, dewey, isbn)
    print(f"{title} has been added to the book list")


def find_user():
    user_to_find = input("Enter the name of user: ").title()
    for user in user_list:
        if user.name == user_to_find:
            print(f"Hi {user_to_find}")
            return user
        print("Sorry, no user was found with that name")
        return None


def find_book():
    book_to_find = input("Enter the name of the book: ").title
    for book in book_list:
        if book.title == book_to_find:
            print(f"The book '{book_to_find}' is in the catalogue")
            return Book
        print("Sorry, no book was found with that name")
        return None


def lend_book():
    user = find_user()
    print()
    if user:  # only if user was found
        book = find_book()  # make sure the book exists
        if book.available:  # and is available
            confirm = input("Type 'Y' if you want to borrow this"
                            "book: "). upper()  # user confirms
            if confirm == "Y":
                print(f"Book title: '{book.title}' is now out on"
                      f"loan to {user.name}")  # feedback to user
                book.available = False  # set 'available' attribute
                book.borrower = user.name  # record borrower name
                user.borrowed_books.append(book.title)
            else:
                print(f"Sorry, '{book.title}' is already out on loan")

def return_book():
    user = find_user()
    print()
    if user:
        book = find_book()
        if not book.available:
            confirm = input("Type 'Y' if you want to"
                            "return this book: ").upper()
            if confirm == "Y":
                print(f"Book title: '{book.title}' is now returned "
                      f"to the library")
                book.available = True
                book.borrower = user.name
                user.borrower_books.remove(book.title)
        else:
            print(f"Sorry, '{book.title}' on loan to someone else")
# Main routine


book_list = []
user_list = []


# Create book objects
Book("Lord of the Rings", "J.R.R. Tolkien",  "TOL", "9780261103252")
Book("The Hunger Games", "Suzanne Collins", "COL", "9781407132082")
Book("A Tale Of Two Cities", "Charles Dickens", "DIC", "9781853262647")
Book("Harry Potter", "J.K. Rowling", "ROW", "9780439321624")

# Create objects - Users
User("John", "12 Example St")
User("Susan", "1011 Binary Rd")
User("Paul", "25  Appletree Dr")
User("Mary", "8 Moon Cres")

new_action = True
while new_action:
    print("1. Lend a book")
    print("2. Return a book")
    print("3. Add a user")
    print("4. Add a book")
    print("5. Exit")

    choice = input("\nWhat would you like to do? - enter a number: ")
    if choice == "1":
        lend_book()
    elif choice == "2":
        return_book()
    elif choice == "3":
        add_user()
    elif choice == "4":
        add_book()
    elif choice == "5":
        confirm = input("Type 'Y' if you want to exit the system - or amy other"
                        " key  to go back to the menu: ").upper()
        if confirm == "Y":
            print("Goodbye")
            new_action = False

    else:
        print("\n***  That was not a valid choice ***\n")
