# ==========================================
# ML COPY
# OAuth Local Mercado Livre
# ==========================================

from flask import Flask, request
import threading

from services.auth_service import AuthService


app = Flask(__name__)

auth_service = AuthService()


@app.route("/")
def home():

    return "ML COPY OAuth Local Online"


@app.route("/callback")
def callback():

    code = request.args.get("code")

    if not code:

        return "Nenhum código recebido."


    print("Código recebido:")
    print(code)


    try:

        account = auth_service.authenticate(code)


        return f"""
        <h2>Conta conectada com sucesso!</h2>

        <p>
        Usuário:
        {account["nickname"]}
        </p>

        <p>
        Pode fechar esta janela.
        </p>
        """


    except Exception as erro:

        print(erro)


        return f"""
        <h2>Erro ao conectar conta</h2>

        <p>{erro}</p>
        """



def iniciar_oauth_server():

    thread = threading.Thread(

        target=lambda:
        app.run(
            host="127.0.0.1",
            port=8080,
            debug=False,
            use_reloader=False
        ),

        daemon=True

    )

    thread.start()