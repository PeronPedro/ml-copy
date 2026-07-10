import customtkinter as ctk


class DashboardView(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure((0, 1), weight=1)

        titulo = ctk.CTkLabel(
            self,
            text="Dashboard",
            font=("Arial", 28, "bold")
        )
        titulo.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 30), sticky="w")

        self.criar_card(1, 0, "Contas conectadas", "0")
        self.criar_card(1, 1, "Anúncios ativos", "0")
        self.criar_card(2, 0, "Conta doadora", "Nenhuma")
        self.criar_card(2, 1, "Última sincronização", "-")

    def criar_card(self, linha, coluna, titulo, valor):

        frame = ctk.CTkFrame(self)

        frame.grid(
            row=linha,
            column=coluna,
            padx=15,
            pady=15,
            sticky="nsew"
        )

        ctk.CTkLabel(
            frame,
            text=titulo,
            font=("Arial", 16)
        ).pack(pady=(15, 5))

        ctk.CTkLabel(
            frame,
            text=valor,
            font=("Arial", 28, "bold")
        ).pack(pady=(0, 20))