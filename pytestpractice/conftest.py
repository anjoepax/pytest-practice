import pytest


@pytest.fixture
def setup():
    print("Once before every method")
    yield
    print("Once after every method")


@pytest.fixture(scope="class")
def one_time_setup(request, browser, os_type):
    print("One time module setup")
    print("Running on OS type: " + str(os_type))
    if browser == "chrome":
        value = 10
        print("Browser is chrome...")
    elif browser == "firefox":
        value = 20
        print("Browser is firefox...")
    else:
        value = 30
        print("Browser is on edge...")
    if request.cls is not None:
        request.cls.value = value
    yield value
    print("One time module teardown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--os_type", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def os_type(request):
    return request.config.getoption("--os_type")

