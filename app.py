import os
from flask import Flask
from models import *
from flask_migrate import Migrate
from routes import routes
from flask_login import LoginManager

# -----------------------
# DIRETÓRIO BASE E TEMPLATES
# -----------------------
base_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(base_dir, "templates")

# -----------------------
# CONFIGURAÇÃO DO APP
# -----------------------
app = Flask(__name__, template_folder=template_dir)

# 🔹 Configuração do banco (LOCAL x RENDER)
if os.environ.get("RENDER"):
    os.makedirs("/data", exist_ok=True)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////data/producao.db"
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///producao.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "123"  # Em produção, use variável de ambiente

# -----------------------
# EXTENSÕES
# -----------------------
db.init_app(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

# -----------------------
# CRIAÇÃO DO BANCO (somente se não existir)
# -----------------------
with app.app_context():
    db.create_all()
    print("✅ Banco criado/verificado com sucesso!")

# -----------------------
# ROTAS
# -----------------------
routes(app)

# -----------------------
# START
# -----------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
