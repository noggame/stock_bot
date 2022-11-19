import configparser as cfg
import logging
import os

def getConfigValue(section:str, name:str):
    config = cfg.ConfigParser()
    value = None

    try:
        config.read(f'{os.getcwd()}/config/config.ini')
        value = config.get(section, name)
    except Exception as ex:
        logging.warning("[System] ConfigParser :: get() :: {}".format(ex))

    return value



