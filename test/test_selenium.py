from selenium import webdriver
from time import sleep
# 实例化两个浏览器
driver_edge = webdriver.Edge()
#分别打开百度等35
my_url = "https://www.baidu.com/"
driver_edge.get(my_url)
sleep(3)
# 分别退出
driver_edge.quit()