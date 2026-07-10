import sqlite3


BANCO = "ml_copy.db"


def conectar():
    return sqlite3.connect(BANCO)


def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        tipo TEXT NOT NULL,
        perfil_chrome TEXT,
        status TEXT DEFAULT 'Ativa',
        data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conexao.commit()
    conexao.close()


def listar_contas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM contas
    ORDER BY id DESC
    """)

    dados = cursor.fetchall()

    conexao.close()

    return dados


def adicionar_conta(nome, tipo, perfil):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO contas
    (nome, tipo, perfil_chrome)
    VALUES (?, ?, ?)
    """, (nome, tipo, perfil))

    conexao.commit()
    conexao.close()


def remover_conta(id_conta):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    DELETE FROM contas WHERE id = ?
    """, (id_conta,))

    conexao.commit()
    conexao.close()