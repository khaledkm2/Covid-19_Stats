
class app_config (object):
    # the configuration can be loadd from yml file later
    COVID_TRACK_URL="https://api.covidtracking.com/v1/states/"
    JSON_FILE_NAME= "daily.json"
    SECRET_KEY= "sdljhfdkfgsdvbflfvsdfafgdf"


class development_app_config(app_config):
    DEBUG = False
    VERIFY = False


class production_app_config(app_config):
    pass


class test_app_config (app_config ):
    pass

configLooader = {
     'development': development_app_config,
    'testing': test_app_config,
    'production': production_app_config
}

