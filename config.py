class Config(object):
    DEBUG = True
    TESTING = False


class DevelopmentConfig(Config):
    SECRET_KEY = "jhfduhfd8754827ywehujkfh977428T%^#@#TYHGF55t7yhlgjhhsddfda"  # Not sure if necessay
    OPENAI_KEY = "YOURKEYHERE"


config = {
    "development": DevelopmentConfig,
    "testing": DevelopmentConfig,
    "production": DevelopmentConfig,
}
