from datetime import date


class Avaliacao:
    def __init__(self, usuario_id, filme_id, nota, comentario="", data=None, id=None):
        self.id = id
        self.usuario_id = usuario_id
        self.filme_id = filme_id
        self.nota = nota
        self.comentario = comentario
        self.data = data or date.today().isoformat()

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, valor):
        valor = int(valor)
        if not 0 <= valor <= 10:
            raise ValueError("A nota deve estar entre 0 e 10.")
        self._nota = valor

    def to_dict(self):
        return {"id": self.id, "usuario_id": self.usuario_id, "filme_id": self.filme_id,
                "nota": self.nota, "comentario": self.comentario, "data": self.data}
