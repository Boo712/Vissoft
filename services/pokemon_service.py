from sqlalchemy.orm import Session
from database.models import Pokemon
from fastapi import HTTPException
import pandas as pd
import io

def get_first_10_pokemon(db: Session):
    return db.query(Pokemon).limit(10).all()

def get_paginated_pokemon(db: Session, page: int, page_size: int):
    offset = (page - 1) * page_size
    return db.query(Pokemon).offset(offset).limit(page_size).all()

def search_pokemon(db: Session, name: str, type1: str, type2: str, generation: int, legendary: bool, page: int, page_size: int):
    query = db.query(Pokemon)
    if name:
        query = query.filter(Pokemon.name.ilike(f"%{name}%"))
    if type1:
        query = query.filter(Pokemon.type1 == type1)
    if type2:
        query = query.filter(Pokemon.type2 == type2)
    if generation:
        query = query.filter(Pokemon.generation == generation)
    if legendary is not None:
        query = query.filter(Pokemon.legendary == legendary)
    offset = (page - 1) * page_size
    return query.offset(offset).limit(page_size).all()

def export_pokemon_data(db: Session, name: str, type1: str, type2: str, generation: int, legendary: bool):
    query = db.query(Pokemon)
    if name:
        query = query.filter(Pokemon.name.ilike(f"%{name}%"))
    if type1:
        query = query.filter(Pokemon.type1 == type1)
    if type2:
        query = query.filter(Pokemon.type2 == type2)
    if generation:
        query = query.filter(Pokemon.generation == generation)
    if legendary is not None:
        query = query.filter(Pokemon.legendary == legendary)
    data = query.all()
    df = pd.DataFrame([pokemon.to_dict() for pokemon in data])
    return df

def add_pokemon(db: Session, pokemon_data: dict):
    if not pokemon_data.get("name"):
        raise HTTPException(status_code=400, detail="Pokemon name cannot be empty.")
    if db.query(Pokemon).filter(Pokemon.name == pokemon_data["name"]).first():
        raise HTTPException(status_code=400, detail="Pokemon name already exists.")

    mandatory_fields = ["type1", "generation", "legendary", "hp", "attack", "defense", "spatk", "spdef", "speed"]
    for field in mandatory_fields:
        if field not in pokemon_data or pokemon_data[field] is None:
            raise HTTPException(status_code=400, detail=f"{field} cannot be empty.")

    total = pokemon_data["hp"] + pokemon_data["attack"] + pokemon_data["defense"] + \
            pokemon_data["spatk"] + pokemon_data["spdef"] + pokemon_data["speed"]
    pokemon_data["total"] = total

    new_pokemon = Pokemon(**pokemon_data)
    db.add(new_pokemon)
    db.commit()
    db.refresh(new_pokemon)
    return new_pokemon

def update_pokemon(db: Session, id: int, updates: dict):
    pokemon = db.query(Pokemon).filter(Pokemon.id == id).first()
    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokemon not found.")

    for key, value in updates.items():
        setattr(pokemon, key, value)
    
    db.commit()
    db.refresh(pokemon)
    return pokemon

def delete_pokemon(db: Session, id: int):
    pokemon = db.query(Pokemon).filter(Pokemon.id == id).first()
    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokemon not found.")

    db.delete(pokemon)
    db.commit()
    return {"message": "Pokemon deleted successfully."}

def get_pokemon_by_id(db: Session, id: int):
    pokemon = db.query(Pokemon).filter(Pokemon.id == id).first()
    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokemon not found.")
    return pokemon

def import_pokemon_data(db: Session, file: bytes):
    data = pd.read_csv(io.BytesIO(file))
    for _, row in data.iterrows():
        pokemon_data = row.to_dict()
        if not db.query(Pokemon).filter(Pokemon.name == pokemon_data["name"]).first():
            new_pokemon = Pokemon(**pokemon_data)
            db.add(new_pokemon)
    db.commit()
    return {"message": "Pokemon data imported successfully."}