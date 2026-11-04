"""Teste da Etapa 1: cria o banco, popula e confirma que a conexão funciona.

Uso:  python backend/testar_conexao.py
"""
from database import Database


def main():
    db = Database()
    db.inicializar(com_dados=True)
    print("Banco criado em:", db.caminho)

    conexao = db.conectar()
    tabelas = conexao.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name"
    ).fetchall()
    print("\nTabelas e quantidade de registros:")
    for t in tabelas:
        total = conexao.execute(f"SELECT COUNT(*) FROM {t['name']}").fetchone()[0]
        print(f"  - {t['name']}: {total}")

    print("\nFilmes com seu gênero (JOIN):")
    linhas = conexao.execute(
        "SELECT f.titulo, f.ano, g.nome AS genero, f.nota "
        "FROM filme f JOIN genero g ON g.id = f.genero_id ORDER BY f.nota DESC LIMIT 5"
    ).fetchall()
    for l in linhas:
        print(f"  {l['titulo']} ({l['ano']}) - {l['genero']} - nota {l['nota']}")

    conexao.close()
    print("\nConexão com o banco funcionando!")


if __name__ == "__main__":
    main()
