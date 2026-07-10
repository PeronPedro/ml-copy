from ui.app import App
from banco import criar_tabelas


if __name__ == "__main__":
    criar_tabelas()

    app = App()
    app.mainloop()