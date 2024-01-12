import time

import pytest

from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomer import SearchCustomerBy
from pageObjects.AddcustomerPage import AddCustomer
from Utilities.readProperties import Readconfig
from Utilities.customLogger import LogGen


class Test_005_SearchCustomerbyName:
    baseurl = Readconfig.getApplicationurl()
    username = Readconfig.getUseremail()
    password = Readconfig.getUserpassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_SearchCustomerbyName(self, setup):
        self.logger.info("********************* Test_005_SearchCustomerbyName ******************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****************** Login Successful **************")

        self.logger.info("****************** Starting Searching Customer by name **************")
        self.addcust = AddCustomer(self.driver)  # creating object for Add customer class
        self.addcust.clickOnCustomermenu()
        self.addcust.clickOnCustomermenuitem()

        self.logger.info("****************** Search Customer by name **************")
        searchcust = SearchCustomerBy(self.driver)
        searchcust.setFirstname("Brenda")
        searchcust.setlastname("Lindgren")
        time.sleep(3)
        searchcust.clickSearchbutton()
        time.sleep(5)
        status = searchcust.SearchCustomerbyName("Brenda Lindgren")
        assert True == status
        self.logger.info("****************** Test_005_SearchCustomerbyName Finished **************")
        self.driver.close()