"""Punto de entrada para Gunicorn en Render.

Se inicializa una sola vez la base de demostración si todavía no existe.
Nunca reinicializar una base con datos existentes.
"""
from pathlib import Path

from app import create_app
from app.db import init_db

app = create_app()

# En Render, montar el disco persistente en:
# /opt/render/project/src/instance
db_path = Path(app.config["DATABASE"])
if not db_path.is_file():
    with app.app_context():
        init_db()
