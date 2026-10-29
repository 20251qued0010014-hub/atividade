from flask import Flask, jsonify, request

app = Flask(__name__)

id = 0
cursos_db = []

@app.route("/cursos")
def get():
    return jsonify(cursos_db)

@app.route("/cursos", methods=["POST"])
def post():
    global id
    id += 1
    dados = request.get_json()
    nome = dados.get("nome")
    instituicao = dados.get("instituicao")
    duracao = dados.get("duracao")
    curso = {"id": id, "nome": nome, "instituicao": instituicao, "duracao": duracao}
    cursos_db.append(curso)
    return jsonify(curso)

@app.route("/cursos/<int:id>", methods=["PUT"])
def put(id):
    dados = request.get_json()
    nome = dados.get("nome")
    instituicao = dados.get("instituicao")
    duracao = dados.get("duracao")
    for curso in cursos_db:
        if curso["id"] == id:
            curso["nome"] = nome
            curso["instituicao"] = instituicao
            curso["duracao"] = duracao
            return jsonify(curso)
    return jsonify({"erro": "Nenhum curso encontrado!"}), 404

@app.route("/cursos/<int:id>", methods=["DELETE"])
def delete(id):
    for curso in cursos_db:
        if curso["id"] == id:
            cursos_db.remove(curso)
            return "", 200
    return jsonify({"erro": "Nenhum curso encontrado!"}), 404

app.run(debug=True)
