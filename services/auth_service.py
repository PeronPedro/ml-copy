# ==========================================
# ML COPY
# Serviço de autenticação OAuth Mercado Livre
# ==========================================

import webbrowser

from api.mercado_livre import MercadoLivreAPI
from services.account_service import AccountService

from config import (
    CLIENT_ID,
    CLIENT_SECRET,
    REDIRECT_URI
)


class AuthService:

    AUTH_URL = "https://auth.mercadolivre.com.br/authorization"

    def __init__(self):

        self.api = MercadoLivreAPI()
        self.account_service = AccountService()


    def get_authorization_url(self):

        url = (
            f"{self.AUTH_URL}"
            f"?response_type=code"
            f"&client_id={CLIENT_ID}"
            f"&redirect_uri={REDIRECT_URI}"
        )

        return url


    def open_login(self):

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

    webbrowser.open_new(url)


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


        user = self.api.get_me(
            access_token
        )


        account = {

            "user_id": user["id"],
            "nickname": user["nickname"],
            "access_token": access_token,
            "refresh_token": refresh_token,
            "expires_in": expires_in

        }


        self.account_service.save_account(account)


        return account



    def refresh(self, refresh_token):

        token = self.api.refresh_token(
            refresh_token,
            CLIENT_ID,
            CLIENT_SECRET
        )

        return token