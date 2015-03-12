#coding=utf-8
#金海马商城加入购物车购买流程+unittest框架+已经重构(运行成功，20150213)
#有一个问题，怎么断言？？下完单之后的订单号与用户中心第一个的订单号是否相等？？
import unittest
from selenium import webdriver
import time
from base_case import BaseCase
from common.login import login

class OrderCart(BaseCase):

	def test_order_cart(self):
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

if __name__  == '__main__':
	unittest.main()