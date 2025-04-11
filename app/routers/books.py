from fastapi import APIRouter, HTTPException, Path
from pydantic import ValidationError

from models.book import Book
from models.review import Review
from data.books import books # importo il dizionario
from typing import Annotated

router = APIRouter(prefix="/books")

#decoratore con metodo percorso e funzione python per gestire
@router.get("/") #specifichiamo il pat nel decoratore
def get_all_books(
        sort: bool =False
) -> list[Book]: #funz che fa codice richiesto, specifico cosa restituisce
    '''Return the list of available books.''' #descrizione da mettere sempre per dire cosa fa la funzione, inoltre viene presa come descrizione della fast API
    if sort:
        return sorted(books.values(), key=lambda book: book.review) #serve per ordinare in base a review
    return list(books.values()) #prendiamo valori da dizionario e gli convertiamo in lista

@router.post("/")
def add_book(book: Book) -> Book:
    '''Adds a new book.'''
    if book.id in books:
        raise HTTPException(status_code=403, detail="Book ID already exists.")
    books[book.id] = book
    return "Book successfully added."

@router.delete("/")
def delete_all_book():
    '''Delete all books.'''
    books.clear()
    return "Book successfully deleted."

@router.delete("/{id}")
def delete_book(id: Annotated[int, Path(description="The ID of the book to get")]
                )   :
    '''Delete the book with the given ID.'''
    try:
        del books[id]
        return "Book successfully deleted."
    except KeyError:
        raise HTTPException(status_code=404, detail="Book not found.")

@router.get("/{id}")
def get_book_by_id(id: Annotated[int, Path(description="The ID of the book to get")]) -> Book:
    '''Return the book by id.'''
#la freccia definisce il tipo di ritorno
    try:
        return books[id]
    except KeyError:
        raise HTTPException(status_code=404, detail="Book not found")

@router.post("/{id}/review")
def add_review(
    id: Annotated[int, Path(description="The ID of the book to get")],
    review: Review):
    try:
        books[id].review=review.review
        return "Review sucessfully added"
    except KeyError:
        raise HTTPException(status_code=404, detail="Book not found")
    except ValidationError:
        raise HTTPException(status_code=400, detail="Not a valid request")


@router.put("/{id}")
def update_book(
        id: Annotated[int, Path(description="The ID of the book to update")],
        book: Book):
    '''updates a book.'''
    if not id in books:
        raise HTTPException(status_code=404, detail="Book not found")
    books[id] = books
    return "Book successfully updated."



