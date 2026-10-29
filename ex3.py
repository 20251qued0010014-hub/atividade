from flask import Flask, jsonify, request

app = Flask(__name__)

id = 0
musicas_db = []

@app.route("/musicas")
def get():
    return jsonify(musicas_db)

@app.route("/musicas", methods = ["POST"])
def post():
    global id
    id +=1
    dados = request.get_json()
    ano = dados.get("ano")
    artista = dados.get("artista")
    nome = dados.get("nome")
    musica = {"id": id, "nome": nome, "artista":artista, "ano": ano}
    musicas_db.append(musica)
    return jsonify(musica)

@app.route("/musicas/<int:id>", methods = ["PUT"])
def put(id):
    dados = request.get_json()
    ano = dados.get("ano")
    artista = dados.get("artista")
    nome = dados.get("nome")
    for musica in musicas_db:
        if musica["id"] == id:
            musica["ano"] = ano
            musica["artista"] = artista
            musica["nome"] = nome
            return jsonify(musica), 200
    return jsonify({"Erro. Nenhuma música encontrada"}), 404

@app.route("/musicas/<int:id>", methods = ["DELETE"])
def delete(id):
    for musica in musicas_db:
        if musica["id"] == id:
             musicas_db.remove(musica)
        return "", 204
    return jsonify({"erro": "Música não encontrado"}), 404

app.run(debug=True)
