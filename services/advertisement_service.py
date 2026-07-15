# ==========================================
# ML COPY
# Serviço de anúncios
# ==========================================

from api.mercado_livre import MercadoLivreAPI
from services.account_service import AccountService


class AdvertisementService:

    def __init__(self):

        self.api = MercadoLivreAPI()
        self.account_service = AccountService()

    # ======================================

    def get_last_items(self, limit=50):

        donor = self.account_service.get_donor()

        print("DONOR:")
        print(donor)

        if donor is None:
            return []

        data = self.api.get_my_items(
            donor["access_token"],
            donor["user_id"],
            limit=limit,
            offset=0
        )

        print("RESPOSTA API:")
        print(data)

        if "results" not in data:
            return []

        return data["results"]