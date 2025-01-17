from sqlalchemy import Column, Integer, String, Boolean
from database.connection import Base

class Pokemon(Base):
    __tablename__ = "pokemon"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)
    type1 = Column(String(50), nullable=False)
    type2 = Column(String(50), nullable=True)
    total = Column(Integer, nullable=False)
    hp = Column(Integer, nullable=False, default=0)
    attack = Column(Integer, nullable=False, default=0)
    defense = Column(Integer, nullable=False, default=0)
    spatk = Column(Integer, nullable=False, default=0)
    spdef = Column(Integer, nullable=False, default=0)
    speed = Column(Integer, nullable=False, default=0)
    generation = Column(Integer, nullable=False)
    legendary = Column(Boolean, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "type1": self.type1,
            "type2": self.type2,
            "total": self.total,
            "hp": self.hp,
            "attack": self.attack,
            "defense": self.defense,
            "spatk": self.spatk,
            "spdef": self.spdef,
            "speed": self.speed,
            "generation": self.generation,
            "legendary": self.legendary,
        }