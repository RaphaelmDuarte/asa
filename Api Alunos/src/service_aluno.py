from src.aluno import Aluno
from src.database import get, insert, update, getAll, delete

async def getById(alunoId: int):
    return await get(alunoId)

async def createStudant(aluno: Aluno):
    return await insert(aluno)

async def updateStudant(aluno: Aluno):
    await update(aluno)

async def getAllStudants():
    return await getAll()

async def deleteStudant(alunoId: int):
    return await delete(alunoId)