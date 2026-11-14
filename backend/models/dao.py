
import sqlite3

from models import Genero, Filme, Usuario, Avaliacao


class BaseDAO:
    def __init__(self, caminho_banco="cineflix.db"):
        self.caminho_banco = caminho_banco

    def _conectar(self):
        conexao = sqlite3.connect(self.caminho_banco)
        conexao.execute("PRAGMA foreign_keys = ON;")
        return conexao


# DAO DE GÊNEROS

class GeneroDAO(BaseDAO):

    def buscar_todos(self):
        with self._conectar() as conexao:
            cursor = conexao.cursor()

            cursor.execute(
                "SELECT id, nome, descricao FROM genero ORDER BY nome"
            )

            return [Genero(*linha) for linha in cursor.fetchall()]

    def inserir(self, genero):
        with self._conectar() as conexao:
            cursor = conexao.cursor()

            cursor.execute(
                "INSERT INTO genero (nome, descricao) VALUES (?, ?)",
                (genero.nome, genero.descricao)
            )

            conexao.commit()
            return cursor.lastrowid


# DAO DE FILMES

class FilmeDAO(BaseDAO):

    def buscar_todos(self):
        with self._conectar() as conexao:
            cursor = conexao.cursor()

            cursor.execute("""
                SELECT
                    f.id,
                    f.titulo,
                    f.ano,
                    f.nota,
                    f.sinopse,
                    f.genero_id,
                    g.nome
                FROM filme f
                JOIN genero g ON f.genero_id = g.id
                ORDER BY f.id DESC
            """)

            resultados = []

            for linha in cursor.fetchall():
                filme = Filme(
                    linha[0],
                    linha[1],
                    linha[2],
                    linha[3],
                    linha[4],
                    linha[5]
                )

                dado = filme.to_dict()
                dado["genero_nome"] = linha[6]

                resultados.append(dado)

            return resultados

    def inserir(self, filme):
        with self._conectar() as conexao:
            cursor = conexao.cursor()

            cursor.execute(
                """
                INSERT INTO filme
                (titulo, ano, nota, sinopse, genero_id)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    filme.titulo,
                    filme.ano,
                    filme.nota,
                    filme.sinopse,
                    filme.genero_id
                )
            )

            conexao.commit()
            return cursor.lastrowid

    def atualizar(self, id_filme, filme):
        with self._conectar() as conexao:
            cursor = conexao.cursor()

            cursor.execute(
                """
                UPDATE filme
                SET titulo=?, ano=?, nota=?, sinopse=?, genero_id=?
                WHERE id=?
                """,
                (
                    filme.titulo,
                    filme.ano,
                    filme.nota,
                    filme.sinopse,
                    filme.genero_id,
                    id_filme
                )
            )

            conexao.commit()

    def remover(self, id_filme):
        with self._conectar() as conexao:
            cursor = conexao.cursor()

            cursor.execute(
                "DELETE FROM filme WHERE id=?",
                (id_filme,)
            )

            conexao.commit()


# DAO DE USUÁRIOS

class UsuarioDAO(BaseDAO):

    def buscar_todos(self):
        with self._conectar() as conexao:
            cursor = conexao.cursor()

            cursor.execute(
                "SELECT id, nome, email FROM usuario ORDER BY nome"
            )

            return [Usuario(*linha) for linha in cursor.fetchall()]

    def inserir(self, usuario):
        with self._conectar() as conexao:
            cursor = conexao.cursor()

            cursor.execute(
                "INSERT INTO usuario (nome, email) VALUES (?, ?)",
                (usuario.nome, usuario.email)
            )

            conexao.commit()
            return cursor.lastrowid


# DAO DE AVALIAÇÕES

class AvaliacaoDAO(BaseDAO):

    def buscar_por_filme(self, filme_id):
        with self._conectar() as conexao:
            cursor = conexao.cursor()

            cursor.execute("""
                SELECT
                    a.id,
                    a.usuario_id,
                    a.filme_id,
                    a.nota,
                    a.comentario,
                    a.data,
                    u.nome
                FROM avaliacao a
                JOIN usuario u ON a.usuario_id = u.id
                WHERE a.filme_id = ?
                ORDER BY a.id DESC
            """, (filme_id,))

            lista = []

            for linha in cursor.fetchall():
                av = Avaliacao(
                    linha[0],
                    linha[1],
                    linha[2],
                    linha[3],
                    linha[4],
                    linha[5]
                )

                dado = av.to_dict()
                dado["usuario_nome"] = linha[6]

                lista.append(dado)

            return lista

    def inserir(self, avaliacao):
        with self._conectar() as conexao:
            cursor = conexao.cursor()

            cursor.execute(
                """
                INSERT INTO avaliacao
                (usuario_id, filme_id, nota, comentario)
                VALUES (?, ?, ?, ?)
                """,
                (
                    avaliacao.usuario_id,
                    avaliacao.filme_id,
                    avaliacao.nota,
                    avaliacao.comentario
                )
            )

            conexao.commit()
            return cursor.lastrowid
