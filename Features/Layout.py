
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec





class LayoutClass:

    def __init__(self, obj):
        global driver
        driver = obj

    def validateMenu(self):
        driver.find_element(By.XPATH, "//span[contains(text(), 'Layout')]").click()
        driver. find_element(By.XPATH, "//a[@title='Stepper']")
        driver.find_element(By.XPATH, "//a[@title='Accordion']")

    def stepperValidation(self):
        WebDriverWait(driver, timeout=3).until(ec.element_to_be_clickable((By.XPATH, "//a[@title='Stepper']"))).click()


    def upperPanelFeature(self):
        WebDriverWait(driver, timeout=3).until(ec.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'next')][1]")))
        element = driver.find_element(By.XPATH, "//button[contains(text(), 'prev')][1]")
        prop = element.get_property('disabled')
        assert (prop == True)
        element1 = driver.find_element(By.XPATH, "//button[contains(text(), 'next')][1]")
        prop1 = element1.get_property('disabled')
        assert (prop1 == False)

    def firstForm(self):
        driver.find_element(By.XPATH, "//span[contains(text(), '1')]")
        driver.find_element(By.XPATH, "//span[contains(text(), '2')]")
        driver.find_element(By.XPATH, "//span[contains(text(), '3')]")
        driver.find_element(By.XPATH, "//span[contains(text(), '4')]")
        driver.find_element(By.XPATH, "//h3[contains(text(), 'Step content #1')][1]")
        WebDriverWait(driver, timeout=3).until(ec.element_to_be_clickable((By.XPATH, "//button[@type='submit'][2]"))).click()
        driver.find_element(By.XPATH, "//h3[contains(text(), 'Step content #2')]")
        element = driver.find_element(By.XPATH, "//button[contains(text(), 'prev')][1]")
        prop = element.get_property('disabled')
        assert (prop == False)
        WebDriverWait(driver, timeout=3).until(ec.element_to_be_clickable((By.XPATH, "//button[@type='submit'][1]"))).click()
        driver.find_element(By.XPATH, "//h3[contains(text(), 'Step content #3')]")
        WebDriverWait(driver, timeout=3).until(ec.element_to_be_clickable((By.XPATH, "//button[@type='submit'][1]"))).click()
        driver.find_element(By.XPATH, "//h3[contains(text(), 'Step content #4')]")
        element = driver.find_element(By.XPATH, "//button[contains(text(), 'prev')][1]")
        prop = element.get_property('disabled')
        assert (prop == False)

    def secondFormFirstStep(self):
        driver.find_element(By.XPATH, "//span[contains(text(), '1')]")
        driver.find_element(By.XPATH, "//span[contains(text(), '2')]")
        driver.find_element(By.XPATH, "//span[contains(text(), '3')]")
        element = driver.find_element(By.XPATH, "//p[@class='lorem']")
        text = element.get_property('innerText')
        assert (text == "Lorizzle ipsum dolizzle stuff fizzle, consectetuer adipiscing break it down. Nullizzle sapien velizzle, my shizz pimpin', shizzle my nizzle crocodizzle shut the shizzle up, gravida vizzle, dang.")
        element = driver.find_element(By.XPATH, "//input[@placeholder = 'Enter your name']")
        placeholder = element.get_property('placeholder')
        assert (placeholder == "Enter your name")
        element.send_keys('1234')
        element1=driver.find_element(By.XPATH, "//form[1]/child::button")
        element1.click()
        #driver.find_element(By.XPATH("xpath=//form[@class='step-container ng-pristine ng-invalid ng-star-inserted ng-touched']/child::button"))

        #prop1 = element1.get_property('disabled')
        #assert (prop1 == True)
        #element.send_keys('1234')
        #element1.click()


        #1st = class ='col-md-12 col-lg-12 col-xxxl-12']
        #2nd = //div[@class='col-md-12 col-lg-6 col-xxxl-6'][1]








