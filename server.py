from flask import render_template
import connexion
from flask_swagger_ui import get_swaggerui_blueprint

# Création de l'instance de l'application
app = connexion.App(__name__, specification_dir="./")

# Lecture du fichier Swagger
app.add_api("swagger.yml")

# Configuration de Swagger UI
SWAGGER_URL = '/api/ui'  # URL pour Swagger UI
API_URL = '/swagger.yml'  # Chemin vers le fichier Swagger YAML
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "API ReST avec Swagger"}
)
app.app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Définir la page d'accueil
@app.route("/")
def home():
    return render_template("home.html")

# Lancer l'application
if __name__ == "__main__":
    app.run()
