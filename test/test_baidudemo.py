import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@allure.feature("百度搜索")
@pytest.mark.parametrize('test_data',['allure','pytest','unitest'])
def test_steps_demo(test_data):
    with allure.step("打开百度网页"):
        driver = webdriver.Edge()
        driver.get("http://www.baidu.com")
        driver.maximize_window()

    with allure.step(f"输入搜索词:{test_data}"):
        driver.find_element(By.ID,"kw").send_keys(test_data)
        time.sleep(2)
        driver.find_element(By.ID,"su").click()
        time.sleep(2)

    with allure.step("保存图片"):
        driver.save_screenshot("./result/b.png")
        allure.attach.file("./result/b.png",attachment_type=allure.attachment_type.PNG)
    with allure.step("关闭浏览器"):
        driver.quit()