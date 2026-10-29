from flask import Flask, jsonify, request

app = Flask(__name__)

id = 0
cidades_db = []

@app.route("/cidades")
def get():
    return jsonify(cidades_db)

@app.route("/cidades", methods=["POST"])
def post():
    global id
    id +=1
    dados=request.get_json()
    pais = dados.get("pais")
    nome = dados.get("nome")
    prefeito = dados.get("prefeito")
    cidade = {"id": id, "pais": pais, "nome": nome, "prefeito": prefeito}
    cidades_db.append(cidade)
    return jsonify(cidade)

@app.route("/cidades/<int:id>", methods = ["PUT"])
def put(id):
    dados=request.get_json()
    pais = dados.get("pais")
    nome = dados.get("nome")
    prefeito = dados.get("prefeito")
    for cidade in cidades_db:
        if cidade["id"]== id:
            cidade["pais"]= pais
            cidade["nome"] = nome
            cidade["prefeito"] = prefeito
        return jsonify(cidade)
    return jsonify({"Erro. Nenhuma Cidade encontrado!"}), 404

@app.route("/cidades/<int:id>", methods = ["DELETE"])
def delete(id):
    for cidade in cidades_db:
        if cidade["id"]== id:
            cidades_db.remove(cidade)
        return "",200
    return jsonify({"Erro. Nenhuma Cidade encontrado!"}), 404

app.run(debug=True)