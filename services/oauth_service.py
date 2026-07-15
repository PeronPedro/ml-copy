# ==========================================
# ML COPY
# Serviço OAuth
# ==========================================

import requests
import time


class OAuthService:

    RENDER_URL = "https://ml-copy.onrender.com"

    def get_code(self):

        while True:

            response = requests.get(
                f"{self.RENDER_URL}/last_code"
            )

            response.raise_for_status()

            code = response.json().get("code")

            if code:
                return code

            time.sleep(2)