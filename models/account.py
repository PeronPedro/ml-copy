from dataclasses import dataclass


@dataclass
class Account:

    id: int | None = None

    # Nome que você dará à conta dentro do ML COPY
    name: str = ""

    # Nome da conta no Mercado Livre
    nickname: str = ""

    # ID do usuário no Mercado Livre
    ml_user_id: str = ""

    # OAuth
    access_token: str = ""
    refresh_token: str = ""

    # Controle do token
    token_expiration: str = ""

    # Status da conexão
    connected: bool = False

    # Última sincronização de anúncios
    last_sync: str = ""