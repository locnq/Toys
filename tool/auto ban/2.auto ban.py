from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

br = webdriver.Chrome('C:\\chromedriver')
br.maximize_window()

USERNAME = "vng001"
PASSWORD = "pubgmpg3!@#"
BAN_TIME = "{}".format(60 * 60 * 24 * 365 * 10)
#                    sec * min * hour * day * year
BAN_REASON = "Your account will be banned for violating regulation."
OP_REASON = "Check Hack" # or Refund or Something else


br.get('http://49.51.228.253/ajax/ajax.html')

time.sleep(5)

br.find_element_by_id("txtLoginName")
login = br.find_element_by_id("txtLoginName")
login.send_keys(USERNAME)


passwordbar = br.find_element_by_id("txtPassword")
passwordbar.send_keys(PASSWORD)

a = input('\nEnter capcha on browser, when done press Enter!\n')

time.sleep(1)

ban_title = br.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[6]/ul/li[2]/a')
ban_title.click()

time.sleep(1)

ban_time = br.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/form/div[5]/div/input')
ban_time.send_keys(BAN_TIME)

time.sleep(1)

bann_reason = br.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/form/div[6]/div/input')
bann_reason.send_keys(BAN_REASON)

time.sleep(1)

ban_operation_reason = br.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/form/div[8]/div/textarea')
ban_operation_reason.send_keys(OP_REASON)

a = input('\nRe-check ban information, if they not ok, then you can change them, when all are ok, press Enter!\n') 

def _ban_openid(openid):
    ban_openid = br.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/form/div[4]/div/input')
    ban_openid.send_keys('{}'.format(openid))

    btnSubmit = br.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/form/div[9]/div/button')
    btnSubmit.click()
    time.sleep(1)
    ban_openid.clear()

with open('openid_need_to_ban.txt', 'r', encoding='utf-8') as r:
    while True:
        openid = r.readline().split('\n')[0]
        if openid == '':
            break
        _ban_openid(openid)
        print(openid)
        time.sleep(0.5)
    r.close()
    
print("Done!")
