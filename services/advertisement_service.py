# ==========================================
# ML COPY
# Serviço de anúncios Mercado Livre
# ==========================================

from api.mercado_livre import MercadoLivreAPI
from services.account_service import AccountService


class AdvertisementService:


    def __init__(self):

        self.api = MercadoLivreAPI()

        self.account_service = AccountService()



    def get_last_ads(self):

        account = self.account_service.get_donor()


        if not account:

            print(
                "Nenhuma conta doadora encontrada."
            )

            return []



        user_id = account["user_id"]

        access_token = account["access_token"]



        anuncios = self.api.get_user_items(

            user_id,

            access_token

        )


        return anuncios[:50]