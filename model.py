import sqlite3 

DATABASE_NAME = "bancoAlunos.db"

def conexao_banco():
    conectar = sqlite3.connect(DATABASE_NAME)
    conectar.row_factory = sqlite3.Row
    return conectar

def criar_tabela_alunos():
    conectar = conexao_banco()

    conectar.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            curso TEXT NOT NULL,
            periodo INTEGER NOT NULL
        ) 
""")

    conectar.commit()
    conectar.close()





    