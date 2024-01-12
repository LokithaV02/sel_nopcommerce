from selenium.webdriver.common.by import By


class SearchCustomerBy:
    # Add customer Page
    txt_email_id = "SearchEmail"
    txt_FirstName_id = "SearchFirstName"
    txt_LastName_id = "SearchLastName"
    btn_search_xpath = "//button[@id='search-customers']"
    # tblsearchResults_xpath = "//table[@id='customers-grid_wrapper']"
    tble_xpath = "//table[@id='customers-grid']"
    tablerows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tablecolumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.txt_email_id).clear()
        self.driver.find_element(By.ID, self.txt_email_id).send_keys(email)

    def setFirstname(self, fname):
        self.driver.find_element(By.ID, self.txt_email_id).clear()
        self.driver.find_element(By.ID, self.txt_FirstName_id).send_keys(fname)

    def setlastname(self, lname):
        self.driver.find_element(By.ID, self.txt_email_id).clear()
        self.driver.find_element(By.ID, self.txt_LastName_id).send_keys(lname)

    def clickSearchbutton(self):
        self.driver.find_element(By.XPATH, self.btn_search_xpath).click()

    def getnoofRows(self):
        return len(self.driver.find_elements(By.XPATH, self.tablerows_xpath))

    def getnoofcolumns(self):
        return len(self.driver.find_elements(By.XPATH, self.tablecolumns_xpath))

    def SearchCustomerbyEmail(self, email):
        flag = False
        for r in range(1, self.getnoofRows()+1):
            table = self.driver.find_element(By.XPATH, self.tble_xpath)
            emailid = table.find_element(By.XPATH, "//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def SearchCustomerbyName(self, name):
        flag = False
        for r in range(1, self.getnoofRows()+1):
            table = self.driver.find_element(By.XPATH, self.tble_xpath)
            tname =table.find_element(By.XPATH, "//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[3]").text
            if tname == name:
                flag = True
                break
        return flag