class Usuario:
    def __init__(self, nome, email, id=None):
        self.id = id
        self.nome = nome
        self.email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        valor = (valor or "").strip().lower()
        if "@" not in valor:
            raise ValueError("E-mail inválido.")
        self._email = valor

    def to_dict(self):
        return {"id": self.id, "nome": self.nome, "email": self.email}
