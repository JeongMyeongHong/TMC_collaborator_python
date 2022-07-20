import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import urllib3


class Crawling:
    def __init__(self):
        self.cat4 = [2, 10, 13, 3, 12, 7, 4, 5, 14, 8, 15]  # url 종류별 밑반찬 3개, 메인 3개, 국 3개, 밥 2개
        # //*[@id="id_search_category"]/table/tbody/tr[1]/td/div/div[1]/a[cat4]

        self.cat3 = range(2, 17)  # url 재료별 5페이지 (총 200개)
        # //*[@id="id_search_category"]/table/tbody/tr[1]/td/div/div[3]/a[cat3]

        self.rec = range(1, 41)  # 페이지별 40개 레시피

    def crawling(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        # driver = webdriver.Chrome("C:\chromedriver.exe", options=options)

        s = Service('D:\chromedriver.exe')
        driver = webdriver.Chrome(service=s)

        url = 'https://www.10000recipe.com/recipe/list.html'
        driver.get(url)

        categoreis = ['1']
        review_list = []

        # 장르 클릭
        for category in categoreis:
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, f'/html/body/div/div[2]/div[1]/div[1]/ul/li[1]/ul/li[{category}]/a'))).click()
            # 페이지 클릭
            for page in range(1, 11):
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                    (By.XPATH, f'//*[@id="bestList"]/div[3]/div[1]/div[1]/p/a[{page}]'))).click()
                # 도서 클릭
                for i in range(1, 40, 2):
                    title1 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                        (By.XPATH, f'//*[@id="category_layout"]/tbody/tr[{i}]/td[3]/p[1]/a[1]'))).text
                    print(f'**********************{title1}**********************')
                    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                        (By.XPATH, f'//*[@id="category_layout"]/tbody/tr[{i}]/td[3]/p[1]/a[1]'))).click()
                    for page in range(1, 12):
                        try:
                            driver.find_element(By.XPATH,
                                                f'//*[@id="infoset_oneCommentList"]/div[2]/div[1]/div/a[{page}]').click()
                            time.sleep(2)
                            for i in range(1, 7):
                                try:
                                    review = WebDriverWait(driver, 20) \
                                        .until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                                 f'#infoset_oneCommentList > div.infoSetCont_wrap.rvCmtRow_cont.clearfix > div:nth-child({i}) > div.cmtInfoBox > div.cmt_cont > span'))).text
                                    review_list.append(review)
                                    print(f'{review}')
                                except:
                                    break
                        except:
                            continue
                    driver.back()

        pd.DataFrame(review_list).to_csv('./save/2000recipes.csv', index=False)
