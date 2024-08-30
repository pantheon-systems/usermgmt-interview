from quart import Quart
from auth.routes.auth import auth_bp
from auth.config import config
from auth.setup_db import setup_database


def create_app():
    app = Quart(__name__)
    app.config.from_object(config)
    app.register_blueprint(auth_bp)

    setup_database()

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
