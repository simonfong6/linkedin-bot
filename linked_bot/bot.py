#!/usr/bin/env python3
"""LinkedIn Bot"""

import logging
import sys
import time

from selenium.webdriver import Chrome

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class Bot:
    """Web Bot"""

    def __init__(self, email, password, debug=False):
        self.driver = Chrome()
        self.debug = debug
        self.email = email
        self.password = password

    def get(self, url):
        """Visit the given url."""
        self.driver.get(url)
        logger.info(f"Current URL {self.driver.current_url}")

    def enter_field(self, id, value):
        """Enters the value into the element with the given id."""
        input_text = self.driver.find_element_by_id(id)
        input_text.send_keys(value)

    def sign_in_to_linkedin(self, email, password):
        """Sign in to LinkedIn"""
        sign_in_url = 'https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'
        self.get(sign_in_url)
        self.enter_field('username', email)
        logger.info(f"Entered 'username' field with '{email}'.")
        self.enter_field('password', password)
        self.click_submit_button()
        
        logger.info(f"Current URL {self.driver.current_url}")

    def click_submit_button(self):
        """Click the button with type set to submit."""
        logger.info("Clicking button the submit button.")
        button_xpath = "//button[@type='submit']"
        button = self.driver.find_element_by_xpath(button_xpath)
        button.click()

    def visit_godwins_linkedin(self):
        """Visits Godwin's Linkedin profile."""
        logger.info("Visiting Godwin's site.")
        godwin_linkedin_url = 'https://www.linkedin.com/in/godwinpang/'
        self.sign_in_to_linkedin(self.email, self.password)
        self.get(godwin_linkedin_url)

    def close(self):
        """Interface to close webdriver."""
        logger.info("Closing the Selenium webdriver.")
        self.driver.stop_client()
        self.driver.close()


def main(args):
    logger.info("Running bot to visit Godwin's LinkedIn page.")

    bot = Bot(debug=True, email=args.email, password=args.password)
    bot.visit_godwins_linkedin()
    bot.close()

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()

    parser.add_argument('--email',
                        help="Email to sign into LinkedIn with.",
                        type=str,
                        required=True)
    parser.add_argument('--password',
                        help="Password to sign in with LinkedIn with.",
                        type=str,
                        required=True)
    parser.add_argument('-d', '--debug',
                        help="Whether or not to run in debug mode.",
                        default=False,
                        action='store_true')

    args = parser.parse_args()
    main(args)