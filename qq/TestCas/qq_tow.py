# !/usr/bin/env python
# -*-coding:utf8-*-
# Project_name:qq
# File_name:qq_tow.py
# Author: yu yu
# Time:2020年04月07日
import unittest
from commone.qqHelper import Helper
from time import sleep
import logging


class qqLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.Helper=Helper()

    @classmethod
    def tearDownClass(cls):
        cls.Helper.quit()

    def test01(self):
        '''点击动态'''
        sleep(20)
        self.Helper.driver.tap([(748,1516),(845,1589)],30)
        self.Helper.save_screencap()
        sleep(2)

    def test02(self):
        '''进入空间'''
        sleep(10)
        self.Helper.w_elem('id','com.tencent.mobileqq:id/qzone_feed_entry').click()
        sleep(5)
        self.Helper.driver.tap([(837,87),(876,122)],50)
        self.Helper.save_screencap()
        sleep(1)

    def test03(self):
        '''发说说'''
        sleep(10)
        self.Helper.driver.tap([(120,179),(185,247)],50)
        self.Helper.w_elem('id','com.tencent.mobileqq:id/itv').click()
        self.Helper.w_elem('id', 'com.tencent.mobileqq:id/itv').send_keys("发个说说做实验")
        a = self.Helper.w_elem('id', 'com.tencent.mobileqq:id/itv').text
        self.assertEqual(a,'发个说说做实验')
        self.Helper.save_screencap()
        sleep(1)
    def test04(self):
        '''发表'''
        self.Helper.w_elem('id','com.tencent.mobileqq:id/ivTitleBtnRightText').click()
        self.Helper.save_screencap()
        sleep(10)



if __name__=='__main__':
    unittest.main()