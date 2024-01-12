import string
import time

import pytest
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomer import SearchCustomerBy
from pageObjects.AddcustomerPage import AddCustomer
from Utilities.readProperties import Readconfig
from Utilities.customLogger import LogGen
import random


class Test_004_SearchCustomerbyEmail:
    baseurl = Readconfig.getApplicationurl()
    username = Readconfig.getUseremail()
    password = Readconfig.getUserpassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_SearchCustomerbyEmail(self, setup):
        self.logger.info("********************* Test_004_SearchCustomerbyEmail ******************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****************** Login Successful **************")

        self.logger.info("****************** Starting Searching Customer by Email **************")
        self.addcust = AddCustomer(self.driver)  # creating object for Add customer class
        self.addcust.clickOnCustomermenu()
        self.addcust.clickOnCustomermenuitem()

        self.logger.info("****************** Search Customer by Emailid **************")
        searchcust = SearchCustomerBy(self.driver)
        searchcust.setEmail("brenda_lindgren@nopCommerce.com")
        time.sleep(3)
        searchcust.clickSearchbutton()
        time.sleep(5)
        status = searchcust.SearchCustomerbyEmail("brenda_lindgren@nopCommerce.com")
        assert True == status
        self.logger.info("****************** Test_004_SearchCustomerbyEmail Finished **************")
        self.driver.close()