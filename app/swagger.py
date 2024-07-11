from flask import Blueprint
from flask_restx import Api

from .routes import movies_bp

swagger_bp = Blueprint("swagger", __name__, url_prefix="/swagger")

api = Api(
    swagger_bp,
    version="1.0",
    title="Movies API",
    description="API para gerenciar filmes",
    doc="/doc",  # Endpoint para a documentação Swagger UI
)

# Adicione o blueprint de rotas ao Swagger
api.add_namespace(movies_bp)


# Registre o blueprint do Swagger na aplicação Flask
def init_app(app):
    app.register_blueprint(swagger_bp)
