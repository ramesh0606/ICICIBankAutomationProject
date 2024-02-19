''''
1. open browser
2. navigate to icici webpage
3. goto Login button place
4. verify 'New user' option is available. if option is available, it is PASS, if option is not available, test case is failure.
'''
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

#open chrome browser

option=Options()
option.add_experimental_option("detach",True)
driver=WebDriver(options=option)
driver.implicitly_wait(30)
driver.get("https://www.icicibank.com/")
driver.maximize_window()
print("current url:",driver.current_url)
print("get title:", driver.title)

#Locate login button & use move_to_element method

action=ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "//button[@class=\"hed-dropdown-toggle login-toggle\"]/span")).perform()
elements=driver.find_elements(By.XPATH, "//div[@class=\"hed-dropdown-list login-list\"]/ul/li")
print("elements:",len(elements), type(len(elements)))
resultFlag=False
for i in range(1, len(elements)+1):
    if driver.find_element(By.XPATH, "//div[@class=\"hed-dropdown-list login-list\"]/ul/li["+str(i)+"]/a").text == "New User1":
        resultFlag=True

if resultFlag == True:
    print("test is pass")
else:
    print("failed")