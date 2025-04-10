from fastapi import APIRouter, HTTPException, Path
from models.book import Book
from data.books import books # importo il dizionario
from typing import Annotated

router = APIRouter(prefix="/books")

#decoratore con metodo percorso e funzione python per gestire
@router.get("/") #specifichiamo il pat nel decoratore
def get_all_books() -> list[Book]: #funz che fa codice richiesto, specifico cosa restituisce
    '''Return the list of available books.''' #descrizione da mettere sempre per dire cosa fa la funzione, inoltre viene presa come descrizione della fast API
    return list(books.values()) #prendiamo valori da dizionario e gli convertiamo in lista

@router.get("/{id}")
def get_book_by_id(id: Annotated[int, Path(description="The ID of the book to get")]) -> Book:
    '''Return the book by id.'''
#la freccia definisce il tipo di ritorno
    try:
        return books[id]
    except KeyError:
        raise HTTPException(status_code=404, detail="Book not found")


