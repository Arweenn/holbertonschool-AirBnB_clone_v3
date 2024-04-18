#!/usr/bin/python3
"""
Entry point to start the application.
"""

from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)


@app.errorhandler(404)
def error_handler(exception):
    """Handles errors"""

    return jsonify({"error": "Not found"}), 404


@app.teardown_appcontext
def teardown(exception):
    """Teardown method to close the storage"""

    storage.close()


if __name__ == "__main__":

    app_host = getenv("HBNB_API_HOST", "0.0.0.0")
    app_port = int(getenv("HBNB_API_PORT", 5000))

    app.run(host=app_host, port=app_port, threaded=True)
