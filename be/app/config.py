class Config:
    pass

class DevelopmentConfig(Config):
    
    DEBUG = True

    # SERVIDOR PRUEBAS
    #SQLALCHEMY_DATABASE_URI = "mysql+pymysql://admin:eurocorp@192.168.10.245:3306/kiosko"

    # DEV
    SQLALCHEMY_DATABASE_URI = "sqlite:///datos.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    LANGUAGES = {
    'en': 'English',
    'es': 'Spanish'
    }


config = {
    "development": DevelopmentConfig,
}
