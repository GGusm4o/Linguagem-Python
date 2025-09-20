"""Sistema de cadastro de palavras-chave e links de livros de uma autora na Amazon.

O módulo fornece uma camada simples de persistência utilizando SQLite para
armazenar associações entre palavras-chave utilizadas em campanhas ou
pesquisas e os links dos livros correspondentes da autora na Amazon. Ele pode
ser executado como um script interativo de linha de comando ou importado em
outros projetos.

Principais funcionalidades:

* criação automática do banco de dados;
* cadastro de novas palavras-chave vinculadas ao link do livro;
* listagem de todas as entradas cadastradas para a autora informada;
* busca por palavras-chave utilizando trechos do termo;
* atualização do link associado a uma palavra-chave;
* remoção de palavras-chave cadastradas.

Exemplo de execução direta pelo terminal::

    $ python sistema_livros_amazon.py

"""

from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Optional

# Caminho padrão para o arquivo de banco de dados. O arquivo é criado no
# mesmo diretório do módulo para facilitar o transporte do sistema.
BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "dados_livros_amazon.db"

# Nome utilizado quando o usuário não informa uma autora específica na
# interface de linha de comando.
AUTORA_PADRAO = "Autora da Amazon"


def _conectar() -> sqlite3.Connection:
    """Cria e retorna uma conexão com o banco de dados SQLite."""

    return sqlite3.connect(DB_PATH)


def inicializar_banco() -> None:
    """Cria a tabela principal caso ela ainda não exista."""

    with _conectar() as conexao:
        conexao.execute(
            """
            CREATE TABLE IF NOT EXISTS livros_autora (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                autora TEXT NOT NULL,
                palavra_chave TEXT NOT NULL,
                link TEXT NOT NULL,
                UNIQUE (autora, palavra_chave)
            )
            """
        )


@dataclass
class RegistroLivro:
    """Representa uma palavra-chave vinculada a um livro da autora."""

    id: int
    autora: str
    palavra_chave: str
    link: str


def adicionar_palavra_chave(autora: str, palavra_chave: str, link: str) -> None:
    """Insere uma nova palavra-chave para a autora.

    Args:
        autora: Nome da autora na Amazon.
        palavra_chave: Palavra-chave utilizada na busca ou divulgação.
        link: URL do livro correspondente na Amazon.

    Raises:
        ValueError: Caso a palavra-chave ou o link estejam vazios ou o link
            não aparente apontar para um endereço da Amazon.
    """

    palavra_chave = palavra_chave.strip()
    link = link.strip()

    if not palavra_chave:
        raise ValueError("A palavra-chave não pode ser vazia.")

    if not link:
        raise ValueError("O link do livro não pode ser vazio.")

    if "amazon." not in link:
        raise ValueError(
            "O link informado não parece ser um endereço da Amazon."
        )

    with _conectar() as conexao:
        try:
            conexao.execute(
                """
                INSERT INTO livros_autora (autora, palavra_chave, link)
                VALUES (?, ?, ?)
                """,
                (autora, palavra_chave, link),
            )
        except sqlite3.IntegrityError as exc:
            raise ValueError(
                "Já existe uma entrada para esta palavra-chave." \
                " Atualize o registro existente em vez de duplicá-lo."
            ) from exc


def listar_palavras_chave(autora: str) -> List[RegistroLivro]:
    """Retorna todos os registros cadastrados para a autora."""

    with _conectar() as conexao:
        cursor = conexao.execute(
            """
            SELECT id, autora, palavra_chave, link
            FROM livros_autora
            WHERE autora = ?
            ORDER BY palavra_chave COLLATE NOCASE
            """,
            (autora,),
        )
        registros = [RegistroLivro(*linha) for linha in cursor.fetchall()]
    return registros


def buscar_por_palavra(autora: str, termo: str) -> List[RegistroLivro]:
    """Busca registros que contenham o termo informado na palavra-chave."""

    termo = f"%{termo.strip()}%"

    with _conectar() as conexao:
        cursor = conexao.execute(
            """
            SELECT id, autora, palavra_chave, link
            FROM livros_autora
            WHERE autora = ? AND palavra_chave LIKE ?
            ORDER BY palavra_chave COLLATE NOCASE
            """,
            (autora, termo),
        )
        registros = [RegistroLivro(*linha) for linha in cursor.fetchall()]

    return registros


