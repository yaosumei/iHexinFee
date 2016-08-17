#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page_object.appium_page_objects import PageObject, page_element


class FenshiKxianPage(PageObject):
	fanhui_button = page_element(accessibility_id='返回')
	xiayigegupiao_button = page_element(accessibility_id = '下一个股票')
	shangyigegupiao_button = page_element(accessibility_id = '上一个股票')

	jiazixuan_staText = page_element(accessibility_id='加自选')

	def hx_right(self):
		el1 = self.w.get_window_size()
		width = el1.get('width')
		height = el1.get('height')
		start_x = width * (67 / 375.0)
		start_y = height * (134 / 667.0)
		end_x = width * (344 / 375.0)
		end_y = height * (134 / 667.0)
		self.w.swipe(start_x, start_y, end_x, end_y, duration=500)

	def hx_left(self):
		el1 = self.w.get_window_size()
		width = el1.get('width')
		height = el1.get('height')
		start_x = width * (344 / 375.0)
		start_y = height * (134 / 667.0)
		end_x = width * (67 / 375.0)
		end_y = height * (134 / 667.0)
		self.w.swipe(start_x, start_y, end_x, end_y, duration=500)