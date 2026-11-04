class Genero:
    def __init__(self, nome, descricao="", id=None):
        self.id = id
        self.nome = nome
        self.descricao = descricao

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        valor = (valor or "").strip()
        if not valor:
            raise ValueError("O nome do gênero é obrigatório.")
        self._nome = valor

    def to_dict(self):
        return {"id": self.id, "nome": self.nome, "descricao": self.descricao}
