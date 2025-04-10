from fastapi import FastAPI
from models.book import Book
from data.books import books # importo il dizionario

app = FastAPI()

@app.get("/books") #specifichiamo il pat nel decoratore
def get_all_books() -> list[Book]: #funz che fa codice richiesto, specifico cosa restituisce
    '''Return the list of available books.''' #descrizione da mettere sempre per dire cosa fa la funzione, inoltre viene presa come descrizione della fast API
    return list(books.values()) #prendiamo valori da dizionario e gli convertiamo in lista


