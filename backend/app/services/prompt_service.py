from sqlalchemy.orm import Session
from app.models.prompt_model import Prompt

def obtener_prompt(db: Session, prompt_name: str) -> str:
    prompt = db.query(Prompt).filter(Prompt.name == prompt_name).first()
    if not prompt:
        raise ValueError(f"Prompt '{prompt_name}' no encontrado.")
    return prompt.message
