"""
Service package for the Flask application
"""
from flask import Flask

app = Flask(__name__)

# Import routes after app is created to avoid circular imports
from service import routes  # noqa: F401, E402
