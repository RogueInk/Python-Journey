# 1. Library Management System
# Features: Add books, Borrow books, Return books, Search books, View all books
# Concepts: Lists, Dictionaries, Loops, Functions
# Challenge: Track who borrowed which book.

# Defining Variables
Booklist = ["The Great Gatsby", "To Kill a Mockingbird", "1984", "Pride and Prejudice", "The Catcher in the Rye", "The Lord of the Rings", "The Hobbit", "The Alchemist", "The Hunger Games", "The Da Vinci Code", "Lord of The Mysteries", "The Chronicles of Narnia", "The Little Prince", "The Grapes of Wrath", "The Picture of Dorian Gray", "The Count of Monte Cristo"]
askname = input("Welcome To The Book Library| Please Enter your name: ")
borrowername = askname.capitalize()
borrowerdict = {}

# This function displays the list of books available in the library.
def DisplayBooks():
    print("Books available in the library:")
    for book in Booklist:
        print(book)

# This function adds a new book to the library's book list.

def AddBook(book):
    if book.lower() in [b.lower() for b in Booklist]:
        print(f"{book} is already in the book list.")
    else:
        Booklist.append(book)
        print(f"{book} has been added to the book list.")

# This function allows a user to borrow a book from the library.

def BorrowBook(Bbook):
    if Bbook.lower() in [b.lower() for b in Booklist]:
        ask = input(f"Do you want to borrow {Bbook}? ")
        if ask.lower() == "yes":
            Booklist.remove(Bbook)
            borrowerdict[Bbook] = borrowername
            print(f"{Bbook} has been borrowed by {borrowername}.")
        else:
            print(f"{Bbook} has not been borrowed.")
    else:
        print(f"{Bbook} is not available for borrowing.")

# This function allows a user to return a borrowed book to the library.

def ReturnBook(Rbook):
    if Rbook.lower() in [b.lower() for b in Booklist]:
        print(f"{Rbook} is already in the book list.")
    else:
        Booklist.append(Rbook)
        borrowerdict.pop(Rbook, None)
        print(f"{Rbook} has been returned to the book list.")

# This function allows a user to search for a book in the library's book list.

def SearchBook(Sbook):
    if Sbook.lower() in [b.lower() for b in Booklist]:
        print(f"{Sbook} is available in the book list.")
    else:
        print(f"{Sbook} is not available in the book list.")

# Main Program Loop
while True:
    print("\n1. Display Books\n2. Add Book\n3. Borrow Book\n4. Return Book\n5. Search Book\n6. Borrower Dictionary\n7. Exit")
    choice = input("Enter your choice: ")

    if choice == "1" or choice.lower() == "display books":
        DisplayBooks()
    elif choice == "2" or choice.lower() == "add book":
        book = input("Enter the name of the book to add: ")
        AddBook(book)
    elif choice == "3" or choice.lower() == "borrow book":
        Bbook = input("Enter the name of the book to borrow: ")
        BorrowBook(Bbook)
    elif choice == "4" or choice.lower() == "return book":
        Rbook = input("Enter the name of the book to return: ")
        ReturnBook(Rbook)
    elif choice == "5" or choice.lower() == "search book":
        Sbook = input("Enter the name of the book to search: ")
        SearchBook(Sbook)
    elif choice == "6" or choice.lower() == "borrower dictionary":
        print(borrowerdict)
    elif choice == "7" or choice.lower() == "exit":
        print("Thank you for using the Book Library!")
        break
    else:
        print("Invalid choice! Please try again.")