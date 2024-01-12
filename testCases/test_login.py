import pytest

from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import Readconfig
from Utilities.customLogger import LogGen


class Test_001_Login:
    baseurl = Readconfig.getApplicationurl()
    username = Readconfig.getUseremail()
    password = Readconfig.getUserpassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_pagehometitle(self, setup):
        self.logger.info("*********************test_001_Login******************")
        self.logger.info("*******************Verifying Home Page Title****************")
        self.driver = setup
        self.driver.get(self.baseurl)
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("******************Home page title test is passed**************")
        else:
            self.driver.save_screenshot(".//Screenshots//" + "test_pagehometitle.png")
            self.driver.close()
            self.logger.error("******************Home page title test is failed**************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login(self, setup):
        self.logger.info("******************Verifying login test**************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == 'Dashboard / nopCommerce administration':
            assert True
            self.logger.info("******************Login test is passed**************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".//Screenshots//" + "test_login.png")
            self.driver.close()
            self.logger.error("******************Login test is failed**************")
            assert False
