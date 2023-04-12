from random import randint
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

username = "填入统一登录帐号"
password = "填入统一登录密码"

driver = webdriver.Chrome('chromedriver')

text_msg = ("null", "null")

select_mode = "random"  # select OR random
select_value = 1  # range from 1 to 5
select_range = (3, 5)  # IF RANDOM, use range [ , ]


def perform_act():
    for index in range(16):
        div_id = "answerDiv" + str(index)
        selections = driver.find_element(By.ID, div_id).find_elements(By.CSS_SELECTOR, "input")

        if select_mode == "select":
            choice = 5 - select_value
        else:
            choice = 5 - randint(select_range[0], select_range[1])

        is_intractable = False
        times_out = -15
        while not is_intractable:
            is_intractable = True
            times_out += 1
            try:
                selections[choice].click()
            except:
                print("Waiting for next[" + str(index) + "]...")
                sleep(0.5)
                is_intractable = False
            if not times_out:
                is_intractable = True

        print("Q" + str(index) + "-> A:" + str(choice))

    for index in range(16, 18):
        div_id = "post-problem" + str(index)
        text_area = driver.find_element(By.ID, div_id).find_element(By.CSS_SELECTOR, "textarea")
        msg = text_msg[index - 17]

        is_intractable = False
        times_out = -15
        while not is_intractable:
            is_intractable = True
            try:
                text_area.send_keys(msg)
            except:
                print("Waiting for next[" + str(index) + "]...")
                sleep(0.5)
                is_intractable = False
            if not times_out:
                is_intractable = True

        print("Q" + str(index) + "-> A:" + msg)


def perform_submit():
    submit = driver.find_element(By.CSS_SELECTOR, "input[value=提交]")
    is_intractable = False
    while not is_intractable:
        is_intractable = True
        try:
            submit.click()
        except:
            print("Waiting for return...")
            sleep(0.5)
            is_intractable = False


def wait_return():
    while driver.current_url != "http://jwc.swjtu.edu.cn/vatuu/AssessAction?setAction=list":
        sleep(1)
        print("Waiting return...")


def perform_enter():
    entry = driver.find_element(By.LINK_TEXT, "填写问卷")

    is_intractable = False
    while not is_intractable:
        is_intractable = True
        try:
            entry.click()
        except:
            is_intractable = False
            sleep(0.5)
            print("Waiting for start...")


if __name__ == "__main__":
    driver.get('http://jwc.swjtu.edu.cn/vatuu/UserLoginForWiseduAction')

    driver.find_element(By.ID, 'username').send_keys(username)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.CLASS_NAME, 'lang_text_ellipsis.login-btn').click()

    while driver.current_url != 'http://jwc.swjtu.edu.cn/vatuu/UserFramework':
        sleep(1)
        print("Waiting logging...")

    print("Successfully Logged in")

    driver.get('http://jwc.swjtu.edu.cn/vatuu/AssessAction?setAction=list')

    entries = driver.find_elements(By.LINK_TEXT, "填写问卷")

    while len(entries):
        print(entries)
        perform_enter()
        perform_act()
        perform_submit()
        wait_return()
        sleep(1)
