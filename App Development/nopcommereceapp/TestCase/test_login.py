import pytest
from PageObjectModel.loginPage import LoginPage
from utilitie.readproporties import ReadConfig
from TestCase.confg import setup


@pytest.fixture()
class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.userEmail()
    password = ReadConfig.userPass()

    def test_homePageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenShots\\" + "test_homePageTitle.png")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenShots\\" + "test_login.png")
            self.driver.close()
            assert False




