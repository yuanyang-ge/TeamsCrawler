import os
import pprint
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

load_dotenv()


#usernameStr = os.environ.get('EMAIL')
#passwordStr = os.environ.get("PASSWORD")
usernameStr = ""
passwordStr = ""
browser = webdriver.Chrome(
    #executable_path=os.environ.get('HOME')+"/myConky/scripts/chromedriver"
    executable_path="./drv/chromedriver"
)
browser.get(
    'https://login.microsoftonline.com/common/oauth2/v2.0/authorize?response_type=id_token&scope=openid%20profile&client_id=5e3ce6c0-2b1f-4285-8d4b-75ee78787346&redirect_uri=https%3A%2F%2Fteams.microsoft.com%2Fgo&state=eyJpZCI6IjVmYzk5NDEwLThlYjctNDFjMy04YzlhLWYzZWJkMWQxZWQ4OSIsInRzIjoxNjc4MTE1NDY4LCJtZXRob2QiOiJyZWRpcmVjdEludGVyYWN0aW9uIn0%3D&nonce=ac54b04e-1537-4932-a011-6769717573dc&client_info=1&x-client-SKU=MSAL.JS&x-client-Ver=1.3.4&client-request-id=446f83ab-fad2-4f69-8381-63500795e881&response_mode=fragment&sso_reload=true'
)


# Email input field
WebDriverWait(browser, 10).until(
    EC.presence_of_element_located(
        (By.ID, 'i0116')
    )
)
username = browser.find_element(By.ID, 'i0116')
username.send_keys(usernameStr)

# Click the next button
browser.find_element(By.ID, 'idSIButton9').click()

#Input field for password
WebDriverWait(browser, 10).until(
    EC.presence_of_element_located(
        (By.ID, 'i0118')
    )
)

password = browser.find_element(By.ID, 'i0118')
password.send_keys(passwordStr)

# sleep for sometime beacuse there is some overlay
time.sleep(10)
#click the submit button
element = browser.find_element(By.ID, 'idSIButton9').click()
# again same reason
time.sleep(20)
#click Yes button
element = browser.find_element(By.ID, 'idBtn_Back').click()

# time to load the Assignments page
# time.sleep(25)

WebDriverWait(browser, 30).until(
    EC.presence_of_element_located(
        (
            By.CLASS_NAME,
            'profile-img-parent'
        )
    )
)

time.sleep(30)

msgContent = browser.find_elements(By.XPATH, '//*[@data-tid="messageBodyContent"]/div')
for msgTxt in msgContent:
    print(msgTxt.get_attribute('innerText'))
