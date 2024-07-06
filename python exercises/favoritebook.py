favorite_book = {
    "title": "How To Kill a Mockindgird",
    "author": "Harper Lee",
    "genre": "Fiction"
}
def get_genre(book):
    return book.get("genre")

genre = get_genre(favorite_book)
print(f"The genre of the book {favorite_book['title']} is {genre} which was written by {favorite_book['author']}.")