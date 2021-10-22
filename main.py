import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


from data import *

options = Options()
options.add_argument("--user-data-dir=D:\myGit\myTypingCheater\profile")

driver = webdriver.Chrome("chromedriver.exe", options=options)


driver.get(targetLink)


def setup():
    print("start typing")
    time.sleep(1)
    spans = driver.find_elements_by_tag_name("span")
    for span in spans:
        if "スタート" in span.text:
            span.click()
            return True
    return False


def dadada():
    print("start game")
    loop = True
    while loop:
        targets = driver.find_elements_by_class_name("mtjNowInput")
        if len(targets) <= 0:
            loop = False
            print("not found target.")
            return False
        targetKey = targets[1].text
        ActionChains(driver).send_keys(targetKey).perform()
        # time.sleep(1)


def typing():
    time.sleep(2)

    spans = driver.find_elements_by_tag_name("div")
    hit = False
    for span in spans:
        if "Press space bar to start!" in span.text:
            print("click start")
            ActionChains(driver).send_keys(Keys.SPACE).perform()
            hit = True
            break

    if not hit:
        return False

    dadada()


def finish():
    print("wait finish.")
    input()
    driver.close()


# loop = True
# while loop:
#     res = input()
#     if res == "run":
#         typing()
#     elif res == "end":
#         loop = False
#         finish()

setup()
typing()


finishWait()
