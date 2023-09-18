from flask import Flask
from flask_cors import CORS
from flaskr import create_app, db
from flaskr.models import Task

app = create_app()

# Enable CORS
CORS(app)

@app.shell_context_processor
def make_shell_context():
    return {"db": db, "Task": Task}