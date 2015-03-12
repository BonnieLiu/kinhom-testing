#coding=utf-8
#金海马商城立即购购买流程+unittest框架+已经重构(运行成功，购买skuid=5513的商品，20150213)
import unittest
from selenium import webdriver
import time
from base_case import BaseCase
from common.login import login


class LijiGou(BaseCase):

	def test_lijigou(self):
		username = 'test01'
		password = 'ceshiceshi'
		login(self.dr,username,password)
		self.dr.get('http://www.kinhom.com/goods-5513-2.html')
		self.dr.maximize_window()
		time.sleep(5)
		#点击“立即购”按钮
		self.by_id("tag_now").click()
		time.sleep(5)
		#页面跳转到“确认订单”页面
		self.by_id("submitToPay").click()

if __name__  == '__main__':
	unittest.main()