from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def _send_get(idin, browser):
    try:
        roleid = browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/form/div[3]/div/input')
        roleid.clear()
        roleid.send_keys('{}'.format(idin))
        time.sleep(0.5)

        btnSubmit = browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/form/div[4]/div/button')
        btnSubmit.click()
        
        time.sleep(2)
        openid = browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div[4]/div/div[2]/div[1]/table/tbody/tr/td[12]')

        return idin, openid.text
    except:
        return idin, ''
        
        

browser = webdriver.Chrome('C:\\chromedriver')
browser.maximize_window()


browser.get('http://49.51.228.253/ajax/ajax.html')

time.sleep(5)

browser.find_element_by_id("txtLoginName")
login = browser.find_element_by_id("txtLoginName")
login.send_keys('vng001')


passwordbar = browser.find_element_by_id("txtPassword")
passwordbar.send_keys('pubgmpg3!@#')

a = input('\nEnter capcha on browser, when done press Enter!\n')

infor_page = browser.find_element_by_xpath('//*[@id="first_menus_7587"]')
infor_page.click()

time.sleep(0.5)

roleidfind = browser.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[1]/ul/li[12]/a')
roleidfind.click()
    
time.sleep(0.5)

with open('id_need_to_ban.txt', 'r', encoding='utf-8') as r:
    while True:
        idin = r.readline().split('\n')[0]
        if idin == '':
            break
        print(idin)

        idin, openid = _send_get(idin, browser)
            
        if not openid == '':
            with open('id-openid.txt', 'a', encoding='utf-8') as w2:
                w2.write('{}\t{}\n'.format(idin, openid))
                w2.close()
            
            with open('openid_need_to_ban.txt', 'a', encoding='utf-8') as w3:
                w3.write('{}\n'.format(openid))
                w3.close()
        else:
            with open('error_id.txt', 'a', encoding='utf-8') as we:
                we.write('{}: không tìm được openid\n'.format(idin))
                we.close()
        print(openid)
        print()
    r.close()
print("Done!")