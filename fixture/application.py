from selenium import webdriver

from fixture.james import JamesHelper
from fixture.session import SessionHelper
from fixture.project import ProjectHelper



class Application:
    def __init__(self, browser, config):
        if browser == 'firefox':
            self.wd = webdriver.Firefox()
        elif browser == 'chrome':
            self.wd = webdriver.Chrome()
        elif browser == 'opera':
            self.wd = webdriver.Opera()
        else:
            raise ValueError('unrecognized browser %s' % browser)
        self.project = ProjectHelper(self)
        self.session = SessionHelper(self)
        self.wd.implicitly_wait(2)
        self.config = config
        self.base_url = config['web']['baseUrl']
        self.james = JamesHelper(self)

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url == "http://localhost/addressbook/"):
            wd.get(self.base_url)

    def is_valid(self):
        try:
            self.wd.current_url()
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()
