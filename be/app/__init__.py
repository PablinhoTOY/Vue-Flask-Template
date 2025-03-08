from flask import Flask
import os
import time
import platform
import logging
from logging.config import dictConfig
from logging.handlers import TimedRotatingFileHandler
import pytz # type: ignore
from dotenv import load_dotenv
from app.config import config
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from flask_mail import Mail

os.environ["TZ"] = "America/Bogota"
try:
    time.tzset()
except:
    pass

IST = pytz.timezone('America/Bogota')

# refers to application_top
APP_ROOT = os.path.join(os.path.dirname(__file__), "..")
dotenv_path = os.path.join(APP_ROOT, ".env")
load_dotenv(dotenv_path)

app = Flask(__name__)
enviroment = config["config"]
app.config.from_object(enviroment)

db = SQLAlchemy(app)
Migrate(app, db)

CORS(app, supports_credentials=True)

#############################LOGGER###################################################
baseDir = os.path.abspath(os.path.dirname(__file__))
month = datetime.now(IST).strftime("%B")
year = datetime.now(IST).strftime("%Y")

if platform.system() == "Windows":
    path = os.path.join(baseDir, "logs\\{}\\{}".format(year, month))
else:
    path = os.path.join(baseDir, "logs/{}/{}".format(year, month))

isExist = os.path.exists(path)
if not isExist:
    # Create a new directory if it doesn't exist
    os.makedirs(path)

logname = os.path.join(path, "bitacora.json".format(year, month))

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "default": {
            "format": "[%(asctime)s] [%(levelname)s | %(module)s] %(message)s",
            "datefmt": "%B %d, %Y %H:%M:%S %Z",
        },
        "simple": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            "datefmt": "%B %d, %Y %H:%M:%S %Z",
        },
        "detailed": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(pathname)s:%(lineno)d",
            "datefmt": "%B %d, %Y %H:%M:%S %Z",
        },
        "json": {
            "class": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "format": "%(asctime)s %(levelname)s %(message)s - %(pathname)s:%(lineno)d",
            "datefmt": "%B %d, %Y %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "detailed",
            "stream": "ext://sys.stdout",
        },
        "file-handler": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": logname,
            "when": "midnight",
            "formatter": "simple",
        },
        "file-handler-json": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": logname,
            "when": "midnight",
            "formatter": "json",
        },
    },
    "root": {"level": "INFO", "handlers": ["console"]},
    "loggers": {
        "modulos": {
            "level": "INFO",
            "handlers": ["file-handler-json"],
            "propagate": False,
        }
    },
}

logging.config.dictConfig(LOGGING_CONFIG)

#################################################################################


# Listas UTP
# app.config["MAIL_SERVER"] = "listas.utp.ac.pa"
# app.config["MAIL_DEFAULT_SENDER"] = '"Kiosko UTP" <soporte@kiosco.utp.ac.pa>'
# app.config["MAIL_PORT"] = 25

#Mailtrap
app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = 'fea2744adb3e00'
app.config['MAIL_PASSWORD'] = 'cabfb7d360e07f'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config["MAIL_DEFAULT_SENDER"] = '"Kiosko UTP" <soporte@kiosco.utp.ac.pa>'
app.config["MAIL_DEBUG"] = False

mail = Mail(app)

@app.cli.command()
def seed():
    """Add seed data to the database."""
    from seed_inicial import seed_db

    seed_db()
    
from app.routes import *