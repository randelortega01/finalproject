"""
Routes for the Flask application
"""
from flask import jsonify
from service import app


@app.route("/")
def index():
    """Root endpoint - returns welcome message"""
    return jsonify(
        status=200,
        message="Welcome to the CI/CD Final Project"
    )


@app.route("/health")
def health():
    """Health check endpoint for Kubernetes/OpenShift"""
    return jsonify(
        status=200,
        message="Healthy"
    )


@app.route("/info")
def info():
    """Information endpoint"""
    return jsonify(
        status=200,
        name="CI/CD Final Project",
        version="1.0.0",
        description="A sample Flask application for CI/CD pipeline demonstration"
    )


@app.route("/count")
def count():
    """Counter endpoint for testing"""
    return jsonify(
        status=200,
        count=42
    )