# Reference: https://automationbyte.com/how-to-interact-with-basic-form-elements-using-selenium/

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By #https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.by.html
from selenium.webdriver.common.keys import Keys #https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.keys.html
from selenium.webdriver.chrome.options import Options
import time
import sys

from driver_path import CHROMEDRIVER_PATH

def run():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True) #keep driver open for testing
    #chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                            options=chrome_options)

    driver.get('https://practice.automationbyte.com/forms/basic-form-1')
    driver.maximize_window()
    
    driver.implicitly_wait(10)

    # Fill text input box
    driver.find_element(By.NAME, 'firstNameInput').send_keys('Michael')
    
    # Fill text input box
    driver.find_element(By.NAME, 'lastNameInput').send_keys('Branton')

    # Select radio choices
    GENDER = 'Female'
    
    try:
        if GENDER=='Male':
            driver.find_element(By.XPATH, './/*[@id="user-registration-form"]/div[1]/div[3]/div[1]/label/input').click()
        elif GENDER=='Female':
            driver.find_element(By.XPATH, './/*[@id="user-registration-form"]/div[1]/div[3]/div[2]/label/input').click()
        else:  
            raise(Exception)
    except:
        driver.quit()
        sys.exit("GENDER input was not valid. Valid inputs include ['Male', 'Female']")
        
    # Select checkboxes
    HOBBY = 'Badminton'
    
    for checkbox in driver.find_elements(By.XPATH, "//div[@class='checkbox']"):
        if checkbox.find_element(By.XPATH, '.// label').text == HOBBY:
            checkbox.find_element(By.XPATH, '.// label/input').click()
        else:
            pass
    
    # Choose from dropdown: https://www.browserstack.com/guide/python-selenium-select-dropdown
    from selenium.webdriver.support.select import Select
    
    dropdown = Select(driver.find_element(By.ID, 'countryInput'))
    dropdown.select_by_visible_text('Canada')
    
    
    #Reset form 
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="user-registration-form"]/div[2]/button[2]').click()

if __name__ == '__main__':
    run() 