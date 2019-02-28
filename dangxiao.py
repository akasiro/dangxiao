# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException #超时的异常
from bs4 import BeautifulSoup
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

class spider(object):
    def start(self):
        driver = webdriver.Chrome()
        # 点击登陆微人大
        self.signinbc(driver)
        # 登陆微人大
        self.loginruc(driver)
        # 选择课程
        self.selectcourse(driver)



        #结束前等待
        input('wait')
        driver.quit()


    def signinbc(self,driver):
        driver.get('http://dxonline.ruc.edu.cn')
        wait = WebDriverWait(driver,10)
        try:
            signinb = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,'body > div.login_main > div > div.fl > a'))
            )
            signinb.click()
        except TimeoutException:
            return self.signinbc(driver)

    def loginruc(self,driver):
        input('请在网页中登陆微人大，登陆完成点击确认')
        wait = WebDriverWait(driver,10)
        try:
            homepagesign = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR,'body > div.header > div > div.logo > a.link1'))
            )
        except TimeoutException:
            return self.loginruc(driver)

    def selectcourse(self,driver):
        input('请选择课程进入课程播放界面，点击确认')
        wait = WebDriverWait(driver,10)
        #切换到播放界面
        handles = driver.window_handles
        for h in handles:
            driver.switch_to_window(h)
            try:
                wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '#myVideo'))
                )
                break
            except TimeoutException:
                continue
        #确认进入课程界面
        try:
            wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR,'#myVideo'))
            )
        except TimeoutException:
            return self.selectcourse(driver)
        #点击开始
        try:
            start = wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'body > doctype > div.content > div > div.fl > div.ts1.tanc > p'))
            )
            start.click()
        except TimeoutException:
            return self.selectcourse(driver)

        print('课程开始')
        #循环检测视频暂停
        tstop1 = True
        tstop2 = True
        tstop3 = True
        while tstop1 | tstop2 | tstop3:
            if tstop1:
                try:
                    ts1 = wait.until(
                        EC.element_to_be_clickable(
                            (By.CSS_SELECTOR, 'body > doctype > div.content > div > div.fl > div.ts21.tanc2 > p'))
                    )
                    ts1.click()
                    tstop1 = False
                except TimeoutException:
                    pass
            if tstop2:
                try:
                    ts2 = wait.until(
                        EC.element_to_be_clickable(
                            (By.CSS_SELECTOR, 'body > doctype > div.content > div > div.fl > div.ts22.tanc2 > p'))
                    )
                    ts2.click()
                    tstop2 = False
                except TimeoutException:
                    pass

            if tstop3:
                try:
                    ts3 = wait.until(
                        EC.element_to_be_clickable(
                            (By.CSS_SELECTOR, 'body > doctype > div.content > div > div.fl > div.ts23.tanc2 > p'))
                    )
                    ts3.click()
                    tstop3 = False
                except TimeoutException:
                    pass
            time.sleep(120)
        #是否继续
        learnornot = input('本课程观看完成，是否继续课程学习，否请输入N:')
        if learnornot == 'N':
            print('学习结束，按任意键关闭浏览器')
        else:
            return self.selectcourse(driver)


if __name__ == '__main__':
    dangxiaospider = spider()
    dangxiaospider.start()