def atualizar_link(registro_id: int, novo_link: str) -> None:
    """Atualiza o link associado a uma palavra-chave existente."""

    novo_link = novo_link.strip()
    if not novo_link:
        raise ValueError("O link do livro não pode ser vazio.")

    if "amazon." not in novo_link:
        raise ValueError("O link informado não parece ser um endereço da Amazon.")

    with _conectar() as conexao:
        linhas_atualizadas = conexao.execute(
            "UPDATE livros_autora SET link = ? WHERE id = ?",
            (novo_link, registro_id),
        ).rowcount

        if linhas_atualizadas == 0:
            raise ValueError("Nenhum registro foi encontrado com o ID informado.")


def remover_palavra_chave(registro_id: int) -> None:
    """Remove um registro do banco de dados."""

    with _conectar() as conexao:
        linhas_removidas = conexao.execute(
            "DELETE FROM livros_autora WHERE id = ?",
            (registro_id,),
        ).rowcount

        if linhas_removidas == 0:
            raise ValueError("Nenhum registro foi encontrado com o ID informado.")


def _exibir_registros(registros: Iterable[RegistroLivro]) -> None:
    """Imprime uma lista de registros em formato tabular simples."""

    registros = list(registros)
    if not registros:
        print("Nenhuma palavra-chave cadastrada.")
        return

    largura_palavra = max(len(r.palavra_chave) for r in registros) + 2
    largura_id = max(len("ID"), max(len(str(r.id)) for r in registros))

    cabecalho = f"{ 'ID'.ljust(largura_id) } | Palavra-chave".ljust(
        largura_id + 3 + largura_palavra
    ) + " | Link"
    separador = "-" * len(cabecalho)

    print(separador)
    print(cabecalho)
    print(separador)
    for registro in registros:
        print(
            f"{str(registro.id).ljust(largura_id)} | "
            f"{registro.palavra_chave.ljust(largura_palavra)} | {registro.link}"
        )
    print(separador)


def _solicitar_id() -> Optional[int]:
    """Solicita um ID numérico ao usuário, retornando ``None`` em branco."""

    valor = input("Informe o ID (ou deixe em branco para cancelar): ").strip()
    if not valor:
        return None

    try:
        return int(valor)
    except ValueError as exc:  # pragma: no cover - fluxo interativo
        raise ValueError("O ID deve ser um número inteiro.") from exc


def executar_interface() -> None:
    """Executa o menu interativo da aplicação."""

    inicializar_banco()
    autora = input(
        "Informe o nome da autora na Amazon (pressione Enter para usar o"
        f" padrão '{AUTORA_PADRAO}'): "
    ).strip() or AUTORA_PADRAO

    print(f"\nGerenciando palavras-chave para a autora: {autora}\n")

    opcoes = {
        "1": "Cadastrar nova palavra-chave",
        "2": "Listar todas as palavras-chave",
        "3": "Buscar palavra-chave",
        "4": "Atualizar link de uma palavra-chave",
        "5": "Remover palavra-chave",
        "0": "Sair",
    }

    while True:
        for chave, descricao in opcoes.items():
            print(f"[{chave}] {descricao}")

        escolha = input("\nSelecione uma opção: ").strip()
        print()

        try:
            if escolha == "1":
                palavra = input("Informe a palavra-chave: ")
                link = input("Informe o link do livro na Amazon: ")
                adicionar_palavra_chave(autora, palavra, link)
                print("Palavra-chave cadastrada com sucesso!\n")

            elif escolha == "2":
                registros = listar_palavras_chave(autora)
                _exibir_registros(registros)
                print()

            elif escolha == "3":
                termo = input("Digite parte da palavra-chave para busca: ")
                registros = buscar_por_palavra(autora, termo)
                _exibir_registros(registros)
                print()

            elif escolha == "4":
                registro_id = _solicitar_id()
                if registro_id is None:
                    print("Operação cancelada.\n")
                    continue

                novo_link = input("Informe o novo link do livro na Amazon: ")
                atualizar_link(registro_id, novo_link)
                print("Link atualizado com sucesso!\n")

            elif escolha == "5":
                registro_id = _solicitar_id()
                if registro_id is None:
                    print("Operação cancelada.\n")
                    continue

                remover_palavra_chave(registro_id)
                print("Registro removido com sucesso!\n")

            elif escolha == "0":
                print("Saindo do sistema. Até logo!")
                break

            else:
                print("Opção inválida. Tente novamente.\n")

        except ValueError as erro:
            print(f"Erro: {erro}\n")


if __name__ == "__main__":  # pragma: no cover - execução direta
    executar_interface()