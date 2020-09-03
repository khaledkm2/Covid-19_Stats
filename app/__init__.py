from flask import Flask
from config import configLooader
from flask_bootstrap import Bootstrap
from flask_babel import Babel

#https://api.covidtracking.com/v1/states/ca/daily.json
def create_app(config_name="development"):
    '''
    THis mthod is usd to cobfigur the application using th confiur name
    :param config_name: development is th default, it can used to config the app in case of testing and production
    :return:
    '''
    from app.routes import routes as routers_blueprint
    covid_app.register_blueprint(routers_blueprint, url_prefix='/')
    print (configLooader)
    app_config = configLooader.get(config_name)
    covid_app.config.from_object(app_config)
    return covid_app

#creat the application
covid_app = Flask(__name__)
#add flask bootsrap
bootstrap = Bootstrap(covid_app)
#add flask table
babel = Babel(covid_app)


