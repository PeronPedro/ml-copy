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


    print(
        "Código recebido:",
        code
    )


    return """
    <h2>Autorização realizada com sucesso.</h2>
    <p>Pode fechar esta janela.</p>
    """



@app.route("/last_code")
def last_code_route():

    global last_code


    if last_code is None:

        return jsonify({
            "code": None
        })


    code = last_code


    last_code = None


    return jsonify({
        "code": code
    })



if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )