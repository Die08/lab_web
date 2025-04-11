
from pydantic import BaseModel, Field
from typing import Annotated

class Book(BaseModel):
    id: int #tipo di dato che accetta
    title: str
    author: str
    #review: int | None=None #rendiamo opzionale la recensione, di default è none
    review: Annotated[int|None, Field(ge=1, le=5)]=None

#book=Book(id=1, title="titolo", author="<NAME>",review=1)
#print(book)