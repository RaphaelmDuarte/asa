from pydantic import BaseModel

class Aluno(BaseModel):
    id: int
    nome: str
    matricula: str
    cpf: str
    endereco: str