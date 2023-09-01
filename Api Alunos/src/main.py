from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from src.aluno import Aluno
from src.service_aluno import createStudant, getById, getAllStudants, updateStudant, deleteStudant

app = FastAPI()

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def default():
    with open("src/index.html", "r") as f:
        return f.read()

@app.get("/alunos", tags=["Alunos"])
async def get_all_alunos():
    alunos = await getAllStudants()
    return {
            "status": "SUCESS",
            "data": alunos
        }

@app.get("/alunos/{alunoId}", tags=["Alunos"])
async def get_aluno(alunoId: int):
    aluno = await getById(alunoId)
    return {
            "status": "SUCESS",
            "data": aluno
        }

@app.post("/alunos", tags=["Alunos"])
async def criar_aluno(aluno: Aluno):
    nwAluno = await createStudant(aluno)
    return {
            "status": "SUCESS",
            "data": nwAluno
        }

@app.put("/alunos", tags=["Alunos"])
async def update_aluno(aluno: Aluno):
    upAluno = await updateStudant(aluno)
    return {
            "status": "SUCESS",
            "data": upAluno
        }

@app.delete("/alunos/{alunoId}", tags=["Alunos"])
async def delete_aluno(alunoId: int):
    try:
        dlStudant = await deleteStudant(alunoId)
        return dlStudant
    except Exception as e:
        return {
            "status": "SUCESS",
            "data": "Erro ao deletar aluno!"
        }