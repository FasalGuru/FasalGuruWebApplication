from flask import Flask


def create_app():
    app = Flask(__name__)

    from fasalguru.dashboard.routes import dashboard
    app.register_blueprint(dashboard, url_prefix='/')

    from fasalguru.models.routes import models
    app.register_blueprint(models, url_prefix='/models')

    return app
