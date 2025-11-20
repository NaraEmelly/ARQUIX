from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, User

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    CORS(app)

    db.init_app(app)

    # Criar BD
    with app.app_context():
        db.create_all()

    # ROTA DE CADASTRO
    @app.post("/register")
    def register():
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"error": "Dados incompletos"}), 400
        
        # Verificar se já existe
        if User.query.filter_by(username=username).first():
            return jsonify({"error": "Usuário já existe"}), 409
        
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()

        return jsonify({"message": "Usuário cadastrado com sucesso!"}), 201

    # ROTA DE LOGIN
    @app.post("/login")
    def login():
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        user = User.query.filter_by(username=username, password=password).first()

        if not user:
            return jsonify({"error": "Credenciais inválidas"}), 401
        
        return jsonify({
            "message": "Login realizado!",
            "user": user.username
        }), 200

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
