from src.aluno import Aluno
from src.database import get, insert, update, getAll, delete

async def getById(alunoId: int):
    return await get(alunoId)

async def createStudant(aluno: Aluno):
    new_aluno = Aluno(
        id= aluno.id,
        nome= aluno.nome,
        matricula= aluno.matricula,
        cpf= aluno.cpf,
        endereco= aluno.endereco
    )
    return await insert(new_aluno)

async def updateStudant(aluno: Aluno):
    await update(aluno)

async def getAllStudants():
    return await getAll()

async def deleteStudant(alunoId: int):
    return await delete(alunoId)