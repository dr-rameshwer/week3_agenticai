"""
Solution 09: Campus Library Inventory Tool
Course Instructor: Dr. Rameshwer

Reference Solution for Exercise 09.
"""

LIBRARY_CATALOGUE = {
    "978-0134685991": {"title": "Effective Python", "author": "Brett Slatkin", "available_copies": 3},
    "978-0596517748": {"title": "JavaScript: The Good Parts", "author": "Douglas Crockford", "available_copies": 0},
    "978-1491957660": {"title": "Designing Data-Intensive Applications", "author": "Martin Kleppmann", "available_copies": 2}
}

def query_library_book_status(isbn: str) -> dict:
    """Queries the campus library inventory for book availability by ISBN."""
    clean_isbn = isbn.strip()
    if clean_isbn in LIBRARY_CATALOGUE:
        book = LIBRARY_CATALOGUE[clean_isbn]
        status = "Available for Loan" if book["available_copies"] > 0 else "All Copies Checked Out"
        return {
            "found": True,
            "isbn": clean_isbn,
            "title": book["title"],
            "author": book["author"],
            "copies": book["available_copies"],
            "status": status
        }
    return {
        "found": False,
        "isbn": clean_isbn,
        "error": f"ISBN '{clean_isbn}' was not found in the campus library catalogue."
    }

if __name__ == "__main__":
    print(query_library_book_status("978-1491957660"))
