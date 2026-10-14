
Libary_books = [
    "Muna Madan",
    "Shirish Ko Phool",
    "Basain",
    "Palpasa Cafe",
    "Karnali Blues",
    "Seto Dharti",
    "Radha",
    "Madhavi",
    "China Harayeko Manche",
    "Summer Love",
    "Pagal Basti",
    "Seto Bagh",
    "Shakuntala",
    "Ular",
    "Aina",
    "Python Crash Course",
    "Atomic Habits",
    "The Alchemist",
    "Rich Dad Poor Dad",
    "Harry Potter",
    "The Power of Habit",
    "Think and Grow Rich",
    "Deep Work",
    "Wings of Fire",
    "The Psychology of Money"
]

Libary_Data = []

# Book menu

def book_menu():
    print("======================Book List===================")
    for index, value in enumerate(Libary_books):
        print(f"{index + 1}. {value}")


# Add Books

def add_books():
    Books = {}
    Books["book_id"] = input("Enter your ID: ")
    Books["book_name"] = input("Enter a Book_Name: ")
    Books["author"] = input("Enter an author: ")
    Books["publised_year"] = input("Enter a Publication year: ")
    Libary_Data.append(Books)
    print("\n✅ Books added Successfully!\n")


# View All Books

def view_books():
    if not Libary_Data:
        print("❌ Books are not Found\n")
        return

    for book in Libary_Data:
        print(
            f"Book_ID: {book['book_id']}, "
            f"Book_Name: {book['book_name']}, "
            f"Author: {book['author']}, "
            f"Publised_year: {book['publised_year']}"
        )


# Search Books

def search_books():
    query = input("Enter ID or Book_Name to search: ")
    found = False

    for book in Libary_Data:
        if query == book["book_id"] or query.lower() == book["book_name"].lower():
            print("✅ Found:")
            print(
                f"Book_ID: {book['book_id']}, "
                f"Book_Name: {book['book_name']}, "
                f"Author: {book['author']}, "
                f"Publised_year: {book['publised_year']}"
            )
            found = True

    if not found:
        print("❌ Books are not Found\n")


# Update Books

def update_books():
    query = input("Enter a Book_ID: ")

    for book in Libary_Data:
        if query == book["book_id"]:
            book["book_name"] = input("Enter new Book_Name: ")
            book["author"] = input("Enter a new author: ")
            book["publised_year"] = input("Enter a new publised_year: ")
            print("✅ Successfully Updated!\n")
            return

    print("❌ Invalid ID. Please try again\n")


# Delete Books

def delete_book():
    query = input("Enter Book_ID: ")

    for book in Libary_Data:
        if query == book["book_id"]:
            Libary_Data.remove(book)
            print("✅ Delete Successfully!\n")
            return

    print("❌ Invalid ID\n")


# Borrow Book

def Borrow_Book():
    query = input("Enter a Book_Name: ")
    found = False

    for book in Libary_Data:
        if query.lower() == book["book_name"].lower():
            print("📚 ✅ Book exist in Library\n")
            found = True
            return

    if not found:
        print("📚 ⛔ Book not found or already borrowed\n")


# Count Books

def count_book():
    print(f"Total Books: {len(Libary_books)}")


# Book Return

def Book_Return():
    Return_Book = {}
    Return_Book["book_id"] = input("Enter a Return_Book_ID: ")
    Return_Book["book_name"] = input("Enter a Return_Book_Name: ")
    Return_Book["author"] = input("Enter a Return_Book_author: ")
    Return_Book["publised_year"] = input("Enter a Publised year: ")

    Libary_Data.append(Return_Book)
    print("✅ Book Return and added Successfully!")


# Main Menu

def main_menu():
    while True:
        print("\n==========================LIBARY MANAGEMENT SYSTEM==========================\n")
        print("1. Show Book Menu")
        print("2. Add Book")
        print("3. View All Books")
        print("4. Search Books")
        print("5. Update Books")
        print("6. Delete Books")
        print("7. Borrow Books")
        print("8. Return Books")
        print("9. Total Books")
        print("10. Exit")

        choice = input("\nEnter a number (1 to 10): ")

        if choice == "1":
            book_menu()

        elif choice == "2":
            add_books()

        elif choice == "3":
            view_books()

        elif choice == "4":
            search_books()

        elif choice == "5":
            update_books()

        elif choice == "6":
            delete_book()

        elif choice == "7":
            Borrow_Book()

        elif choice == "8":
            Book_Return()

        elif choice == "9":
            count_book()

        elif choice == "10":
            print("Exiting program. Goodbye! 👋")
            break

        else:
            print("❌ Invalid choice. Try again.\n")


# Run Program

main_menu()
