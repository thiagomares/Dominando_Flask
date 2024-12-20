# domain/models/jogo.py
from app import db  # Importando a instância db do app

class Jogo(db.Model):
    __tablename__ = "jogos"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))

    def __repr__(self):
        return f"<Jogo {self.nome}>"
