# ==========================================
# ML COPY
# Integração API Mercado Livre
# ==========================================

import requests


class MercadoLivreAPI:


    BASE_URL = "https://api.mercadolibre.com"



    def get_access_token(
        self,
        authorization_code,
        client_id,
        client_secret,
        redirect_uri
    ):

        url = "https://api.mercadolibre.com/oauth/token"


        data = {

            "grant_type": "authorization_code",
            "client_id": client_id,
            "client_secret": client_secret,
            "code": authorization_code,
            "redirect_uri": redirect_uri

        }


        response = requests.post(
            url,
            data=data
        )


        response.raise_for_status()


        return response.json()



    def refresh_token(
        self,
        refresh_token,
        client_id,
        client_secret
    ):

        url = "https://api.mercadolibre.com/oauth/token"


        data = {

            "grant_type": "refresh_token",
            "client_id": client_id,
            "client_secret": client_secret,
            "refresh_token": refresh_token

        }


        response = requests.post(
            url,
            data=data
        )


        response.raise_for_status()


        return response.json()



    def get_me(
        self,
        access_token
    ):

        url = f"{self.BASE_URL}/users/me"


        headers = {

            "Authorization":
            f"Bearer {access_token}"

        }


        response = requests.get(
            url,
            headers=headers
        )


        response.raise_for_status()


        return response.json()