from fastapi import FastAPI
from classes import Request_Aluno
from models import Aluno, session

app = FastAPI()

@app.get("/")
async def root():
	return {
		"status":"Sucess",
		"data":"No data"
}

@app.get("/alunos")
async def get_all_alunos():
	alunos_query = session.query(Aluno)
	alunos = alunos_query.all()
	return {
			"STATUS": "SUCESS",
			"data": alunos
  }

@app.post("/alunos")
async def criar_aluno(request_aluno: Request_Aluno):
	aluno_json = request_aluno
	print(aluno_json.nome)

	aluno = Aluno(
		nome = aluno_json.nome,
		email = aluno_json.email,
		cpf = aluno_json.cpf,
		endereco = aluno_json.endereco
	)
	session.add(aluno)
	session.commit()
	
	return {
	  "status": "SUCESS",
    "data": aluno_json
  }

@app.put("/alunos")
async def alterar_aluno(request_aluno: Request_Aluno):
    aluno_json = request_aluno
    aluno_query = session.query(Aluno).filter(
        Aluno.id==aluno_json.id
    )
    aluno = aluno_query.first()
    print(aluno.nome)
    aluno.nome = aluno_json.nome
    aluno.cpf = aluno_json.cpf
    aluno.email = aluno_json.email
    aluno.endereco = aluno_json.endereco

    session.add(aluno)
    session.commit()

    return {
        "status": "SUCESS",
        "data": aluno_json
    }
