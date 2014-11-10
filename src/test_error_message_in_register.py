from selenium import webdriver
import os, sys
lib_path = os.path.abspath('./')
from pages import *
import variables


browser = webdriver.Firefox()
browser.get('http://www.lazada.vn/')
page = MainPage(browser)
page.do_a_sing_up('ausfkajsf@gmail.com', 'male')
