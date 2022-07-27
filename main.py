from ast import arg
import threading
from selenium import webdriver
import random, os
from selenium.webdriver.common.keys import Keys
import warnings
from colorama import Fore, init


init()
warnings.filterwarnings("ignore")
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('--disable-logging')
options.add_argument('--log-level=3')
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)


def bot(code, username):
    try:
        username = username+'-'+str(random.randint(0, 9999999))
        driver.execute_script(f'''window.open("", "{username}");''')
        driver.switch_to.window(username)
        driver.get('https://kahoot.it/')
        easyfind_name('gameId', code)
        easyfind_xpath('//*[@id="root"]/div[1]/div/div/div/div[3]/div[2]/main/div/form/button', True)
        easyfind_name('nickname', username)
        easyfind_xpath('//*[@id="root"]/div[1]/div/div/div[1]/div/div[2]/main/div/form/button', True)
        print(Fore.GREEN + f'    [+] {username} joined !')
    except Exception as e:
        print(Fore.RED + f'    [-] {username} failed !')

def easyfind_xpath(xpath, click):
    while True:
        try:
            if click == True:
                driver.find_element_by_xpath(xpath).click()
            else:
                driver.find_element_by_xpath(xpath)
            break
        except Exception as e:
            pass

def easyfind_name(name, key):
    while True:
        try:
            if key != '':
                driver.find_element_by_name(name).send_keys(key)
            else:
                driver.find_element_by_name(name)
            break
        except Exception as e:
            pass

os.system('cls')
un = str(input('    username : '))
code = int(input('    game code : '))
bn = int(input('    how much bot you want : '))
print('\n\n\n')
for i in range(bn):
    x = threading.Thread(target=bot, args=(code, un))
    x.start()
    x.join()
