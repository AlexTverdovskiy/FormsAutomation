import configparser

def ReadConfigData(section, key):
    config = configparser.ConfigParser()
    config.read("C:/Users/tverdovskiyai/PycharmProjects/NGX/ConfigurationFiles/Config.cfg")
    return config.get(section, key)