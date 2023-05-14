from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app = FastAPI()

class Libro(BaseModel):
    titulo: str
    autor: str
    paginas: int
    editorial: Optional[str]

@app.get("/")
def index():
    return {"mensaje":"Hacemos de algo simple algo extraordinario"}


@app.get("/libros/{id}")
def mostrar_libro(id: int):
    if id == 1:
        return "nombre: El libro 1, autor: Juan"
    elif id == 2:
        return " nombre: El libro 2, autor: Sam"
    else:
        return "mensaje: No hay libro con ese id"
    
@app.post("/libros")
def insertar_libro(libro: Libro):
    return f"{libro.titulo} fue insertado"