#coding: utf-8
#金海马商城购物车删除+unittest框架+重构(20150202，还未运行成功,运行已成功，20150213已运行成功)
#未断言- -

import unittest
from selenium import webdriver
import time
from base_case import BaseCase
from common.login import login 

class CartDelete(BaseCase):

	def test_cart_delete(self):
		self.dr.get('http://www.kinhom.com/goods-5513-2.html')
		self.dr.maximize_window()
		time.sleep(5)
		#点击“加入购物车”按钮
		self.by_id('tag_cart').click()
		time.sleep(3)
		#点击“查看购物车”按钮
		self.by_class_name('btn1').click()
		time.sleep(3)
		#购物车点击“删除”的图标
		self.by_class_name('ui-cart-list-del ').click()		
		#删除提示框点击“确定”按钮
		self.by_id('J_msgDialogOk').click()

if __name__  == '__main__':
	unittest.main()