# PART 1: Create the library's book names and available copies
books = ["python_book", "java_book", "html_book", "css_book", "sql_book"]
available_copies = [7, 0, 5, 3, 9]


# PART 2: Pair books with available copies into a dictionary
library = {
    book: copies
    for book, copies in zip(books, available_copies)
}

print("Complete Library:", library)


# PART 3: Filter only the books that are currently available
available_books = [
    book for book in books
    if library[book] > 0
]

print("Available Books:", available_books)


# PART 4: Ask the student which book they want to borrow
selected_book = input("Which book do you want to borrow? ")


# PART 5: Stop the checker early if the selected book is unavailable
if selected_book not in library or library[selected_book] == 0:
    print(
        selected_book,
        "is currently unavailable! Stopping the checker."
    )
    exit()


# PART 6: Create book prices and ask for an additional charge
book_prices = [100, 150, 80, 120, 200]

extra_charge = int(
    input("Enter the extra charge to add to every price: ")
)


# PART 7: Apply the extra charge to every price using map()
updated_prices = list(
    map(lambda price: price + extra_charge, book_prices)
)

print("Updated Prices:", updated_prices)


# PART 8: Find the updated price of the selected book
book_position = books.index(selected_book)

selected_price = updated_prices[book_position]

print(
    "Price of",
    selected_book,
    "after extra charge:",
    selected_price
)


# PART 9: Reduce the available copies after borrowing
library[selected_book] = library[selected_book] - 1

print(
    selected_book,
    "borrowed! Remaining copies:",
    library[selected_book]
)


# PART 10: Print the final library summary
print("")
print("===== LIBRARY INVENTORY CHECKER =====")
print("Book Borrowed:", selected_book)
print("Price Paid:", selected_price)
print("Updated Library:", library)
print("======================================")
