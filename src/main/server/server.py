from flask import Flask
from src.main.routes.user_routes import user_routes_bp

app = Flask(__name__)

app.register_blueprint(user_routes_bp)