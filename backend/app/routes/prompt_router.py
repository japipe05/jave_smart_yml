from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.services.prompt_service import obtener_prompt

router = APIRouter()

# Dependency para obtener DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/generar-prompt")
def generar_prompt(prompt_name: str, introduccion: str, db: Session = Depends(get_db)):
    try:
        cuerpo_prompt = obtener_prompt(db, prompt_name)
        prompt_final = f"Introducción: {introduccion}\n{cuerpo_prompt}"
        return {"prompt": prompt_final}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
