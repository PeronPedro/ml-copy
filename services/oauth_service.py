# ==========================================
# ML COPY
# Serviço OAuth
# ==========================================

import requests


class OAuthService:

    RENDER_URL = "https://ml-copy.onrender.com"


    def get_code(self):

        url = f"{self.RENDER_URL}/last_code"


        response = requests.get(
            url
        )


        response.raise_for_status()


        data = response.json()


        return data.get("code")