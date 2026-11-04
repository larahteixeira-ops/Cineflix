-- CineFlix - Etapa 1: estrutura do banco de dados (SQLite)
PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS avaliacao;
DROP TABLE IF EXISTS filme;
DROP TABLE IF EXISTS usuario;
DROP TABLE IF EXISTS genero;

CREATE TABLE genero (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    nome      TEXT NOT NULL UNIQUE,
    descricao TEXT
);

CREATE TABLE filme (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo    TEXT    NOT NULL,
    ano       INTEGER NOT NULL CHECK (ano BETWEEN 1888 AND 2100),
    nota      REAL    NOT NULL DEFAULT 0 CHECK (nota BETWEEN 0 AND 10),
    sinopse   TEXT,
    genero_id INTEGER NOT NULL,
    FOREIGN KEY (genero_id) REFERENCES genero (id)
        ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE usuario (
    id    INTEGER PRIMARY KEY AUTOINCREMENT,
    nome  TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);

CREATE TABLE avaliacao (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    filme_id   INTEGER NOT NULL,
    nota       INTEGER NOT NULL CHECK (nota BETWEEN 0 AND 10),
    comentario TEXT,
    data       TEXT    NOT NULL DEFAULT (date('now')),
    FOREIGN KEY (usuario_id) REFERENCES usuario (id) ON DELETE CASCADE,
    FOREIGN KEY (filme_id)   REFERENCES filme (id)   ON DELETE CASCADE,
    UNIQUE (usuario_id, filme_id)  -- um usuário avalia cada filme uma vez
);

CREATE INDEX idx_filme_genero ON filme (genero_id);
CREATE INDEX idx_avaliacao_filme ON avaliacao (filme_id);
