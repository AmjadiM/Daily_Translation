import json

# ToDO: Create users function
# ToDo: Update user information function
#

class User(object):
    # User class created dynamically from JSON configuration
    def __init__(self, d):
        self.__dict__ = d

class Config(object):
    def __init__(self):
        self._config = config  # set it to conf

    def get_property(self, property_name):
        if property_name not in self._config.keys():  # we don't want KeyError
            return None  # just return None if not found
        return self._config[property_name]


class UserConfig(Config):

    @property
    def Languages(self):
        return self.get_property('Languages')

    @property
    def PhoneNumbers(self):
        return self.get_property('PhoneNumbers')

    @property
    def Provider(self):
        return self.get_property('Provider')


def get_contact():
    # Prompt user for information to initialize app
    name = input('What is your name?')
    phone_number = input('I hate to ask like this, but what\'s your phone number?')
    provider = input('Who is your phone provider?')
    print(('So you are {}, your phone number is {}, and provider is {}').format(name, phone_number, provider))
    print('Your daily translations are being set up')
    return name, phone_number, provider

def get_config(path="C:\Python\PycharmProjects\quoteDetect\config.json"):
    # Return configuration file with user details
    with open(path, 'r') as myjson:
        config = (json.load(myjson)).get("Users")
        return config

def get_users(self, config):
    # Return list of users
    users = list(self, config.keys)
    for elem in users:
        return elem
#
#def get_user_details(user, config=get_config()):
#    # Return details for specific user -- Use to instantiate class
#    return (config[user][0])

def get_user_details(user, path="C:\Python\PycharmProjects\quoteDetect\config.json"):
    # Return details for specific user -- Use to instantiate class
    with open(path, 'r') as myjson:
        config = (json.load(myjson)).get("Users")
        return (config[user][0])

def add_user(config=get_config()):
    print("hello")


