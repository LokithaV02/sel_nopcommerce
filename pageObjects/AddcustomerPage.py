import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class AddCustomer:
    #Add Customer Page
    lnkCustomers_menu_xpath = "//a[@href ='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//a[@href ='/Admin/Customer/List']/*[contains(text(),'Customers')]"
    btnaddnew_xpath = "//a[@class='btn btn-primary']"
    text_email_xpath = "//input[@id='Email']"
    text_password_xpath = "//input[@id='Password']"
    text_firstname_xpath = "//input[@id='FirstName']"
    text_lastname_xpath = "//input[@id='LastName']"
    rb_gen_male_id = "Gender_Male"
    rb_gen_female_id = "Gender_Female"
    txt_dob_xpath = "//input[@id='DateOfBirth']"
    txt_companyname_xpath = "//input[@id='Company']"
    chkbox_istax_xpath = "//input[@id='IsTaxExempt']"
    lstbox_newsletter_xpath = "(//div[@class='k-multiselect-wrap k-floatwrap'])[1]"
    lstitem_Yourstore_xpath = "//li[contains(text(), 'Your store name')]"
    lstitem_Teststore_xpath = "//li[contains(text(), 'Test store 2')]"
    lstbox_Customerroles_xpath = "(//div[@class='k-multiselect-wrap k-floatwrap'])[2]"
    del_existingtags_custroles_xpath = "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]"
    lstitem_Administrators_xpath = "//li[contains(text(), 'Administrators')]"
    lstitem_ForumModerators_xpath = "//li[contains(text(), 'Forum Moderators')]"
    lstitem_Guests_xpath = "//li[contains(text(), 'Guests')]"
    lstitem_Registered_xpath = "//li[contains(text(), 'Registered')]"
    lstitem_vendors_xpath = "//li[contains(text(), 'Vendors')]"
    drpmanofVendor_xpath = "//*[@id='VendorId']"
    chkbox_active_xpath = "//input[@id='Active']"
    txt_admin_comment_xpath = "//textarea[@id='AdminComment']"
    btn_save_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomermenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menu_xpath).click()

    def clickOnCustomermenuitem(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddNewbtn(self):
        self.driver.find_element(By.XPATH, self.btnaddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.text_email_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.text_password_xpath).send_keys(password)

    def setFirstname(self, firstname):
        self.driver.find_element(By.XPATH, self.text_firstname_xpath).send_keys(firstname)

    def setLastname(self, lastname):
        self.driver.find_element(By.XPATH, self.text_lastname_xpath).send_keys(lastname)

    def setGender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.ID, self.rb_gen_male_id).click()
        elif gender == "Female":
            self.driver.find_element(By.ID, self.rb_gen_female_id).click()
        else:
            self.driver.find_element(By.ID, self.rb_gen_male_id).click()

    def setDateofbirth(self, dob):
        self.driver.find_element(By.XPATH, self.txt_dob_xpath).send_keys(dob)

    def setCompanyname(self, companyname):
        self.driver.find_element(By.XPATH, self.txt_companyname_xpath).send_keys(companyname)

    def clickOncheckboxTaxexempt(self):
        self.driver.find_element(By.XPATH, self.chkbox_istax_xpath).click()

    def setNewsletters(self, newsletter):
        self.driver.find_element(By.XPATH, self.lstbox_newsletter_xpath).click()
        time.sleep(3)
        if newsletter == "Your store name":
            self.newslst = self.driver.find_element(By.XPATH, self.lstitem_Yourstore_xpath)
        elif newsletter == "Test store 2":
            self.newslst = self.driver.find_element(By.XPATH, self.lstitem_Teststore_xpath)
        else:
            self.newslst = self.driver.find_element(By.XPATH, self.lstitem_Yourstore_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.newslst)

    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH, self.lstbox_Customerroles_xpath).click()
        time.sleep(5)
        if role == "Administrators":
            self.listitem = self.driver.find_element(By.XPATH, self.lstitem_Administrators_xpath)
        elif role == "Registered":
            self.listitem = self.driver.find_element(By.XPATH, self.lstitem_Registered_xpath)
        elif role == "Guests":
            # here user can be either registered or Guest only one i.e cannot be both
            time.sleep(3)
            self.driver.find_element(By.XPATH, self.del_existingtags_custroles_xpath).click()
            self.listitem = self.driver.find_element(By.XPATH, self.lstitem_Guests_xpath)
        elif role == "Registered":
            self.listitem = self.driver.find_element(By.XPATH, self.lstitem_Registered_xpath)
        elif role == "Vendors":
            self.listitem = self.driver.find_element(By.XPATH, self.lstitem_vendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstitem_Guests_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listitem) #execute script is used when list item is not clickable

    def selectVendormanager(self, value):
        sd = Select(self.driver.find_element(By.XPATH, self.drpmanofVendor_xpath))
        sd.select_by_visible_text(value)

    def clickOncheckboxActive(self):
        self.driver.find_element(By.XPATH, self.chkbox_active_xpath).click()

    def setAdminComment(self, comment):
        self.driver.find_element(By.XPATH, self.txt_admin_comment_xpath).send_keys(comment)

    def clickOnsavebtn(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()