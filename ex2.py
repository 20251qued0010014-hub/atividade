from flask import Flask, jsonify, request

app = Flask(__name__)

id = 0
alunos_db = []

@app.route('/alunos')
def retornar_filmes():
    return jsonify(alunos_db)

@app.route("/alunos", methods=["POST"])
def postar():
    global id
    id = id+1
    dados = request.get_json()
    nome = dados.get("nome")
    curso = dados.get("curso")
    idade = dados.get("idade")
    aluno = {"id": id, "curso": curso, "nome": nome, "idade":idade}
    alunos_db.append(aluno)
    return jsonify(aluno)

@app.route("/alunos/<int:id>", methods=["PUT"])
def att(id):
    dados = request.get_json()
    nome = dados.get("nome")
    curso = dados.get("curso")
    idade = dados.get("idade")
    for aluno in alunos_db:
        if aluno["id"] == id:
            aluno["nome"]= nome
            aluno["idade"] = idade
            aluno["curso"] = curso
            return jsonify(aluno), 200
    return jsonify({"erro": "Aluno Não encontrado"}), 404

@app.route("/alunos/<int:id>", methods=["DELETE"])
def remover(id):
    for aluno in alunos_db:
        if aluno["id"] == id:
            alunos_db.remove(aluno)
        return '', 204
    return jsonify({"erro": "Aluno não encontrado"}), 404
    
    
app.run(debug=True)