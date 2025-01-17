from fastapi import APIRouter, HTTPException, Query, Depends
from services.pokemon_service import (
    get_first_10_pokemon, get_paginated_pokemon, search_pokemon,
    export_pokemon_data, add_pokemon, update_pokemon, delete_pokemon,
    get_pokemon_by_id, import_pokemon_data
)
from database.connection import get_db
from sqlalchemy.orm import Session
from fastapi.responses import StreamingResponse
import io

router = APIRouter()

@router.get("/pokemon/first10")
def api_get_first_10_pokemon(db: Session = Depends(get_db)):
    return get_first_10_pokemon(db)

@router.get("/pokemon")
def api_get_paginated_pokemon(page: int = 1, page_size: int = 10, db: Session = Depends(get_db)):
    return get_paginated_pokemon(db, page, page_size)

@router.get("/pokemon/search")
def api_search_pokemon(
    name: str = Query(None),
    type1: str = Query(None),
    type2: str = Query(None),
    generation: int = Query(None),
    legendary: bool = Query(None),
    page: int = 1,
    page_size: int = 10,
    db: Session = Depends(get_db)
):
    return search_pokemon(db, name, type1, type2, generation, legendary, page, page_size)

@router.get("/pokemon/export")
def api_export_pokemon(
    name: str = Query(None),
    type1: str = Query(None),
    type2: str = Query(None),
    generation: int = Query(None),
    legendary: bool = Query(None),
    db: Session = Depends(get_db)
):
    csv_data = export_pokemon_data(db, name, type1, type2, generation, legendary)
    buffer = io.StringIO()
    csv_data.to_csv(buffer, index=False)
    buffer.seek(0)
    return StreamingResponse(buffer, media_type="text/csv", headers={"Content-Disposition": "attachment; filename=pokemon.csv"})

@router.post("/pokemon")
def api_add_pokemon(pokemon_data: dict, db: Session = Depends(get_db)):
    return add_pokemon(db, pokemon_data)

@router.put("/pokemon/{id}")
def api_update_pokemon(id: int, updates: dict, db: Session = Depends(get_db)):
    return update_pokemon(db, id, updates)

@router.delete("/pokemon/{id}")
def api_delete_pokemon(id: int, db: Session = Depends(get_db)):
    return delete_pokemon(db, id)

@router.get("/pokemon/{id}")
def api_get_pokemon_by_id(id: int, db: Session = Depends(get_db)):
    return get_pokemon_by_id(db, id)

@router.post("/pokemon/import")
def api_import_pokemon(file: bytes, db: Session = Depends(get_db)):
    return import_pokemon_data(db, file)