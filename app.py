import os
from flask import Flask, render_template
from flask_migrate import Migrate
from models import db  # Import the db instance from models/__init__.py
from routes.book_bp import book_bp
from routes.category_bp import category_bp
from config import Config

# Initialize the Flask application
app = Flask(__name__)
app.config.from_object(Config)

# Initialize the database and migration tool
db.init_app(app)
migrate = Migrate(app, db)

# Register Blueprints for routes
app.register_blueprint(category_bp, url_prefix="/category")
app.register_blueprint(book_bp, url_prefix="/books")

# Define the main route
@app.route("/")
def index():
    return render_template("index.html")

# Entry point for running the application
if __name__ == "__main__":
    app.run(port=4000, debug=True)
