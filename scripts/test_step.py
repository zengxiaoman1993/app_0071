import allure

class TestSetup:
    @allure.severity(allure.severity_level.BLOCKER) # 最重要的用例
    @allure.step("我是测试步骤名称")
    def test_001(self):
        allure.attach("我是步骤描述的内容", "附件名字")

    @allure.severity(allure.severity_level.CRITICAL)  # 比较重要的用例
    def test_002(self):
        assert False

    @allure.severity(allure.severity_level.NORMAL)  # 比较重要的用例
    def test_003(self):
        assert True