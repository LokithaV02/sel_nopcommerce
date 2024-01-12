import configparser
config= configparser.RawConfigParser()
config.read(".//Configurations/config.ini")

class Readconfig:
    @staticmethod
    def getApplicationurl():
        url = config.get('common info','baseurl')
        return url

    @staticmethod
    def getUseremail():
        username = config.get('common info', 'useremail')
        return username

    @staticmethod
    def getUserpassword():
        password = config.get('common info', 'password')
        return password




