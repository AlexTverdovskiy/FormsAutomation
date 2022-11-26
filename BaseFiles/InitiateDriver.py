from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Library import ConfigReader

def StartBrowser():
    global driver

    if ((ConfigReader.ReadConfigData('Details', 'Browser'))=='Chrome'):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif ((ConfigReader.ReadConfigData('Details', 'Browser'))=='Firefox'):
        path = "./Driver/geckodriver.exe"
        driver = webdriver.Firefox(executable_path=path);
    else:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.maximize_window()
    driver.get(ConfigReader.ReadConfigData('Details', 'Application_URL'))
    return driver

def CloseBrowser():
    driver.close