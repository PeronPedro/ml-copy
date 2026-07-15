# ==========================================
# ML COPY
# Serviço de autenticação Mercado Livre
# ==========================================

import time

from api.mercado_livre import MercadoLivreAPI
from services.oauth_service import OAuthService
from services.account_service import AccountService

from config import (
    CLIENT_ID,
    CLIENT_SECRET,
    REDIRECT_URI
)


class AuthService:

    def __init__(self):

        self.api = MercadoLivreAPI()
        self.oauth = OAuthService()
        self.account_service = AccountService()

    def open_login(self):

        import webbrowser
        import urllib.parse

        params = {
            "response_type": "code",
            "client_id": CLIENT_ID,
            "redirect_uri": REDIRECT_URI
        }

        url = (
            "https://auth.mercadolivre.com.br/authorization?"
            + urllib.parse.urlencode(params)
        )

        print(url)

        webbrowser.open(url)

    def login_and_save(self):

        print("Aguardando autorização Mercado Livre...")

        code = None

        while code is None:

            code = self.oauth.get_code()

            time.sleep(2)

        print("Código recebido:", code)

        return self.authenticate(code)

    def authenticate(self, authorization_code):

        token = self.api.get_access_token(
            authorization_code,
            CLIENT_ID,
            CLIENT_SECRET,
            REDIRECT_URI
        )

        access_token = token["access_token"]
        refresh_token = token["refresh_token"]
        expires_in = token["expires_in"]

        user = self.api.get_me(access_token)

        account = {
            "user_id": user["id"],
            "nickname": user["nickname"],
            "access_token": access_token,
            "refresh_token": refresh_token,
            "expires_in": expires_in
        }

        self.account_service.save_account(account)

        print("CONTA SALVA COM SUCESSO")

        return account