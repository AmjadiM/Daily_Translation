import configparser

class smtp_client():
    pass


class User(object):
    # User class created dynamically from JSON configuration
    def __init__(self, d):
        self.__dict__ = d
