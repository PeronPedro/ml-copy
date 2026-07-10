# ==========================================
# ML COPY
# Serviço de contas
# ==========================================

from database import get_connection


class AccountService:


    def save_account(self, account):

        connection = get_connection()

        cursor = connection.cursor()


        cursor.execute(
            """
            INSERT INTO accounts
            (
                user_id,
                nickname,
                access_token,
                refresh_token,
                expires_in
            )
            VALUES
            (
                ?,
                ?,
                ?,
                ?,
                ?
            )

            ON CONFLICT(user_id)
            DO UPDATE SET

                nickname = excluded.nickname,
                access_token = excluded.access_token,
                refresh_token = excluded.refresh_token,
                expires_in = excluded.expires_in

            """,

            (
                account["user_id"],
                account["nickname"],
                account["access_token"],
                account["refresh_token"],
                account["expires_in"]
            )
        )


        connection.commit()

        connection.close()



    def get_accounts(self):

        connection = get_connection()

        cursor = connection.cursor()


        cursor.execute(
            """
            SELECT
                id,
                user_id,
                nickname,
                access_token,
                refresh_token,
                expires_in

            FROM accounts

            ORDER BY id DESC

            """
        )


        accounts = cursor.fetchall()


        connection.close()


        return accounts



    def get_account_by_user_id(
        self,
        user_id
    ):

        connection = get_connection()

        cursor = connection.cursor()


        cursor.execute(
            """
            SELECT *

            FROM accounts

            WHERE user_id = ?

            """,
            (
                user_id,
            )
        )


        account = cursor.fetchone()


        connection.close()


        return account