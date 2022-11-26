
from Features import Layout
from BaseFiles import InitiateDriver

def testCheckElement():
    driver = InitiateDriver.StartBrowser()
    layout = Layout.LayoutClass(driver)
    layout.validateMenu()
    layout.stepperValidation()
    layout.upperPanelFeature()
    layout.firstForm()
    layout.secondFormFirstStep()