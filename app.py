from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class ColetaModels:
    from src.domain.models.jogos import Jogo
    
    
@app.route("/")
def index():
    return "<h1>Hello, World!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
    