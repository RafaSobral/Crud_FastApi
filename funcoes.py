from database import conexao_banco
from model import Aluno

def cadastrar_aluno(aluno:  Aluno):
    conectar = conexao_banco()

    cursor = conectar.execute(
        """
        INSERT INTO alunos (nome, idade, curso, periodo)
        VALUES (?, ?, ?, ?)
        """,
        (aluno.nome, aluno.idade, aluno.curso, aluno.periodo)
    )

    conectar.commit()

    novo_Aluno = Aluno(
        id=cursor.lastrowid,
        nome=aluno.nome,
        idade=aluno.idade,
        curso=aluno.curso,
        periodo=aluno.periodo
    )

    conectar.close()

    return novo_Aluno


def listar_alunos():
    conectar = conexao_banco()
    
    resultado = conectar.execute(
            "SELECT id, nome, idade, curso, periodo FROM alunos"
        ).fetchall()

    conectar.close()

    alunos= []

    for row in resultado: 
        aluno = Aluno(
            id=row["id"],
            nome=row["nome"],
            idade=row["idade"],
            curso=row["curso"],
            periodo=row["periodo"]
        )

        alunos.append(aluno)

    return alunos


def selecionar_aluno(aluno_id: int):
    conectar = conexao_banco()

    row = conectar.execute(
        "SELECT id, nome, idade, curso, periodo FROM alunos WHERE id = ?",
        (aluno_id,)
    ).fetchone()


    conectar.close()

    if row is None:
        return None

    aluno = Aluno(
        id = row["id"],
        nome = row["nome"],
        idade = row["idade"],
        curso = row["curso"],
        periodo = row["periodo"]
    )

    return aluno

def atualizar_aluno(aluno_id: int, aluno: Aluno):
    conectar = conexao_banco()

    cursor = conectar.execute(
        """
        UPDATE alunos
        SET  nome = ?, idade = ?, curso = ?, periodo = ?
        WHERE id = ?
        """,
        (aluno.nome, aluno.idade, aluno.curso, aluno.periodo, aluno_id)
    )

    conectar.commit()
    conectar.close()

    aluno.id = aluno_id

    return aluno

def deletar_aluno(aluno_id: int):
    conectar = conexao_banco()

    cursor  = conectar.execute(
        "DELETE FROM alunos WHERE id = ?",
        (aluno_id,)
    )
    conectar.commit()
    conectar.close()


    
