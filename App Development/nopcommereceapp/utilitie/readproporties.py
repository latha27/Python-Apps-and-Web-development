import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")


class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def userEmail():
        email = config.get('common info', 'username')
        return email

    @staticmethod
    def userPass():
        password = config.get('common info', 'password')
        return password