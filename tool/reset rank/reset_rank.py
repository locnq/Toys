from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from tqdm import tqdm
import time


def _send_get(idin, browser):
    try:
        roleid = browser.find_element_by_xpath(
            '/html/body/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/form/div[3]/div/input')
        roleid.clear()
        roleid.send_keys('{}'.format(idin))
        time.sleep(0.5)

        btnSubmit = browser.find_element_by_xpath(
            '/html/body/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/form/div[4]/div/button')
        btnSubmit.click()

        time.sleep(2)
        openid = browser.find_element_by_xpath(
            '/html/body/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div[4]/div/div[2]/div[1]/table/tbody/tr/td[12]')

        return idin, openid.text
    except:
        return idin, ''


def run():
    path = 'openid'
    default_delay = 0.5
    browser = webdriver.Chrome('C:\\chromedriver')

    browser.get('http://49.51.228.253/ajax/ajax.html')
    browser.maximize_window()

    time.sleep(5)

    browser.find_element_by_id("txtLoginName")
    login = browser.find_element_by_id("txtLoginName")
    login.send_keys('vng001')

    passwordbar = browser.find_element_by_id("txtPassword")
    passwordbar.send_keys('pubgmpg3!@#')

    a = input('\nEnter capcha on browser, when done press Enter!\n')

    infor_page = browser.find_element_by_xpath('//*[@id="first_menus_7588"]')
    infor_page.click()

    time.sleep(default_delay)

    infor_page = browser.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[4]/a')
    infor_page.click()

    time.sleep(default_delay)

    infor_page = browser.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[4]/ul/li[7]/a')
    infor_page.click()

    time.sleep(default_delay)

    time.sleep(default_delay)

    point = browser.find_element_by_name('value')
    point.send_keys('{}'.format(1200))

    time.sleep(default_delay)

    reason = browser.find_element_by_xpath(
        '/html/body/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/form/div[8] /div/textarea'
    )
    reason.send_keys('{}'.format('hack'))

    print('Giải thích (trên browser)')
    print('1. North America')
    print('2. Europe')
    print('3. Asia')
    print('4. South America')
    print('5. Russia')
    print('6. Japan and South Korea')
    a = input('Chọn server trên browser rồi bấm Enter ở đây')

    rank_type = [15, 16, 17, 18, 19, 20]

    submit = browser.find_element_by_xpath(
        '/html/body/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/form/div[9] /div/button'
    )


    openid = browser.find_element_by_name('openid')
    type = browser.find_element_by_name('type')

    time.sleep(2)

    # with open('roleid.txt', 'r', encoding='utf-8') as r:
    #     while True:
    #         idin = r.readline().split('\n')[0]
    #         if idin == '':
    #             break
    #         print(idin)
    #
    #         idin, openid = _send_get(idin, browser)
    #
    #         if not openid == '':
    #             with open(path + 'id-openid.txt', 'a', encoding='utf-8') as w2:
    #                 w2.write('{}\t{}\n'.format(idin, openid))
    #                 w2.close()
    #
    #             with open(path + 'openid_need_to_ban.txt', 'a', encoding='utf-8') as w3:
    #                 w3.write('{}\n'.format(openid))
    #                 w3.close()
    #         else:
    #             with open(path + 'error_id.txt', 'a', encoding='utf-8') as we:
    #                 we.write('{}\tkhông tìm được openid\n'.format(idin))
    #                 we.close()
    #         print(openid)
    #         print()
    #     r.close()
    # print("Done!")

    with open('openid_need_to_reset.txt', 'r') as r:
        g = r.readlines()
        r.close()

    openids = [i.replace('\n', '') for i in g]

    # submit reset rank
    pro_bar = tqdm(openids)
    for opid in pro_bar:
        pro_bar.set_description('Reseting OpenID {}'.format(opid))
        openid.clear()
        time.sleep(0.5)
        openid.send_keys('{}'.format(opid))

        for t in rank_type:
            type.clear()
            time.sleep(0.5)
            type.send_keys('{}'.format(t))
            time.sleep(2.5)
            submit.click()

while True:
    run()
    a = input('Chạy thêm lần nữa? Chọn server trên browser rồi bấm Enter ở đây')
a = input('Done!')