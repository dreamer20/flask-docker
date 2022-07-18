from flask import Flask


def create_app(test_config=None):

    app = Flask(__name__)

    if test_config is not None:
        app.config.from_mapping(test_config)

    @app.route('/')
    def index():
        return 'hello local'

    return app
