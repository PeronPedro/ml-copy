# ==========================================
# ML COPY
# Serviço de contas
# ==========================================

from database import get_connection


class AccountService:

    # =====================================================

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

    # =====================================================

    def get_accounts(self):

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *

            FROM accounts

            ORDER BY nickname
            """
        )

        accounts = cursor.fetchall()

        connection.close()

        return accounts

    # =====================================================

    def get_account_by_user_id(self, user_id):

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *

            FROM accounts

            WHERE user_id = ?
            """,
            (user_id,)
        )

        account = cursor.fetchone()

        connection.close()

        return account

    # =====================================================
    # CONTA DOADORA
    # =====================================================

    def set_donor(self, user_id):

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            UPDATE accounts
            SET role='DESTINATION'
            """
        )

        cursor.execute(
            """
            UPDATE accounts
            SET role='DONOR'
            WHERE user_id=?
            """,
            (user_id,)
        )

        connection.commit()

        connection.close()

    # =====================================================

    def get_donor(self):

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *

            FROM accounts

            WHERE role='DONOR'

            LIMIT 1
            """
        )

        account = cursor.fetchone()

        connection.close()

        return account

    # =====================================================

    def get_destinations(self):

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *

            FROM accounts

            WHERE role='DESTINATION'

            ORDER BY nickname
            """
        )

        accounts = cursor.fetchall()

        connection.close()

        return accounts