import pytest
import allure

@allure.feature("登录模块")
class TestLogin:
    @allure.story("登录成功")
    def test_login_sucess(self):
        print("这是登录：测试用例，登录成功")
        pass
    @allure.story("登录失败")
    def test_login_fail(self):
        print("这是登录：测试用例，登录失败,用户名缺失")
        pass

    @allure.story("登录失败")
    def test_login_fail_a(self):
        print("这是登录：测试用例，登录失败，密码错误")
        pass

    @allure.story("登录失败")
    def test_login_fail_b(self):
        with allure.step("点击用户名"):
            print("输入用户名")
        with allure.step("点击密码"):
            print("输入密码")
        print("点击登录")
        with allure.step("点击登录之后登录失败"):
            assert '1' == 1
            print("登录失败")
        print("这是登录：测试用例，登录失败,密码缺失")
        pass

if __name__=="__main__":
    pytest.main()