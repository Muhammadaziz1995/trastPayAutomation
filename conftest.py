import json
import os
import subprocess


import pytest
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from allure import attachment_type
import allure
from appium.options.android import UiAutomator2Options


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
    parser.addoption("--emulator_1", action="store", default="Pixel_6_Pro_11.0")
    # parser.addoption("--emulator_2", action="store", default="")
    # parser.addoption("--emulator_3", action="store", default="")
    # parser.addoption("--emulator_4", action="store", default="")
    parser.addoption("--app_path", action="store", default="./apps/"
                                                           "trastPay_1.1.26.05.debug.apk")


@pytest.fixture(scope="session")
def platform(request, pytestconfig):
    return pytestconfig.getoption('--platform')


@pytest.fixture(scope="session")
def app_path(request, pytestconfig):
    return pytestconfig.getoption('--app_path')


global driver_1, driver_2, driver_3, request


@pytest.fixture()
def get_screenshot_on_failed_case(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(request.instance.driver_1.get_screenshot_as_png(),
                      name="failed_test",
                      attachment_type=attachment_type.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def emulator_1(request, pytestconfig, platform, app_path):

    appium_server_1 = AppiumService()
    appium_server_1.start(
        args=[
            '--address',
            '0.0.0.0',
            '--port',
            '4723',
            '--base-path',
            '/wd/hub'
        ],
        main_script="/Applications/Appium Server GUI.app/Contents/Resources/app/node_modules/appium/build/lib/main.js",
        node="/usr/local/bin/node",
        npm="/usr/local/bin/npm"
    )
    # appium_server_1.start(args=["-a", "0.0.0.0", "-p", "4723"])
    # appium_server_1.start(a="0.0.0.0", p="4723")
    # appium_server_1.start(address="0.0.0.0", p="4723")
    request.addfinalizer(appium_server_1.stop)
    emulator_name = pytestconfig.getoption('--emulator_1')
    url = 'http://localhost:4723/wd/hub'
    capabilities_options = UiAutomator2Options().load_capabilities(setup_capabilities(platform, emulator_name, app_path))
    request.instance.driver_1 = webdriver.Remote(url, options=capabilities_options)

    def teardown():
        request.instance.driver_1.terminate_app('trastpay.uz')
        request.instance.driver_1.quit()
        if platform == "android":
            subprocess.Popen('adb -s emulator-5554 emu kill', shell=True)

    request.addfinalizer(teardown)

    # @pytest.hookimpl(hookwrapper=True, tryfirst=True)
    # def pytest_runtest_makereport(item, call):
    #     pytest_html = item.config.pluginmanager.getplugin('html')
    #     outcome = yield
    #     report = outcome.get_result()
    #     report.session = item.session
    #     extras = getattr(report, "extras", [])
    #     if report.when == "call" or report.when == "setup":
    #         extras.append(pytest_html.extras.url(""))
    #         xfail = hasattr(report, "wasxfail")
    #         if (report.skipped and xfail) or (report.failed and not xfail):
    #             report_directory = os.path.dirname(item.config.option.htmlpath)
    #             file_name = report.nodeid.replace("::", "_") + ".png"
    #             destination_file = os.path.join(report_directory, file_name)
    #             # request.instance.driver_1.save_screenshot(destination_file)
    #             request.instance.driver_1.get_screenshot_as_file(destination_file)
    #             allure.attach(request.instance.driver_1.save_screenshot(file_name), name="file_name", attachment_type=allure_commons.attachment_type.PNG)
    #             if file_name:
    #                 html = '<div><img src="%s" alt="screenshot" style="width:300px;height=200px" onclick="window.open(this.src align="right")"></div>' % file_name
    #             extras.append(pytest_html.extras.html(html))
    #         report.extras = extras


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
# def pytest_html_report_title(report):
#     report.title = "Mobile Automation Report"


def setup_capabilities(platform, emulator_name, app_path):
    if platform == "android":
        capabilities = {
            'platformName': 'Android',
            'appium:platformVersion': emulator_name.split('_')[-1],
            'appium:deviceName': emulator_name,
            'appium:avd': emulator_name,
            'appium:newCommandTimeout': 3600,
            'appium:noReset': True,
            'appium:app': PATH(app_path),
            'appium:appWaitDuration': 300000,
            'appium:avdReadyTimeout': 500000,
            'appium:adbExecTimeout': 500000,
            'appium:automationName': 'UiAutomator2',
            'appium:appPackage': 'trastpay.uz',
            'appium:appActivity': 'uz.trastpay.ui.activity.MainActivity'
        }
    else:
        capabilities = {
            "platformName": "iOS",
            "appium:platformVersion": "15.5",
            "appium:deviceName": "iPhone 12 Pro Max",
            "appium:automationName": "XCUITest",
            # "appium:app": "/Users/muhammadaziz/Desktop/AnorMobile/app/AnorMobile.app",
            "appium:adbExecTimeout": "500000",
            "appium:appWaitDuration": "300000",
            "appium:noReset": True,
            "appium:newCommandTimeout": "3600"
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
