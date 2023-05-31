from flask import Flask, render_template
from .task import task



def create_app():
    # create instance flask
    app = Flask(__name__)
    
    #register blueprint here
    app.register_blueprint(task.taskBp, url_prefix="/tasks")
    
    #route default
    @app.route('/')
    def index():
        return render_template('index.html')
    return app

