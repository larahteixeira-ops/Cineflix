"""Conexão com o banco de dados (SQLite).

Todas as classes DAO (Etapa 2) vão usar a classe Database para obter conexões.
"""
import sqlite3

from config import DB_PATH, SCHEMA_PATH, SEED_PATH


class Database:
    def __init__(self, caminho=DB_PATH):
        self.caminho = caminho

    def conectar(self):
        """Abre uma conexão com chaves estrangeiras ativas e linhas acessíveis por nome."""
        conexao = sqlite3.connect(self.caminho)
        conexao.row_factory = sqlite3.Row
        conexao.execute("PRAGMA foreign_keys = ON")
        return conexao

    def inicializar(self, com_dados=True):
        """Recria as tabelas a partir de schema.sql e, opcionalmente, carrega seed.sql."""
        conexao = self.conectar()
        try:
            conexao.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))
            if com_dados:
                conexao.executescript(SEED_PATH.read_text(encoding="utf-8"))
            conexao.commit()
        finally:
            conexao.close()
