from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from src.aluno import Aluno
from src.service_aluno import createStudant, getById, getAllStudants, updateStudant, deleteStudant

app = FastAPI()

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def default():
    with open("src/html/index.html", "r") as f:
        return f.read()

@app.get("/alunos", tags=["Alunos"])
async def get_all_alunos():
    alunos = await getAllStudants()
    return mensageSucess(alunos)

@app.get("/alunos/{alunoId}", tags=["Alunos"])
async def get_aluno(alunoId: int):
    aluno = await getById(alunoId)
    return mensageSucess(aluno)

@app.post("/alunos", tags=["Alunos"])
async def criar_aluno(aluno: Aluno):
    nwAluno = await createStudant(aluno)
    return mensageSucess(nwAluno)

@app.put("/alunos", tags=["Alunos"])
async def update_aluno(aluno: Aluno):
    upAluno = await updateStudant(aluno)
    return mensageSucess(upAluno)

@app.delete("/alunos/{alunoId}", tags=["Alunos"])
async def delete_aluno(alunoId: int):
    try:
        dlStudant = await deleteStudant(alunoId)
        return mensageSucess(dlStudant)
    except Exception as e:
        return mensageSucess("Erro ao deletar aluno!")
    
def mensageSucess(msg: str):
    return {
        "status": "SUCESS",
        "data": msg
    }