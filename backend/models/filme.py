class Filme:
    def __init__(self, titulo, ano, nota, genero_id, sinopse="", id=None):
        self.id = id
        self.titulo = titulo
        self.ano = ano
        self.nota = nota
        self.sinopse = sinopse
        self.genero_id = genero_id

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, valor):
        valor = (valor or "").strip()
        if not valor:
            raise ValueError("O título é obrigatório.")
        self._titulo = valor

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, valor):
        valor = int(valor)
        if not 1888 <= valor <= 2100:
            raise ValueError("Ano inválido.")
        self._ano = valor

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, valor):
        valor = float(valor)
        if not 0 <= valor <= 10:
            raise ValueError("A nota deve estar entre 0 e 10.")
        self._nota = valor

    def to_dict(self):
        return {"id": self.id, "titulo": self.titulo, "ano": self.ano,
                "nota": self.nota, "sinopse": self.sinopse, "genero_id": self.genero_id}
