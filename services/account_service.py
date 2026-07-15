# ==========================================
# ML COPY
# Serviço de contas
# ==========================================

from database import get_connection


class AccountService:


    def save_account(self, account):

        conn = get_connection()

        cursor = conn.cursor()


        cursor.execute(
            """
            INSERT INTO accounts
            (
                user_id,
                nickname,
                access_token,
                refresh_token,
                expires_in,
                role
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                account["user_id"],
                account["nickname"],
                account["access_token"],
                account["refresh_token"],
                account["expires_in"],
                "donor"
            )
        )


        conn.commit()

        conn.close()



    def get_accounts(self):

        conn = get_connection()

        cursor = conn.cursor()


        cursor.execute(
            """
            SELECT *
            FROM accounts
            """
        )


        rows = cursor.fetchall()

        conn.close()


        return rows



    def get_donor(self):

        conn = get_connection()

        cursor = conn.cursor()


        cursor.execute(
            """
            SELECT *
            FROM accounts
            WHERE role='donor'
            LIMIT 1
            """
        )


        row = cursor.fetchone()

        conn.close()


        if not row:

            return None


        return {

            "id": row[0],

            "user_id": row[1],

            "nickname": row[2],

            "access_token": row[3],

            "refresh_token": row[4],

            "expires_in": row[5]

        }