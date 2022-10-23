import datetime
import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def json_to_obj(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            obj = json.load(f)
        return obj
    except:
        print(f'There is not {file_name} (in proper format)')
        exit()


def get_driver(headless=False):
    options = Options()
    if headless: options.add_argument('--headless')
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(options=options, service=service)
    return driver


def get_n_minutes_later(n):
    now = datetime.datetime.now()
    # nml means "n minutes later"
    nml = now + datetime.timedelta(minutes=int(n))
    return nml.hour, nml.minute, nml.second


class OpenDns:
    def __init__(self, mail, password, network_id):
        self.mail       = mail
        self.password   = password
        self.network_id = network_id
        self.driver     = get_driver(headless=True)


    def login(self):
        self.driver.get("https://login.opendns.com/")

        username_form = self.driver.find_element(By.ID, "username")
        password_form = self.driver.find_element(By.ID, "password")
        sign_in_btn   = self.driver.find_element(By.ID, "sign-in")

        username_form.send_keys(self.mail)
        password_form.send_keys(self.password)
        sign_in_btn.click()

        time.sleep(5)
        return


    def move_to_setting(self):
        self.driver.get('https://dashboard.opendns.com/settings/')

        ip_setting_link = self.driver.find_element(By.ID, self.network_id)
        ip_setting_link.click()

        time.sleep(2)
        return


    def add_domain(self, domain):
        block_domain_form = self.driver.find_element(By.ID, "block-domain")
        add_domain_btn    = self.driver.find_element(By.ID, "add-domain")

        block_domain_form.send_keys(domain)
        time.sleep(1.5)

        add_domain_btn.click()
        time.sleep(1.5)

        # 追加するドメインの候補を聞かれても無視する
        try:
            self.driver.find_element(By.ID, "confirm-add-domain").click()
            time.sleep(1.5)
        except:
            # すでにブロックされているドメインでも追加する
            try:
                self.driver.find_element(By.ID, "confirm-add-already-blocked").click()
                time.sleep(1.5)
            except:
                return


    def restrict(self):
        black_list = json_to_obj('black_list.json')

        if black_list == []:
            print('Your blacklist is empty! Please add domain to blacklist')
            return

        for domain in black_list:
            self.add_domain(domain)
        return


    def permit(self):
        always_block_checkboxes = self.driver.find_elements(By.CSS_SELECTOR, ".domains-list")

        if always_block_checkboxes == []:
            print('There is no blocked domain')
            return

        for checkbox in always_block_checkboxes:
            checkbox.click()

        delete_btn = self.driver.find_element(By.ID, "delete-domains")
        delete_btn.click()
        return
