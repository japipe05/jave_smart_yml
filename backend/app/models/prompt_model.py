# models.py
from sqlalchemy import Column, Integer, String
from app.database.postgres import Base  # Asegúrate de que database.py tiene el Base que ya mostraste

class Prompt(Base):
    __tablename__ = "prompts"

    id = Column(Integer, primary_key=True, index=True)
    opcion = Column(String, index=True)
    descripcion = Column(String)
