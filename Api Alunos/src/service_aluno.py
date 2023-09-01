from src.aluno import Aluno
from src.database import db

async def getById(alunoId: int):
    return db[alunoId]

async def createStudant(aluno: Aluno):
    new_aluno = Aluno(
        id= aluno.id,
        nome= aluno.nome,
        matricula= aluno.matricula,
        cpf= aluno.cpf,
        endereco= aluno.endereco
    )
    new_aluno.id = len(db)
    db.append(new_aluno)
    return new_aluno

async def updateStudant(aluno: Aluno):
    db[aluno.id] = aluno

async def getAllStudants():
    return db

async def deleteStudant(alunoId: int):
    dlStudant = db.pop(alunoId)
    return dlStudant