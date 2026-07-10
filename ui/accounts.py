# ==========================================
# ML COPY
# Tela de gerenciamento de contas
# ==========================================

import customtkinter as ctk

from services.auth_service import AuthService


class AccountsView(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.auth_service = AuthService()

        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)


        # ---------------- Título ----------------

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


        # ---------------- OAuth Mercado Livre ----------------

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


        # ---------------- Cadastro manual ----------------

        cadastro = ctk.CTkFrame(self)

        cadastro.grid(
            row=2,
            column=0,
            padx=20,
            pady=10,
            sticky="ew"
        )


        ctk.CTkLabel(
            cadastro,
            text="Apelido da conta"
        ).pack(
            anchor="w",
            padx=15,
            pady=(15, 5)
        )


        self.entry_nome = ctk.CTkEntry(
            cadastro,
            placeholder_text="Ex.: Principal"
        )

        self.entry_nome.pack(
            fill="x",
            padx=15
        )


        self.btn_adicionar = ctk.CTkButton(
            cadastro,
            text="+ Adicionar Conta",
            command=self.adicionar_conta
        )

        self.btn_adicionar.pack(
            padx=15,
            pady=15
        )


        # ---------------- Lista ----------------

        self.lista = ctk.CTkScrollableFrame(self)

        self.lista.grid(
            row=3,
            column=0,
            padx=20,
            pady=10,
            sticky="nsew"
        )


        self.atualizar_lista()



    # =====================================================

    def conectar_ml(self):

        print("Abrindo autenticação Mercado Livre...")

        self.auth_service.open_login()



    # =====================================================

    def atualizar_lista(self):

        for widget in self.lista.winfo_children():
            widget.destroy()


        exemplo = [
            "Principal",
            "Loja A",
            "Loja B"
        ]


        for nome in exemplo:

            frame = ctk.CTkFrame(
                self.lista
            )

            frame.pack(
                fill="x",
                pady=5
            )


            ctk.CTkLabel(
                frame,
                text="🟢 " + nome,
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



    # =====================================================

    def adicionar_conta(self):

        nome = self.entry_nome.get()


        if nome.strip() == "":
            return


        print("Nova conta:", nome)


        self.entry_nome.delete(
            0,
            "end"
        )