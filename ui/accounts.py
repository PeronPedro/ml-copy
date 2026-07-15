# ==========================================
# ML COPY
# Tela de gerenciamento de contas
# ==========================================

import customtkinter as ctk

from services.auth_service import AuthService
from services.account_service import AccountService


class AccountsView(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.auth_service = AuthService()
        self.account_service = AccountService()

        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)


        titulo = ctk.CTkLabel(
            self,
            text="Gerenciador de Contas",
            font=("Arial", 28, "bold")
        )

        titulo.grid(
            row=0,
            column=0,
            padx=20,
            pady=(20, 10),
            sticky="w"
        )


        oauth_frame = ctk.CTkFrame(self)

        oauth_frame.grid(
            row=1,
            column=0,
            padx=20,
            pady=10,
            sticky="ew"
        )


        self.btn_conectar = ctk.CTkButton(
            oauth_frame,
            text="🔗 Conectar Mercado Livre",
            command=self.conectar_ml
        )

        self.btn_conectar.pack(
            padx=15,
            pady=15
        )


        self.lista = ctk.CTkScrollableFrame(self)

        self.lista.grid(
            row=3,
            column=0,
            padx=20,
            pady=10,
            sticky="nsew"
        )


        self.atualizar_lista()


    # ==================================

    def conectar_ml(self):

        print(
            "Iniciando autenticação Mercado Livre..."
        )

        self.auth_service.open_login()

        self.auth_service.login_and_save()

        self.atualizar_lista()


    # ==================================

    def atualizar_lista(self):

        for widget in self.lista.winfo_children():

            widget.destroy()


        contas = self.account_service.get_accounts()


        if not contas:

            ctk.CTkLabel(
                self.lista,
                text="Nenhuma conta cadastrada."
            ).pack(
                pady=20
            )

            return


        for conta in contas:

            frame = ctk.CTkFrame(
                self.lista
            )

            frame.pack(
                fill="x",
                pady=5
            )


            ctk.CTkLabel(
                frame,
                text=f"🟢 {conta[2]}",
                font=("Arial", 16)
            ).pack(
                side="left",
                padx=15,
                pady=12
            )


            ctk.CTkButton(
                frame,
                text="Excluir",
                width=90
            ).pack(
                side="right",
                padx=10
            )