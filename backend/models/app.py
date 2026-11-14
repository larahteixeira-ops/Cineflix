
import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS

from models import Genero, Filme, Usuario, Avaliacao
from dao import GeneroDAO, FilmeDAO, UsuarioDAO, AvaliacaoDAO

app = Flask(__name__)
CORS(app)

# Conexão com os DAOs
genero_dao = GeneroDAO()
filme_dao = FilmeDAO()
usuario_dao = UsuarioDAO()
avaliacao_dao = AvaliacaoDAO()


@app.route("/", methods=["GET"])
def inicio():
    return jsonify({"status": "API CineFlix ativa!"})


# ROTAS DE GÊNEROS

@app.route("/generos", methods=["GET"])
def listar_generos():
    generos = genero_dao.buscar_todos()
    return jsonify([g.to_dict() for g in generos])


@app.route("/generos", methods=["POST"])
def criar_genero():
    dados = request.json

    try:
        novo = Genero(
            None,
            dados["nome"],
            dados.get("descricao", "")
        )

        id_gerado = genero_dao.inserir(novo)

        return jsonify({
            "id": id_gerado,
            "mensagem": "Gênero cadastrado com sucesso!"
        }), 201

    except Exception as erro:
        return jsonify({"erro": str(erro)}), 400


# ROTAS DE FILMES

@app.route("/filmes", methods=["GET"])
def listar_filmes():
    return jsonify(filme_dao.buscar_todos())


@app.route("/filmes", methods=["POST"])
def criar_filme():
    dados = request.json

    try:
        filme = Filme(
            None,
            dados["titulo"],
            dados["ano"],
            dados.get("nota", 0),
            dados.get("sinopse", ""),
            dados["genero_id"]
        )

        id_gerado = filme_dao.inserir(filme)

        return jsonify({
            "id": id_gerado,
            "mensagem": "Filme cadastrado com sucesso!"
        }), 201

    except Exception as erro:
        return jsonify({"erro": str(erro)}), 400


@app.route("/filmes/<int:id_filme>", methods=["PUT"])
def atualizar_filme(id_filme):
    dados = request.json

    try:
        filme = Filme(
            id_filme,
            dados["titulo"],
            dados["ano"],
            dados.get("nota", 0),
            dados.get("sinopse", ""),
            dados["genero_id"]
        )

        filme_dao.atualizar(id_filme, filme)

        return jsonify({
            "mensagem": "Filme atualizado com sucesso!"
        })

    except Exception as erro:
        return jsonify({"erro": str(erro)}), 400


@app.route("/filmes/<int:id_filme>", methods=["DELETE"])
def remover_filme(id_filme):
    try:
        filme_dao.remover(id_filme)

        return jsonify({
            "mensagem": "Filme removido com sucesso!"
        })

    except Exception as erro:
        return jsonify({"erro": str(erro)}), 400


# ROTAS DE USUÁRIOS

@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    usuarios = usuario_dao.buscar_todos()
    return jsonify([u.to_dict() for u in usuarios])


@app.route("/usuarios", methods=["POST"])
def criar_usuario():
    dados = request.json

    try:
        usuario = Usuario(
            None,
            dados["nome"],
            dados["email"]
        )

        id_gerado = usuario_dao.inserir(usuario)

        return jsonify({
            "id": id_gerado,
            "mensagem": "Usuário cadastrado com sucesso!"
        }), 201

    except sqlite3.IntegrityError:
        return jsonify({
            "erro": "Este e-mail já está cadastrado."
        }), 400

    except Exception as erro:
        return jsonify({"erro": str(erro)}), 400


# ROTAS DE AVALIAÇÕES

@app.route("/filmes/<int:id_filme>/avaliacoes", methods=["GET"])
def listar_avaliacoes(id_filme):
    return jsonify(avaliacao_dao.buscar_por_filme(id_filme))


@app.route("/avaliacoes", methods=["POST"])
def criar_avaliacao():
    dados = request.json

    try:
        av = Avaliacao(
            None,
            dados["usuario_id"],
            dados["filme_id"],
            dados["nota"],
            dados.get("comentario", "")
        )

        id_gerado = avaliacao_dao.inserir(av)

        return jsonify({
            "id": id_gerado,
            "mensagem": "Avaliação registrada!"
        }), 201

    except sqlite3.IntegrityError:
        return jsonify({
            "erro": "Este usuário já avaliou este filme."
        }), 400

    except Exception as erro:
        return jsonify({"erro": str(erro)}), 400


# INICIAR API

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
