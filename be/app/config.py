
import os

class Config:
    
    DEBUG = True

    # SERVIDOR PRUEBAS
    #SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_DATABASE')}"

    # DEV
    SQLALCHEMY_DATABASE_URI = "sqlite:///datos.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    LANGUAGES = {
    'en': 'English',
    'es': 'Spanish'
    }


config = {
    "config": Config,
}
