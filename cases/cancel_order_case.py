#coding=utf-8
#金海马商城购买然后取消订单的流程+unittest框架+已重构(运行成功)
import unittest
from selenium import webdriver
import time
from base_case import BaseCase
from common.login import login 

class CancelOrder(BaseCase):
	def test_cancel_order(self):
		username = 'test01'
		password = 'ceshiceshi'
		login(self.dr,username,password)
		self.dr.get('http://www.kinhom.com/goods-5513-2.html')
		self.dr.maximize_window()
		time.sleep(5)
		#点击“加入购物车”按钮
		self.by_id('tag_cart').click()
		time.sleep(3)
		#点击“查看购物车”按钮
		self.by_class_name('btn1').click()
		
		time.sleep(3)
		#购物车点击“去结算”按钮
		self.by_id('contin').click()
		time.sleep(3)
		#页面跳转到“确认订单”页面
		self.by_id("submitToPay").click()
		time.sleep(3)

		#点击用户名的链接，进入到用户中心
		self.by_xpath("//li[@class='loginbar']/span[1]/a").click()		
		#点击第一个订单的取消订单按钮
		self.by_xpath("//td[@class='operateLink bdr vl_middle']/p[2]/a").click()
		#点击取消订单确认框的“确定”按钮
		self.by_id('confirm_button').click()

if __name__  == '__main__':
	unittest.main()