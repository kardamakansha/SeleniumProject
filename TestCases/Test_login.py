import time
from PageObjects.LoginPage import Login
from PageObjects.DashboardPage import Dashboard
import pytest
from Utilities.logger import logclass


@pytest.mark.usefixtures("setup")
class Test_login(logclass):
    def test_001(self):
        time.sleep(3)
        log = self.getthelogs()
        lg = Login(self.driver)
        db = Dashboard(self.driver)
        log.info("TEST CASE 001")
        log.info("Test Case Stating")
        lg.input_username("admin")
        log.info("enter user name")
        lg.input_password("admin123")
        log.info("enter Password")
        lg.click_login()
        log.info("clicked Login")
        if db.profile_picture():
            print("Passed")
            assert True
            log.info("test case pass")
        else:
            print("Failed")
            log.info("test case failed")
            assert False


    def test_002(self):
        print(self.name)
        time.sleep(3)
        lg = Login(self.driver)
        lg.input_username("amin")
        lg.input_password("admin123")
        lg.click_login()
        if 'Invalid credentials' in lg.text_invalidmsg():
            print("Invalid credentials")
            assert True
        else:
            print("Failed")
            assert False

    def test_003(self):
        time.sleep(3)
        lg = Login(self.driver)
        lg.input_username("admin")
        lg.input_password("admin1234")
        lg.click_login()
        if "Invalid credentials" in lg.text_invalidmsg():
            print("Invalid credentials")
            assert True
        else:
            print("Failed")
            assert False
