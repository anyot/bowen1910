# !/usr/bin/env python
# -*-coding:utf8-*-
# Project_name:untitled1
# File_name:qqHelper.py
# Author: yu yu
# Time:2020年04月01日
from appium import webdriver
import time
import os
from selenium.webdriver.support.ui import WebDriverWait
import yaml
import logging
from logging import config
with open(r'E:\qq\configg\qq.yaml','r',encoding='utf-8')as file:
    data = yaml.load(file,Loader=yaml.FullLoader)
desired_cap={
    'platformName':data['platformName'],
    'platformVersion':data['platformVersion'],
    'deviceName':data['deviceName'],
    'appPackage':data['appPackage'],
    'appActivity':data['appActivity'],
    'noReset':False
}
# print(desired_cap)
logging.config.fileConfig(r'E:\qq\configg\log.conf')
logging = logging.getLogger()

class Helper():
    def __init__(self):
        logging.info('start-up app')
        self.driver=webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub',desired_cap)
        logging.info('success app')

        try:
            logging.info('click agree')
            WebDriverWait(self.driver,30).until(lambda w: w.find_element_by_id('com.tencent.mobileqq:id/btn_login')).click()
        except:
            logging.info('no found agree')

        try:
            WebDriverWait(self.driver,50).until(lambda w: w.find_element_by_xpath('//android.widget.EditText[@content-desc="请输入QQ号码或手机或邮箱"]')).clear()
            WebDriverWait(self.driver, 50).until(lambda w: w.find_element_by_xpath('//android.widget.EditText[@content-desc="请输入QQ号码或手机或邮箱"]')).send_keys('865800253')
        except:
            logging.info('输入账号成功')

        try:
            WebDriverWait(self.driver, 50).until(lambda w: w.find_element_by_xpath('//android.widget.EditText[@content-desc="密码 安全"]')).send_keys('ttwan3344')

            WebDriverWait(self.driver, 50).until(lambda w: w.find_element_by_xpath( '//android.widget.ImageView[@content-desc="登 录"]')).click()
            WebDriverWait(self.driver, 50).until(lambda w: w.find_element_by_id('com.tencent.mobileqq:id/dialogRightBtn')).click()
            WebDriverWait(self.driver, 50).until(lambda w: w.find_element_by_xpath('//android.widget.ImageView[@content-desc="登 录"]')).click()
        except:
            logging.info("登陆成功")


    def quit(self):
        '''关闭app'''
        self.driver.quit()

    def w_elem(self,method,element):
        '''封装定位'''
        ele = None
        if method=='id':
            ele = WebDriverWait(self.driver,20).until(lambda w: w.find_element_by_id(element))
        elif method=='xpath':
            ele = WebDriverWait(self.driver,20).until(lambda w: w.find_element_by_xpath(element))
        elif method=='class':
            ele = WebDriverWait(self.driver,20).until(lambda w: w.find_element_by_class(element))
        elif method=='name':
            ele = WebDriverWait(self.driver,20).until(lambda w: w.find_element_by_name(element))
        elif method=='list_id':
            ele = WebDriverWait(self.driver,20).until(lambda w: w.find_elements_by_id(element))
        else:
            logging.info('There is no such positioning method')
        if ele is not None:
            return ele

    def get_now(self):
        '''获取当前时间'''
        self.now=time.strftime('%Y %m %d %H %M %S')

    def save_screencap(self):
        '''截图保存'''
        now = time.strftime('%Y%m%d%H%M%S')
        picture_path=r'E:\qq\report\screenshot\\'
        picture_name=picture_path+now+'.png'
        logging.info('get screenshot')
        self.driver.get_screenshot_as_file(picture_name)
        time.sleep(2)
        print('screenshot',now,'.png')