from flask import Flask, jsonify, request

app = Flask(__name__)

id = 0
carros_db = []

@app.route("/carros")
def get():
    return jsonify(carros_db)

@app.route("/carros", methods = ["POST"])
def post():
    global id
    id +=1
    dados = request.get_json()
    ano = dados.get("ano")
    marca = dados.get("marca")
    modelo = dados.get("modelo")
    carro = {"id": id, "ano": ano, "marca": marca, "modelo": modelo}
    carros_db.append(carro)
    return jsonify(carro)

@app.route("/carros/<int:id>", methods = ["PUT"])
def put(id):
    dados = request.get_json()
    ano = dados.get("ano")
    marca = dados.get("marca")
    modelo = dados.get("modelo")
    for carro in carros_db:
        if carro["id"] == id:
            carro["marca"] = marca
            carro["ano"] = ano
            carro["modelo"] = modelo
        return jsonify(carro)
    return jsonify({"Erro. Nenhum Carro encontrado!"}), 404

@app.route("/carros/<int:id>", methods = ["DELETE"])
def delete(id):
    for carro in carros_db:
        if carro["id"] == id:
            carros_db.remove(carro)
        return "", 200
    return jsonify({"Erro. Nenhum Carro encontrado!"}), 404

app.run(debug=True)
