# ==========================================
# ML COPY
# Serviço autenticação OAuth Mercado Livre
# ==========================================

import webbrowser
import urllib.parse

from api.mercado_livre import MercadoLivreAPI
from services.account_service import AccountService
from services.oauth_service import OAuthService

from config import (
    CLIENT_ID,
    CLIENT_SECRET,
    REDIRECT_URI
)


class AuthService:


    AUTH_URL = (
        "https://auth.mercadolivre.com.br/authorization"
    )


    def __init__(self):

        self.api = MercadoLivreAPI()

        self.account_service = AccountService()

        self.oauth_service = OAuthService()


    # ======================================

    def get_authorization_url(self):

        params = {

            "response_type": "code",

            "client_id": CLIENT_ID,

            "redirect_uri": REDIRECT_URI

        }


        return (

            self.AUTH_URL
            + "?"
            + urllib.parse.urlencode(params)

        )


    # ======================================

    def open_login(self):

        url = self.get_authorization_url()

        print(url)

        webbrowser.open_new(url)


    # ======================================

    def authenticate(self, authorization_code):


        token = self.api.get_access_token(

            authorization_code,

            CLIENT_ID,

            CLIENT_SECRET,

            REDIRECT_URI

        )


        user = self.api.get_me(

            token["access_token"]

        )


        account = {

            "user_id":
            user["id"],


            "nickname":
            user["nickname"],


            "access_token":
            token["access_token"],


            "refresh_token":
            token["refresh_token"],


            "expires_in":
            token["expires_in"]

        }


        self.account_service.save_account(
            account
        )


        return account


    # ======================================

    def login_and_save(self):

        print(
            "Aguardando autorização Mercado Livre..."
        )


        code = None


        while code is None:

            code = self.oauth_service.get_code()


        print(
            "Código recebido:"
        )

        print(code)


        return self.authenticate(code)