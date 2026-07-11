from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    return "ML COPY OAuth Server Online"


@app.route("/callback")
def callback():

    code = request.args.get("code")

    if not code:
        return "Nenhum código recebido."

    print("Authorization Code:", code)

    return f"""
    <h2>Autorização realizada com sucesso.</h2>
    <p>Code:</p>
    <textarea rows="8" cols="90">{code}</textarea>
    <br><br>
    Pode fechar esta janela.
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)