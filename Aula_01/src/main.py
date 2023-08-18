from fastapi import FastAPI
from pydantic import BaseModel
from logging.config import dictConfig
import logging
from src.config import log_config

dictConfig(log_config)

app = FastAPI(debug = True)
logger = logging.getLogger('foo-logger')

class Aluno(BaseMode1):
    nome: str
    matricula: str
    curso: str


@app.get("/")
async def root():
    logger.debug()



@app.get("/parametro/{parametro_id}")
async def mostra_parametro(parametro_id):
    mensagem = f"O valor do parametro - {parametro_id}"
    