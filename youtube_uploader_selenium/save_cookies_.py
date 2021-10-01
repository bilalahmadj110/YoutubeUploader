""" This module implements save cookies from youtube URL. """

import json
import logging
from selenium_firefox.firefox import Firefox


from .Constant import *

logging.basicConfig()


class YouTubeCookiesSaver:
    """ This module implements save cookies from youtube URL. """

    def __init__(self, cookies_name='default_youtube') -> None:
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        self.logger.debug('INIT SAVE COOKIES...')

        self.cookies_name = cookies_name

        self.browser = Firefox('', '')

    def save_cookies(self, c):
        # saving cookies
        self.logger.debug('Saving cookies...')
        a_file = open(f"{self.cookies_name}.json", "w")
        json.dump(c, a_file)
        a_file.close()
        self.logger.debug('DONE saving cookies!')

    def setup(self):
        try:
            self.__login()
            self.browser.driver.quit()
            return True
        except Exception as e:
            print("ERROR:  ", e)
            self.browser.driver.quit()
            return False

    def __login(self):
        self.logger.debug(f'Loading {Constant.YOUTUBE_URL} ...')
        self.browser.get(Constant.YOUTUBE_URL)
        input('Press any key after you done LogIn to save cookies: ')
        self.save_cookies(self.browser.driver.get_cookies())
