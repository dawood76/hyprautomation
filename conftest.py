import pytest
from pytest import fixture

#pytest_plugins = 'allure.pytest_plugin'
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
         action="store"
    )
    parser.addoption(
        "--baseurl",
         action="store"
    )

@pytest.fixture(scope="session", autouse=True)
def browser(request):
    return request.config.getoption("--browser")
    #request.addfinalizer(finalizer_function)

@pytest.fixture(scope="session", autouse=True)
def baseurl(request):
    return request.config.getoption("--baseurl")
