import pytest
import allure

@allure.title("Verify ✅pass!! if the framework works")
@allure.description("Verify if the framework works")
def test_sample_pass():
    assert True == True

@allure.title("Verify 🛑 Fail!! if the framework works")
@allure.description("Verify if the framework works")
def test_sample_fail():
    assert True == False