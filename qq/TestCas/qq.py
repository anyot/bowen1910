# !/usr/bin/env python
# -*-coding:utf8-*-
# Project_name:untitled1
# File_name:qq.py
# Author: yu yu
# Time:2020年04月01日
import unittest
from commone.qqHelper import Helper
from time import sleep

class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.Helper=Helper()

    @classmethod
    def tearDownClass(cls):
        cls.Helper.quit()

    def test01(self):
        '''发消息'''
        sleep(20)
        self.Helper.w_elem('id','com.tencent.mobileqq:id/et_search_keyword').click()
        self.Helper.w_elem('id','com.tencent.mobileqq:id/et_search_keyword').send_keys("宇")
        self.Helper.w_elem('xpath','//android.widget.TextView[@text="宇宙无敌大宝蛋"]').click()
        self.Helper.save_screencap()
        sleep(1)
        self.Helper.w_elem('id','com.tencent.mobileqq:id/input').click()
        self.Helper.w_elem('id','com.tencent.mobileqq:id/input').send_keys("宝宝")
        self.Helper.w_elem('id','com.tencent.mobileqq:id/fun_btn').click()
        self.Helper.save_screencap()
        sleep(1)

if __name__=='__main__':
    unittest.main()
