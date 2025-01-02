import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_DIR = BASE_DIR / "db"
ARQUIVO_DB = DB_DIR / "flashcards.json"

DB_DIR.mkdir(parents=True, exist_ok=True)

def inicializar_db():
    if not ARQUIVO_DB.exists():
        with open(ARQUIVO_DB, "w") as f:
            json.dump({}, f)

def carregar_flashcards():
    with open(ARQUIVO_DB, "r") as f:
        return json.load(f)

def salvar_flashcards(data):
    with open(ARQUIVO_DB, "w") as f:
        json.dump(data, f, indent=4)
