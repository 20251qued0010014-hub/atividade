from flask import Flask, jsonify, request

app = Flask(__name__)

id = 0
jogos_db = []

@app.route("/jogos")
def get():
    return jsonify(jogos_db)

@app.route("/jogos", methods = ["POST"])
def post():
    global id
    id += 1
    dados = request.get_json()
    nome = dados.get("nome")
    genero = dados.get("genero")
    ano = dados.get("ano")
    jogo = {"id": id, "nome": nome, "genero": genero, "ano": ano}
    jogos_db.append(jogo)
    return jsonify(jogo)

@app.route("/jogos/<int:id>", methods = ["PUT"])
def put(id):
    dados = request.get_json()
    nome = dados.get("nome")
    genero = dados.get("genero")
    ano = dados.get("ano")
    for jogo in jogos_db:
        if jogo["id"] == id:
            jogo["nome"] = nome
            jogo["genero"] = genero
            jogo["ano"] = ano
        return jsonify(jogo)
    return jsonify({"Erro. Nenhum Jogo encontrado!"}), 404

@app.route("/jogos/<int:id>", methods = ["DELETE"])
def delete(id):
    for jogo in jogos_db:
        if jogo["id"] == id:
            jogos_db.remove(jogo)
        return "",200
    return jsonify({"Erro. Nenhum Jogo encontrado!"}), 404

app.run(debug=True)

                 

