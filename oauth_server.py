from flask import Flask, request, jsonify

app = Flask(__name__)

last_code = None


@app.route("/")
def home():
    return "ML COPY OAuth Server Online"


@app.route("/callback")
def callback():
    global last_code

    code = request.args.get("code")

    if not code:
        return "Nenhum código recebido."

    last_code = code

    return """
    <h2>Conta conectada com sucesso</h2>
    <p>Pode fechar esta janela.</p>
    """


@app.route("/last_code")
def last_code_route():
    global last_code

    return jsonify({
        "code": last_code
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)