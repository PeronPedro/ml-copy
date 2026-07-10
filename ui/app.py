# ==========================================
# ML COPY
# Interface Principal
# ==========================================

import customtkinter as ctk

from config import (
    APP_NAME,
    APP_VERSION,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    THEME,
    APPEARANCE
)

from database import initialize_database

from ui.dashboard import DashboardView
from ui.accounts import AccountsView


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode(APPEARANCE)
        ctk.set_default_color_theme(THEME)

        initialize_database()

        self.title(f"{APP_NAME} - {APP_VERSION}")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.minsize(WINDOW_WIDTH, WINDOW_HEIGHT)

        self.current_view = None

        self.create_layout()

        self.show_dashboard()

    # ==================================================

    def create_layout(self):

        self.sidebar = ctk.CTkFrame(
            self,
            width=220,
            corner_radius=0
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        titulo = ctk.CTkLabel(
            self.sidebar,
            text="ML COPY",
            font=("Arial", 26, "bold")
        )

        titulo.pack(pady=(25, 5))

        versao = ctk.CTkLabel(
            self.sidebar,
            text=f"Versão {APP_VERSION}"
        )

        versao.pack(pady=(0, 20))

        ctk.CTkButton(
            self.sidebar,
            text="🏠 Dashboard",
            command=self.show_dashboard
        ).pack(fill="x", padx=15, pady=5)

        ctk.CTkButton(
            self.sidebar,
            text="👤 Contas",
            command=self.show_accounts
        ).pack(fill="x", padx=15, pady=5)

        ctk.CTkButton(
            self.sidebar,
            text="📦 Anúncios"
        ).pack(fill="x", padx=15, pady=5)

        ctk.CTkButton(
            self.sidebar,
            text="📤 Destinos"
        ).pack(fill="x", padx=15, pady=5)

        ctk.CTkButton(
            self.sidebar,
            text="⚙ Configurações"
        ).pack(fill="x", padx=15, pady=5)

        self.main = ctk.CTkFrame(self)

        self.main.pack(
            side="left",
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )

        self.status = ctk.CTkLabel(
            self,
            text="Sistema iniciado",
            anchor="w"
        )

        self.status.pack(
            side="bottom",
            fill="x",
            padx=10,
            pady=8
        )

    # ==================================================

    def clear_view(self):

        if self.current_view is not None:
            self.current_view.destroy()

    # ==================================================

    def show_dashboard(self):

        self.clear_view()

        self.current_view = DashboardView(self.main)

        self.current_view.pack(
            fill="both",
            expand=True
        )

        self.status.configure(
            text="Dashboard"
        )

    # ==================================================

    def show_accounts(self):

        self.clear_view()

        self.current_view = AccountsView(self.main)

        self.current_view.pack(
            fill="both",
            expand=True
        )

        self.status.configure(
            text="Gerenciador de Contas"
        )