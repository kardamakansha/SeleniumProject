import time
from PageObjects.LoginPage import Login
from PageObjects.DashboardPage import Dashboard
import pytest
from PageObjects.EmployementStatusPage import EmpStatus
from Utilities.logger import logclass
from Utilities.random_status import status_genrator
import configparser
config = configparser.ConfigParser()
config.read("utilities/input.properties")


@pytest.mark.usefixtures("setup")
class Test_login(logclass):
    def test_001(self):
        time.sleep(3)
        log = self.getthelogs()
        lg = Login(self.driver)
        db = Dashboard(self.driver)
        log.info("TEST CASE 001")
        log.info("Test Case Stating")
        lg.input_username(config.get("credential", "correct_username"))
        log.info("enter user name")
        lg.input_password(config.get("credential", "correct_password"))
        log.info("enter Password")
        lg.click_login()
        log.info("clicked Login")
        self.driver.save_screenshot('Screenshot\\test_login.png')
        if db.profile_picture():
            print("Passed")
            assert True
            log.info("test case pass")
        else:
            print("Failed")
            log.info("test case failed")
            assert False
        time.sleep(1)
        db.button_Admin()
        log.info("Click admin button")
        db.button_user_management()
        log.info("Click user management button")
        time.sleep(1)
        db.button_job()
        log.info("Click job button")
        time.sleep(1)
        db.button_employement_status()
        log.info("Click employment button")
        time.sleep(1)
        es = EmpStatus(self.driver)
        old_count = 0
        for i in es.field_count():
            old_count = old_count + 1
        print(old_count)
        time.sleep(1)
        es.click_Add_button()
        log.info("Click add button")
        time.sleep(1)
        es.Enter_Name(status_genrator())
        log.info("Enter Name")
        time.sleep(1)
        es.save_button()
        log.info("Click save button")
        print("Add Successfully")
        time.sleep(6)
        new_count = 0
        for j in es.field_count():
            new_count = new_count + 1
        print(new_count)
        time.sleep(2)
        if old_count + 1 == new_count:
            assert True
        else:
            assert False
        time.sleep(6)
        es.Delete_Click()
        time.sleep(4)
        es.delete_confirm()
        print("Deleted Successfully")
        time.sleep(5)
        old_count = 0
        for k in es.field_count():
            old_count = old_count + 1
        print(old_count)
        time.sleep(2)















