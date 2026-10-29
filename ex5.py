from flask import Flask, jsonify, request

app = Flask(__name__)

id = 0
produtos_db = []

@app.route("/produtos")
def get():
    return jsonify(produtos_db)

@app.route("/produtos", methods = ["POST"])
def post():
    global id
    id +=1
    dados = request.get_json()
    nome = dados.get("nome")
    preco = dados.get("preco")
    categoria = dados.get("categoria")
    produto = {"id":id,"nome": nome, "preco": preco, "categoria": categoria}
    produtos_db.append(produto)
    return jsonify(produto)

@app.route("/produtos/<int:id>", methods =["PUT"])
def put(id):
    dados = request.get_json()
    nome = dados.get("nome")
    preco = dados.get("preco")
    categoria = dados.get("categoria")
    for produto in produtos_db:
        if produto["id"] == id:
            produto["nome"] = nome
            produto["preco"] = preco
            produto["categoria"] = categoria
        return jsonify(produto)
    return jsonify({"Erro. Nenhum Produto encontrado!"}), 404

@app.route("/produtos/<int:id>", methods =["DELETE"])
def delete(id):
    for produto in produtos_db:
        if produto["id"] == id:
            produtos_db.remove(produto)
        return "",200
    return jsonify({"Erro. Nenhum Produto encontrado!"}), 404         

app.run(debug=True)


