import os
from pathlib import Path


class Config:
	SECRET_KEY = os.environ.get('FLASK_SECRET', 'dev-secret')
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///seloedu.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	# Upload / images config
	BASE_DIR = Path(__file__).resolve().parent
	UPLOAD_FOLDER = str(BASE_DIR / 'static' / 'uploads')
	MAX_CONTENT_LENGTH = 4 * 1024 * 1024
	ALLOWED_IMAGE_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
	THUMBNAIL_SIZE = (200, 200)


class DevelopmentConfig(Config):
	DEBUG = True
	# Mail settings
	MAIL_SERVER = os.environ.get('MAIL_SERVER', 'localhost')
	MAIL_PORT = int(os.environ.get('MAIL_PORT', 1025))
	MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'False').lower() == 'true'
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME', '')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', '')
	MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER', 'newpassword@seloedu.com')
