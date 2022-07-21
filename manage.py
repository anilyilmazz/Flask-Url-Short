from url_short_app.source import create_app, db
from url_short_app import blueprint

from flask_migrate import Migrate

from url_short_app.source.models import url

app = create_app("app")
app.register_blueprint(blueprint)

app.app_context().push()

migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(app.run(host='0.0.0.0', port=5000))
