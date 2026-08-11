from fastapi import APIRouter, Body, HTTPException

import funcoes
from model import Aluno

router = APIRouter(prefix="/alunos", tags=["alunos"])


def validar_aluno(nome, idade, curso, periodo):
    if not nome:
        raise HTTPException(status_code=400, detail="Digite o nome do aluno")

    if idade is None:
        raise HTTPException(status_code=400, detail="Digite a idade do aluno")
    try:
        idade = int(idade)
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="O campo idade deve ser um número inteiro.",
        )

    if not curso:
        raise HTTPException(status_code=400, detail="Digite o curso do aluno")

    if periodo is None:
        raise HTTPException(status_code=400, detail="Digite o período do aluno")
    try:
        periodo = int(periodo)
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="O campo período deve ser um número inteiro.",
        )

    return Aluno(
        nome=nome,
        idade=idade,
        curso=curso,
        periodo=periodo
    )


@router.post(
    "",
    summary="Criar aluno"
)
def cadastrar_aluno(
    nome: str = Body(...),
    idade: int = Body(...),
    curso: str = Body(...),
    periodo: int = Body(...)
):
    aluno = validar_aluno(nome, idade, curso, periodo)

    return funcoes.cadastrar_aluno(aluno)

@router.get(
    "",
    summary="Listar alunos"
)
def listar_alunos():
    return funcoes.listar_alunos()


@router.get(
    "/{aluno_id}",
    summary="Buscar aluno por ID"
)
def buscar_aluno(aluno_id: int):
    aluno = funcoes.selecionar_aluno(aluno_id)

    if aluno is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")

    return aluno


@router.put(
    "/{aluno_id}",
    summary="Atualizar aluno"
)
def atualizar_aluno(
    aluno_id: int,
    nome: str = Body(...),
    idade: int = Body(...),
    curso: str = Body(...),
    periodo: int = Body(...)
):

    aluno = validar_aluno(nome, idade, curso, periodo)

    aluno_atualizado = funcoes.atualizar_aluno(aluno_id, aluno)

    if aluno_atualizado is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")

    return aluno_atualizado


@router.delete(
    "/{aluno_id}",
    summary="Deletar aluno"
)
def deletar_aluno(aluno_id: int):
    aluno_deletado = funcoes.deletar_aluno(aluno_id)

    if not aluno_deletado:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")

    return {"mensagem": "Aluno deletado com sucesso"}
