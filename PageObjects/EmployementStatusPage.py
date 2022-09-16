class EmpStatus:
    def __init__(self, driver):
        self.driver = driver
        self.Add_button_xpath = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']"
        self.Name_Xpath = "//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']"
        self.button_submit_xpath = "//button[@type='submit']"
        self.total_field_xpath = "(//div[@class='oxd-table-card'])"
        self.delete_button_xpath = "//div[@role='table']//div[1]//div[1]//div[3]//div[1]//button[1]//i[1]"
        self.delete_button2_xpath = "//button[normalize-space()='Yes, Delete']"

    def field_count(self):
        return self.driver.find_elements("xpath", self.total_field_xpath)

    def click_Add_button(self):
        self.driver.find_element("xpath", self.Add_button_xpath).click()

    def Enter_Name(self, Name):
        self.driver.find_element("xpath", self.Name_Xpath).send_keys(Name)

    def save_button(self):
        self.driver.find_element("xpath", self.button_submit_xpath).click()

    def Delete_Click(self):
        self.driver.find_element("xpath", self.delete_button_xpath).click()

    def delete_confirm(self):
        self.driver.find_element("xpath", self.delete_button2_xpath).click()
