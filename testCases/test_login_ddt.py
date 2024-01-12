import time

import pytest

from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import Readconfig
from Utilities.customLogger import LogGen
from Utilities import XLUtils


class Test_002_DDT_Login:
    baseurl = Readconfig.getApplicationurl()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("*********** Test_002_DDT_Login *******************")
        self.logger.info("****************** Verifying login ddt test **************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of Rows in a Excel", self.rows)
        lst_status = []

        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = 'Dashboard / nopCommerce administration'

            if act_title == exp_title:
                if self.exp == 'Pass':
                    self.logger.info("*********PASSED************")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("*********FAILED************")
                    self.lp.clickLogout()
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("*********FAILED************")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("*********PASSED************")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("*********Login DDT test is Passed************")
            self.driver.close()
            assert True
        else:
            self.logger.info("*********Login DDT test is Failed************")
            self.driver.close()
            assert False

        self.logger.info("********* End of Login DDT test ************")
        self.logger.info("********** COmpleted TC_LoginDDT_002*********")
