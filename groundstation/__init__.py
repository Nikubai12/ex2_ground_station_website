import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(script_info=None):
	app = Flask(__name__,
 	static_folder = './public',
 	template_folder="./templates")

	app_settings = os.getenv('APP_SETTINGS')
	app.config.from_object(app_settings)

	db.init_app(app)
	migrate.init_app(app, db)

	from groundstation.views import home_blueprint
	from groundstation.backend_api.housekeeping import housekeeping_blueprint
	# register the blueprints
	app.register_blueprint(home_blueprint)
	app.register_blueprint(housekeeping_blueprint)

	@app.shell_context_processor
	def ctx():
		return {'app': app, 'db': db}

	return app
