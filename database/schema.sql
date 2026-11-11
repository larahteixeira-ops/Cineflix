-- CineFlix - Etapa 1: estrutura do banco de dados (SQLite)
PRAGMA foreign_keys = ON;
CREATE DATABASE IF NOT EXISTS cineflix
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE cineflix;

SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS avaliacao;
DROP TABLE IF EXISTS filme;
DROP TABLE IF EXISTS usuario;
DROP TABLE IF EXISTS genero;

SET FOREIGN_KEY_CHECKS = 1;

-- Tabela de gêneros
CREATE TABLE genero (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    nome      TEXT NOT NULL UNIQUE,
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL UNIQUE,
    descricao TEXT
);
) ENGINE=InnoDB;

-- Tabela de filmes
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
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    ano INT NOT NULL,
    nota DECIMAL(3,1) NOT NULL DEFAULT 0,
    sinopse TEXT,
    genero_id INT NOT NULL,

    CONSTRAINT chk_filme_ano
        CHECK (ano BETWEEN 1888 AND 2100),

    CONSTRAINT chk_filme_nota
        CHECK (nota BETWEEN 0 AND 10),

    CONSTRAINT fk_filme_genero
        FOREIGN KEY (genero_id)
        REFERENCES genero(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE=InnoDB;

-- Tabela de usuários
CREATE TABLE usuario (
    id    INTEGER PRIMARY KEY AUTOINCREMENT,
    nome  TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE
) ENGINE=InnoDB;

-- Tabela de avaliações
CREATE TABLE avaliacao (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    filme_id   INTEGER NOT NULL,
    nota       INTEGER NOT NULL CHECK (nota BETWEEN 0 AND 10),
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    filme_id INT NOT NULL,
    nota INT NOT NULL,
    comentario TEXT,
    data       TEXT    NOT NULL DEFAULT (date('now')),
    FOREIGN KEY (usuario_id) REFERENCES usuario (id) ON DELETE CASCADE,
    FOREIGN KEY (filme_id)   REFERENCES filme (id)   ON DELETE CASCADE,
    UNIQUE (usuario_id, filme_id)  -- um usuário avalia cada filme uma vez
);

CREATE INDEX idx_filme_genero ON filme (genero_id);
CREATE INDEX idx_avaliacao_filme ON avaliacao (filme_id);
    data DATE NOT NULL DEFAULT (CURRENT_DATE),

    CONSTRAINT chk_avaliacao_nota
        CHECK (nota BETWEEN 0 AND 10),

    CONSTRAINT fk_avaliacao_usuario
        FOREIGN KEY (usuario_id)
        REFERENCES usuario(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_avaliacao_filme
        FOREIGN KEY (filme_id)
        REFERENCES filme(id)
        ON DELETE CASCADE,

    CONSTRAINT uk_usuario_filme
        UNIQUE (usuario_id, filme_id)
) ENGINE=InnoDB;

-- Índices
CREATE INDEX idx_filme_genero
ON filme(genero_id);

CREATE INDEX idx_avaliacao_filme
ON avaliacao(filme_id);