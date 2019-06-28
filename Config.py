import configparser


def get_modules():
    config = configparser.ConfigParser()
    config.read("modules.ini")
    section = config['modules']
    return config.items('modules')


def get_module_names():
    config = configparser.ConfigParser()
    config.read("modules.ini")
    section = config['modules']
    return dict(config.items('modules')).values()


def add_module(name: str):
    config = configparser.ConfigParser()
    config.read("modules.ini")
    section = config['modules']
    section[name] = name
    with open('modules.ini', 'w') as configfile:
        config.write(configfile)


def remove_module(name: str):
    pass


def get_token() -> str:
    config = configparser.ConfigParser()
    config.read("token.ini")
    section = config['token']
    return section['token']
