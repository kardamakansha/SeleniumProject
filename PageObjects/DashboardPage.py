class Dashboard:
    def __init__(self, driver):
        self.driver = driver
        self.displayed_xpath = "//img[@alt='profile picture']"
        self.Admin_xpath = "//span[normalize-space()='Admin']"
        self.user_management_xpath = "//span[normalize-space()='User Management']//i[@class='oxd-icon bi-chevron-down']"
        self.job_xpath = "//span[normalize-space()='Job']"
        self.employement_status_xpath = "//ul[@class='oxd-dropdown-menu']/li[3]"



    def profile_picture(self):
        return self.driver.find_element("xpath", self.displayed_xpath).is_displayed()

    def button_Admin(self):
        self.driver.find_element("xpath", self.Admin_xpath).click()

    def button_user_management(self):
        self.driver.find_element("xpath", self.user_management_xpath).click()

    def button_job(self):
        self.driver.find_element("xpath", self.job_xpath).click()

    def button_employement_status(self):
        self.driver.find_element("xpath", self.employement_status_xpath).click()

