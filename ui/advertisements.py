# ==========================================
# ML COPY
# Tela de anúncios
# ==========================================

import customtkinter as ctk

from services.advertisement_service import AdvertisementService


class AdvertisementsView(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.service = AdvertisementService()

        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # =====================================
        # Título
        # =====================================

        titulo = ctk.CTkLabel(
            self,
            text="Últimos anúncios",
            font=("Arial", 28, "bold")
        )

        titulo.grid(
            row=0,
            column=0,
            padx=20,
            pady=(20, 10),
            sticky="w"
        )

        # =====================================
        # Barra superior
        # =====================================

        top = ctk.CTkFrame(self)

        top.grid(
            row=1,
            column=0,
            padx=20,
            pady=10,
            sticky="ew"
        )

        ctk.CTkButton(
            top,
            text="Buscar últimos 50 anúncios",
            command=self.carregar_anuncios
        ).pack(
            side="left",
            padx=10,
            pady=10
        )

        # =====================================
        # Lista
        # =====================================

        self.lista = ctk.CTkScrollableFrame(self)

        self.lista.grid(
            row=2,
            column=0,
            padx=20,
            pady=10,
            sticky="nsew"
        )

    # =====================================

    def carregar_anuncios(self):

        for widget in self.lista.winfo_children():
            widget.destroy()

        try:

            anuncios = self.service.get_last_items(50)

            if len(anuncios) == 0:

                ctk.CTkLabel(
                    self.lista,
                    text="Nenhum anúncio encontrado."
                ).pack(pady=20)

                return

            for item_id in anuncios:

                frame = ctk.CTkFrame(self.lista)

                frame.pack(
                    fill="x",
                    padx=5,
                    pady=4
                )

                ctk.CTkCheckBox(
                    frame,
                    text=item_id
                ).pack(
                    side="left",
                    padx=15,
                    pady=10
                )

        except Exception as erro:

            ctk.CTkLabel(
                self.lista,
                text=str(erro)
            ).pack(
                pady=20
            )