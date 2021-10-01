"""This module implements uploading videos on YouTube via Selenium using metadata JSON file
    to extract its title, description etc."""

import json
import logging
import os
import time
from collections import defaultdict
from pathlib import Path
from selenium.webdriver import Firefox, Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from typing import DefaultDict, Optional
from selenium.webdriver.common.action_chains import ActionChains


from .Constant import *

# from selenium.webdriver.remote.file_detector import UselessFileDetector

logging.basicConfig()


def load_metadata(metadata_json_path: Optional[str] = None) -> DefaultDict[str, str]:
    if metadata_json_path is None:
        return defaultdict(str)
    with open(metadata_json_path, encoding='utf-8') as metadata_json_file:
        return defaultdict(str, json.load(metadata_json_file))


class YouTubeUploader:
    """A class for uploading videos on YouTube via Selenium using metadata JSON file
    to extract its title, description etc"""

    def __init__(self, video_path, video_title, video_desc, video_tags, video_privacy, channel, thumbnail_path=None,
                 add_extra_click=False, add_second_click=False, cookies_name='default') -> None:
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        self.video_path = video_path
        self.video_title = video_title
        self.video_desc = video_desc
        self.video_tags = video_tags
        self.video_privacy = video_privacy.title().strip()
        self.add_extra_click = add_extra_click
        self.add_second_click = add_second_click

        self.cookies_name = cookies_name

        self.thumbnail_path = thumbnail_path
        self.channel = channel

        self.logger.debug('Opening browser...')
        self.current_working_dir = str(Path.cwd())

        self.browser = Firefox()
  

        #print(dir(self.browser))

    def load_cookies(self):
        # load cookies from given filename
        self.logger.debug('Loading cookies')
        cookies = json.loads(open(f"{self.cookies_name}.json").read())
        for cookie in cookies:
            #print (cookie)
            self.browser.add_cookie(cookie)
        self.browser.refresh()

    def upload(self):
        # try:
        self.__login()
        return self.__upload()
        # except Exception as e:
        #     print(e)
        #     self.__quit()

    def __login(self):
        self.logger.debug(f'Loading {Constant.YOUTUBE_URL} ...')
        self.browser.get(Constant.YOUTUBE_URL)
        time.sleep(Constant.USER_WAITING_TIME)
        try:
            if not os.path.exists(f"{self.cookies_name}.json"):
                self.logger.debug("Cookies doesn't exists")
                raise Exception
            self.load_cookies()
        except Exception as e:
            print(e)
            print(
                "Fail to load cookies. Please set `SAVE_COOKIES` to `True` under config variables in "
                "`upload.py`.\nExiting browser now.")
            self.browser.quit()
            self.__quit()

    def __write_in_field(self, field, string, select_all=False):
        if field is not None:
            field.click()
        time.sleep(Constant.USER_WAITING_TIME)
        if select_all:
            field.send_keys(Keys.COMMAND + 'a')
            time.sleep(Constant.USER_WAITING_TIME)
        try:
            field.clear()
        except:
            pass
        time.sleep(0.2)
        field.send_keys(string)

    def __upload(self) -> (bool, Optional[str]):
        self.logger.debug('Loading Youtube...')
        self.browser.get(Constant.YOUTUBE_URL)

        time.sleep(Constant.USER_WAITING_TIME)

        self.logger.debug('Loading youtube upload studio')
        self.browser.get(Constant.YOUTUBE_UPLOAD_URL)
        time.sleep(Constant.USER_WAITING_TIME)

        absolute_video_path = str(Path.cwd() / self.video_path)
        self.browser.find_element(By.XPATH, Constant.INPUT_FILE_VIDEO).send_keys(absolute_video_path)

        self.logger.debug('Attached video {}'.format(self.video_path))

        time.sleep(10)

        title_field = self.browser.find_elements(By.XPATH, Constant.TEXTBOX)
        
        if len(title_field) == 1:
            self.__write_in_field(title_field, self.video_title, True)
            

        self.__write_in_field(title_field[0], self.video_title, True)
        self.logger.debug('The video title was set to \"{}\"'.format(self.video_title))

        if self.video_desc:
            self.__write_in_field(title_field[1], self.video_desc)
            self.logger.debug('The video desc was set to \"{}\"'.format(self.video_desc))

        if self.thumbnail_path:
            absolute_thumbnail_path = str(Path.cwd() / self.thumbnail_path)
            self.browser.find_element(By.XPATH, Constant.INPUT_FILE_VIDEO).send_keys(absolute_thumbnail_path)
            self.logger.debug('Setting thumbnail was set to "{}"'.format(absolute_thumbnail_path))

        self.browser.find_element(By.XPATH, Constant.KIDS_NOT_PATH).click() # Constant.NOT_MADE_FOR_KIDS_LABEL).click()
        self.logger.debug('Selected \"{}\"'.format(Constant.NOT_MADE_FOR_KIDS_LABEL))

        # Advanced options
        self.browser.find_element(By.XPATH, Constant.MORE_BUTTON).click()
        self.logger.debug('Clicked MORE OPTIONS')

        tags_field = self.browser.find_element(By.XPATH, Constant.TAGS_PATH)
        
        self.__write_in_field(tags_field.find_element(By.ID, Constant.TEXT_INPUT), ','.join(self.video_tags))
        self.logger.debug('The tags were set to \"{}\"'.format(self.video_tags))

        if self.add_extra_click:
            self.browser.find_element(By.ID, Constant.NEXT_BUTTON).click()
            self.logger.debug('Clicked {}'.format(Constant.NEXT_BUTTON))
            # Turn monetization ON
            self.browser.find_element(By.XPATH, Constant.MONITIZATION_TAG_ICON).click()
            self.browser.find_element(By.XPATH, Constant.MONITIZATION_TAG).click()
            self.browser.find_element(By.XPATH, Constant.MONITIZATION_TAG_BUT).click()

        if self.add_second_click:            
            self.browser.find_element(By.ID, Constant.NEXT_BUTTON).click()
            self.logger.debug('Clicked {}'.format(Constant.NEXT_BUTTON))
            
            element = self.browser.find_element(By.ID, Constant.SECOND_EXTRA_CLICK)
            actions = ActionChains(self.browser)
            actions.move_to_element(element).perform()
            self.browser.find_element(By.XPATH, Constant.SECOND_EXTRA_CLICK).click()
            self.logger.debug('Clicked another {}'.format(Constant.NEXT_BUTTON))
        self.browser.execute_script("window.scrollTo(0, 200)")
        self.browser.find_element(By.ID, Constant.NEXT_BUTTON).click()
        self.logger.debug('Clicked another {}'.format(Constant.NEXT_BUTTON))

        self.browser.find_element(By.ID, Constant.NEXT_BUTTON).click()
        self.logger.debug('Clicked another {}!'.format(Constant.NEXT_BUTTON))

        # UNCOMMENT BELOW TWO LINES TO ADD ONE MORE STEP CLICK
        self.browser.find_element(By.ID, Constant.NEXT_BUTTON).click()
        self.logger.debug('Clicked another {}!'.format(Constant.NEXT_BUTTON))

        if self.video_privacy.lower() == 'public':
            self.browser.find_element(By.XPATH, Constant.PUBLIC_TAG).click()
        elif self.video_privacy.lower() == 'unlisted':
            self.browser.find_element(By.XPATH, Constant.UNLISTED_TAG).click()
        else:
            self.browser.find_element(By.XPATH, Constant.PRIVATE_TAG).click()
        # public_main_button = self.browser.driver.find(By.NAME, self.video_privacy)
        # self.browser.find_element(By.ID, Constant.RADIO_LABEL, public_main_button).click()
        self.logger.debug('Made the video {}'.format(self.video_privacy))

        video_id = self.__get_video_id()

        status_container = self.browser.find_element(By.XPATH, Constant.STATUS_CONTAINER)
        print ("Waiting to upload.")
        self.browser.execute_script("window.scrollTo(0, 200)")
        while True:
            in_process = status_container.text.find(Constant.UPLOADED) != -1
            if in_process:
                time.sleep(Constant.USER_WAITING_TIME)
            else:
                break
            print('.', end='')

        done_button = self.browser.find_element(By.ID, Constant.DONE_BUTTON)

        # Catch such error as
        # "File is a duplicate of a video you have already uploaded"
        if done_button.get_attribute('aria-disabled') == 'true':
            error_message = self.browser.find_element(By.XPATH, Constant.ERROR_CONTAINER).text
            self.logger.error(error_message)
            return False, None

        done_button.click()

        time.sleep(Constant.USER_WAITING_TIME)

        self.logger.debug("Published the video with video_id = {}".format(video_id))

        try:
            self.browser.find_element(By.XPATH, Constant.PUBLIC_BUTTON).click()
        except Exception as e:
            print(e)

        time.sleep(Constant.USER_WAITING_TIME)
        self.browser.get(Constant.YOUTUBE_URL)

        return True, video_id

    def __get_video_id(self) -> Optional[str]:
        video_id = None
        try:
            video_id = self.browser.find_element(By.XPATH, Constant.VIDEO_URL_CONTAINER).text   
        except Exception as e:
            try:
                video_id = self.browser.find_element(By.XPATH, Constant.VIDEO_URL_ELEMENT).text
            except:
                print (e)
                self.logger.warning(Constant.VIDEO_NOT_FOUND_ERROR)             
        return video_id

    def __quit(self):
        return
        # self.browser.driver.quit()
