from src.aluno import Aluno

db = []
indice = [0]

async def get(alunoId: Aluno):
    index = await getIndex(alunoId)
    if (index == None):
        return
    return db[index]

async def getAll():
    return db

async def insert(new_aluno: Aluno):
    new_aluno.id = indice[0]
    db.append(new_aluno)
    indice[0] = indice[0] + 1
    return new_aluno

async def update(upAluno: Aluno):
    index = await getIndex(upAluno.id)
    db[index] = upAluno

async def delete(alunoId: int):
    index = await getIndex(alunoId)
    return db.pop(index)

async def getIndex(alunoId: int):
    for aluno in db:
        if aluno.id == alunoId:
            return db.index(aluno)
        