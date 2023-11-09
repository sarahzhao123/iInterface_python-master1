import allure
@allure.link("http://www.baidu.com",name="链接")
def test_with_link():
    print("这是一条加了链接的测试")
    pass

TEST_CASE_LINK="http://www.baidu.com"
@allure.testcase(TEST_CASE_LINK,"登录用例")
def test_with_testcase_link():
    print("这是一条测试用例的链接，链接到测试用例里面")
    pass

def test_attach_text():
    allure.attach("这是一个纯文本",attachment_type=allure.attachment_type.TEXT)

def test_attach_html():
    allure.attach("<body>这是一段htmlbody块</body>","html测试块",attachment_type=allure.attachment_type.HTML)

def test_attach_photo():
    allure.attach("G:\iInterface_python-master1\\resource\小怪物.jpg",name="这是一个小怪物的图片",attachment_type=allure.attachment_type.JPG)