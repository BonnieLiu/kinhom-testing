#coding: utf-8
from selenium import webdriver
import unittest
import time


class BaseCase(unittest.TestCase):
	def setUp(self):
		self.dr = webdriver.Chrome()
		self.dr.get('http://www.kinhom.com')

	def by_name(self,the_name):
		return self.dr.find_element_by_name(the_name)

	def by_id(self,the_id):
		return self.dr.find_element_by_id(the_id)

	def by_class_name(self,the_class_name):
		return self.dr.find_element_by_class_name(the_class_name)

	def by_xpath(self,the_xpath):
		return self.dr.find_element_by_xpath(the_xpath)

	def by_css(self,the_css):
		return self.dr.find_element_by_css_selector(the_css)

	def tearDown(self):
		print'after every test'
		self.dr.quit()
