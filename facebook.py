import os
import random
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
import json , time , threading
from time import sleep
from selenium.webdriver import ActionChains
def login(driver,mail,passw):
    try:
        driver.implicitly_wait(30)
        user = driver.find_element(By.ID, value='email')
        user.send_keys(mail)
        time.sleep(1)
        password = driver.find_element(By.ID, value='pass')
        password.send_keys(passw)
        time.sleep(2)
        button_log = driver.find_element(By.ID, value='loginbutton')
        button_log.click()
        time.sleep(5)
        try:
            driver.find_element(By.ID, value='pass')    
            print('[-] Error For Login Try Check Password')
            with open('error.txt','a+') as f:
                f.write(mail,' | ',passw+'\n')
            return 'Error'
        except:
            return 'Done'
        driver.close()
    except:
        return'check'
def get_cookies(path):
    with open(f'{path}.txt','r') as accountfile:
        read_acc = accountfile.read().split('\n')
        x = 1
        for i in read_acc:
            account = i.split(':')
            driver = webdriver.Chrome()
            driver.get('https://facebook.com/login')
            check_login = login(driver,account[0],account[1])
            if check_login == 'Done':
                with open(f'{x}.txt', 'w+') as filehandler:

                    cookies = json.dump(driver.get_cookies(), filehandler)
                    x += 1
            elif check_login == 'Error':
                pass
            driver.close()
def login_cookies(path,link,sleep_,number):
    for i in range(1,number+1):
        driver = uc.Chrome(use_subprocess=True)
        driver.get('https://facebook.com/login')
        with open(f'{path}.txt', 'r') as cookiesfile:
            cookies = json.load(cookiesfile)
        for cook in cookies:
            driver.add_cookie(cook)
        driver.refresh()
        time.sleep(1)
        driver.get(link)
        print('[-] Collect Time Now')
        time.sleep(2)
        time.sleep(sleep_)
        driver.close()
def view_live(path,link,sleep_):
    driver = uc.Chrome(use_subprocess=True)
    driver.get('https://facebook.com/login')
    with open(f'{path}.txt', 'r') as cookiesfile:
        cookies = json.load(cookiesfile)
    for cook in cookies:
        driver.add_cookie(cook)
    driver.refresh()
    driver.get(link)
    time.sleep(2)
    try:
        driver.find_element(By.ID, value='pass')    
        print('[-] Error For Login Try Check Password')
    except:
        print(f'[-] Watching Live Now ==> {path}')
        time.sleep(2)
        time.sleep(sleep_*60)
        driver.close()
def follow_page(path,link):
    driver = uc.Chrome(use_subprocess=True)
    driver.get('https://facebook.com/login')
    with open(f'{path}.txt', 'r') as cookiesfile:
            cookies = json.load(cookiesfile)
    for cook in cookies:
        driver.add_cookie(cook)
    driver.refresh()
    time.sleep(1)
    try:
        driver.get(link)
        time.sleep(1)
        try:
            driver.implicitly_wait(10)
            follow_button = '/html/body/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr/td[2]/a'
            driver.find_element(By.XPATH, follow_button).click()
            follow_done = '<span class="cu">Following</span>'
            while True:
                if follow_done in driver.page_source:
                    print('[-] Follow Done')
                    break
            driver.close()
        except:
            print('Error')
            
    except:
        pass
def like_post(path,id):
    driver = uc.Chrome(use_subprocess=True)
    driver.get('https://facebook.com/login')
    try:
        with open(f'{path}.txt', 'r') as cookiesfile:
            cookies = json.load(cookiesfile)

        for cook in cookies:
            driver.add_cookie(cook)

        driver.refresh()
        reacton = f'https://mbasic.facebook.com/reactions/picker/?is_permalink=1&ft_id={id}'
        driver.get(reacton)
        time.sleep(1)
        try:
            driver.implicitly_wait(30)
            #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            x = ['care','love','wow']
            random_rec = random.choice(x)
            if random_rec == 'wow':
                wow = driver.find_element(By.XPATH, value='/html/body/div/div/div[2]/div/table/tbody/tr/td/ul/li[5]/table/tbody/tr/td/a')
                wow.click()
                sleep(2)
            elif random_rec == 'love':
                love = driver.find_element(By.XPATH, value='/html/body/div/div/div[2]/div/table/tbody/tr/td/ul/li[2]/table/tbody/tr/td/a')            
                love.click()
                sleep(2)
            elif random_rec == 'care':
                care = driver.find_element(By.XPATH, value='/html/body/div/div/div[2]/div/table/tbody/tr/td/ul/li[3]/table/tbody/tr/td/a')
                care.click()
                sleep(2)
            driver.close()
        except:
            print('error')
            with open('error.txt','a+') as f:
                f.write(path)
    except:
        pass
def like_reels(path,link):
    driver = uc.Chrome(use_subprocess=True)
    driver.get('https://facebook.com/login')
    try:
        with open(f'{path}.txt', 'r') as cookiesfile:
            cookies = json.load(cookiesfile)

        for cook in cookies:
            driver.add_cookie(cook)

        driver.refresh()
        driver.get(link)
        time.sleep(1)
        try:
            driver.implicitly_wait(30)
            like_buton = driver.find_element(By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[1]/div/i')
            like_buton.click()
            driver.close()
        except:
            print('error')
            with open('error.txt','a+') as f:
                f.write(path)
    except:
        pass

os.system('cls')
ask1 = int(input('''
[1] - Open Facebook Script
[2] - Get Cookie's
[-] Select Number: '''))
if ask1 == 1:
    ask2 = int(input('''[1] - Reels - View
[2] - Reels - Likes
[3] - Follow - Page
[4] - Like - Posts
[5] - Stream Views
[-] Select Number: '''))
    if ask2 == 1:
        n1 = int(input('First number of mails: '))
        n2 = int(input('Third number of mails: '))
        link_video = input('Link Of Video: ')
        sleep_ = int(input('Seconds Sleep: '))
        nuum = int(input('The number of views per account: '))
        for i in range(n1,n2+1):
            threading.Thread(target=login_cookies,args=(i,link_video,sleep_,nuum)).start()

    elif ask2 == 2:
        n1 = int(input('First number of mails: '))
        n2 = int(input('Third number of mails: '))
        link_post = input('Link for Reel-Post: ')
        for i in range(n1,n2+1):
            threading.Thread(target=like_reels,args=(i,link_post)).start()      

    elif ask2 == 3:
        n1 = int(input('First number of mails: '))
        n2 = int(input('Third number of mails: '))
        link_page = input('Link for Post: ')

        for i in range(n1,n2+1):
            threading.Thread(target=follow_page,args=(i,link_page)).start() 

    elif ask2 == 4:
        n1 = int(input('First number of mails: '))
        n2 = int(input('Third number of mails: '))
        link_post = input('Link for Post: ')

        for i in range(n1,n2+1):
            threading.Thread(target=like_post,args=(i,link_post)).start()
    elif ask2 == 4:
        n1 = int(input('First number of mails: '))
        n2 = int(input('Third number of mails: '))
        link_video = input('Link Of Video: ')
        sleep_ = int(input('Seconds Sleep: '))
        for i in range(n1,n2+1):
            threading.Thread(target=login_cookies,args=(i,link_video,sleep_)).start()
elif ask1 == 2:
    path = input('Write filename for acc: ')
    get_cookies(path)
