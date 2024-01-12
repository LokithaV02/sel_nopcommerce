import string
import time

import pytest
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from Utilities.readProperties import Readconfig
from Utilities.customLogger import LogGen
import random

class Test_003_AddCustomer:
    baseurl = Readconfig.getApplicationurl()
    username = Readconfig.getUseremail()
    password = Readconfig.getUserpassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addcustomer(self, setup):
        self.logger.info("********************* Test_003_Add Customer ******************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****************** Login Successful **************")

        self.logger.info("****************** Starting Add Customer Test **************")
        self.addcust = AddCustomer(self.driver)  # creating object for Add customer class
        self.addcust.clickOnCustomermenu()
        time.sleep(3)
        self.addcust.clickOnCustomermenuitem()
        # click on Add new button
        self.addcust.clickOnAddNewbtn()
        self.logger.info("****************** Providing Customer Info **************")
        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFirstname("Pavan")
        self.addcust.setLastname("testing")
        self.addcust.setGender("Male")
        self.addcust.setDateofbirth("7/05/1987")
        self.addcust.setCompanyname("Testyentra")
        self.addcust.clickOncheckboxTaxexempt()
        self.addcust.setNewsletters("Test store 2")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.selectVendormanager("Vendor 2")
        self.addcust.clickOncheckboxActive()
        self.addcust.setAdminComment("This is for testing")
        self.addcust.clickOnsavebtn()
        self.logger.info("****************** Saving Customer Info **************")
        self.logger.info("****************** Validating of Customer started **************")
        # self.msg = self.driver.find_element(By.TAG_NAME,"body").text
        self.msg = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissable']").text
        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("************* Add Customer Test Passed **************")
        else:
            self.driver.save_screenshot(".//Screenshots//" + "test_addCustomer_scr.png")
            self.logger.error("************* Add Customer Test Failed **************")
            assert True == False
        self.driver.close()
        self.logger.info("************** Ending Add Customer Test **********")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
