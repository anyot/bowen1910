# !/usr/bin/env python
# -*-coding:utf8-*-
# Project_name:untitled1
# File_name:run.py
# Author: yu yu
# Time:2020年04月01日
import unittest
import time
import os
from configg.HTMLTestRunner import HTMLTestRunner
#测试用例所在的文件夹路径
case_path=r'E:\qq\TestCas'
report_path=r'E:\qq\report'
#通过unittest.defaultTestLoader这个属性discover方法，可以查找
#case_path目录下以stu开头的测试脚本
discover = unittest.defaultTestLoader.discover(case_path,pattern='qq.py')

if __name__ == '__main__':
    #获取当前时间
    now = str(time.strftime('%Y %m %d %H %M %S',time.localtime(time.time())))
    #测试报告存放的文件夹路径
    #测试报告的名字
    filepath=os.path.join(report_path,'%s.html'%(now))

    # 打开测试报告
    with open(filepath,'wb')as file:
        #stream:测试报告写入哪个文件
        #title:测试报告的标题
        #description:用例的描述
        #tester:作者
        #verbosity:值大于等于2，报告内容更加详细
        runner = HTMLTestRunner(stream=file,
                                title=u'测试报告',
                                description=u'用例执行情况如下',
                                tester=u'王培宇',
                                verbosity=3
                                 )
        #运用HTMLTestRunner里面的run函数
        run = HTMLTestRunner()
        runner.run(discover)