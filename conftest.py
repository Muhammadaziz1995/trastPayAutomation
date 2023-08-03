import json
import os
import subprocess

import pytest
from appium import webdriver
from appium.webdriver.appium_service import AppiumService

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

BUNDLE_ID = "trastpay.uz"

pytest_plugins = [
   "flows.flow_factory",
]


def pytest_addoption(parser):
    parser.addoption("--data", action="store", default="")
    parser.addoption("--platform", action="store", default="android")
    parser.addoption('--repeat', action='store',
                     help='Number of times to repeat each test')
    # parser.addoption("--emulator_1", action="store", default="Pixel_6_Pro_API_10.0")
    parser.addoption("--emulator_1", action="store", default="Pixel_6_Pro_30_11.0")
    # parser.addoption("--emulator_2", action="store", default="")
    # parser.addoption("--emulator_3", action="store", default="")
    # parser.addoption("--emulator_4", action="store", default="")
    parser.addoption("--app_path", action="store", default="C:\\Users\\user\\Desktop\\trastpay-automation\\apps\\"
                                                           "trastPay_1.1.16.debug.apk")


@pytest.fixture(scope="module")
def data_user_a(request):
    return load_data("default_data_for_user_a")


@pytest.fixture(scope="module")
def data_user_b(request):
    return load_data("default_data_for_user_b")


@pytest.fixture(scope="module")
def data_user_c(request):
    return load_data("default_data_for_user_c")


@pytest.fixture(scope="module")
def country_codes(request):
    return load_data("country_codes")


def load_data(file_name):
    with open(PATH('data/%s.json' % file_name)) as data_file:
        json_str = data_file.read()
    return json.loads(json_str)


@pytest.fixture(scope="session")
def platform(request, pytestconfig):
    return pytestconfig.getoption('--platform')


@pytest.fixture(scope="session")
def app_path(request, pytestconfig):
    return pytestconfig.getoption('--app_path')


@pytest.fixture()
def emulator_1(request, pytestconfig, platform, app_path):
    appium_server_1 = AppiumService()
    appium_server_1.start(
        args=[
            '--address',
            '127.0.0.1',
            '--port',
            '4723',
            '--base-path',
            '/wd/hub'
        ]
    )
    # appium_server_1.start(args=["-a", "0.0.0.0", "-p", "4723"])
    # appium_server_1.start(a="0.0.0.0", p="4723")
    # appium_server_1.start(address="0.0.0.0", p="4723")
    request.addfinalizer(appium_server_1.stop)
    emulator_name = pytestconfig.getoption('--emulator_1')
    url = 'http://localhost:4723/wd/hub'
    request.instance.driver_1 = webdriver.Remote(url, setup_capabilities(platform, emulator_name, app_path))

    def teardown():
        request.instance.driver_1.close_app()
        request.instance.driver_1.quit()
        if platform == "android":
            subprocess.Popen('adb -s emulator-5554 emu kill', shell=True)

    request.addfinalizer(teardown)


@pytest.fixture()
def emulator_2(request, pytestconfig, platform, app_path):
    appium_server_2 = AppiumService()
    # appium_server_2.start(args=["-a", "0.0.0.0", "-p", "4724"])
    appium_server_2.start(a="0.0.0.0", p="4724")

    request.addfinalizer(appium_server_2.stop)
    emulator_name = pytestconfig.getoption('--emulator_2')
    url = 'http://localhost:4723/wd/hub'
    request.instance.driver_2 = webdriver.Remote(url, setup_capabilities(platform, emulator_name, app_path))

    def teardown():
        request.instance.driver_2.close_app()
        request.instance.driver_2.quit()
        if platform == "android":
            subprocess.Popen('adb -s emulator-5556 emu kill', shell=True)

    request.addfinalizer(teardown)


@pytest.fixture()
def emulator_3(request, pytestconfig, platform, app_path):
    appium_server_3 = AppiumService()
    appium_server_3.start(args=["-a", "0.0.0.0", "-p", "4725"])
    request.addfinalizer(appium_server_3.stop)
    emulator_name = pytestconfig.getoption('--emulator_3')
    url = 'http://localhost:4723//wd//hub'
    request.instance.driver_3 = webdriver.Remote(url, setup_capabilities(platform, emulator_name, app_path))

    def teardown():
        request.instance.driver_3.close_app()
        request.instance.driver_3.quit()
        if platform == "android":
            subprocess.Popen('adb -s emulator-5558 emu kill', shell=True)

    request.addfinalizer(teardown)


def setup_capabilities(platform, emulator_name, app_path):
    if platform == "android":
        capabilities = {
            'platformName': 'Android',
            'platformVersion': emulator_name.split('_')[-1],
            'deviceName': emulator_name,
            'avd': emulator_name,
            'newCommandTimeout': 3600,
            'noReset': True,
            'app': PATH(app_path),
            'appWaitDuration': 300000,
            'avdReadyTimeout': 500000,
            'adbExecTimeout': 500000,
            'automationName': 'UiAutomator2',
            'appPackage': 'trastpay.uz',
            'appActivity': 'uz.trastpay.ui.activity.MainActivity'
        }
        return capabilities


@pytest.fixture
def restart_app(request):
    request.instance.driver.activate_app(BUNDLE_ID)

    def teardown():
        request.instance.driver.terminate_app(BUNDLE_ID)

    request.addfinalizer(teardown)


# This function below is showing doc string of test functions
def pytest_itemcollected(item):
    par = item.parent.obj
    node = item.obj
    pref = par.__doc__.strip() if par.__doc__ else par.__class__.__name__
    suf = node.__doc__.strip() if node.__doc__ else node.__name__
    if suf:
        item._nodeid = item._nodeid + ': -- ' + suf + ' --'


def pytest_generate_tests(metafunc):
    if metafunc.config.option.repeat is not None:
        count = int(metafunc.config.option.repeat)

        # We're going to duplicate these tests by parametrizing them,
        # which requires that each test has a fixture to accept the parameter.
        # We can add a new fixture like so:
        metafunc.fixturenames.append('tmp_ct')

        # Now we parametrize. This is what happens when we do e.g.,
        # @pytest.mark.parametrize('tmp_ct', range(count))
        # def test_foo(): pass
        metafunc.parametrize('tmp_ct', range(count))
