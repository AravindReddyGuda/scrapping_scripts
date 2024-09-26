from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import random
CN=input('Enter the 26-digit Survey Number: ')
CN1 = CN[0:5]
CN2 = CN[5:10]
CN3 = CN[10:15]
CN4 = CN[15:20]
CN5 = CN[20:25]
CN6 = CN[25:26]

# Specify the path to your chromedriver
chrome_service = Service('C:/Users/1234a/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe')
# Initialize the WebDriver with the Service object
driver = webdriver.Chrome(service=chrome_service)
# Maximize the window to avoid layout issues
driver.maximize_window()
# Open the local survey page
driver.get("https://www.mcdvoice.com/")

# Sleep for a few seconds to ensure the page is fully loaded
time.sleep(2)

# Function to fill out the survey inputs
def fill_survey():
    # Fill out the input fields for the survey code
    driver.find_element(By.ID, 'CN1').send_keys(str(CN1))
    driver.find_element(By.ID, 'CN2').send_keys(str(CN2))
    driver.find_element(By.ID, 'CN3').send_keys(str(CN3))
    driver.find_element(By.ID, 'CN4').send_keys(str(CN4))
    driver.find_element(By.ID, 'CN5').send_keys(str(CN5))
    driver.find_element(By.ID, 'CN6').send_keys(str(CN6))
    
    # Click the "NextButton" before answering the questions (assuming it's a separate step)
    next_button = driver.find_element(By.ID, 'NextButton')
    next_button.click()

    # Randomly answer the multiple-choice questions (if applicable)
    # Assuming each question has inputs of type 'radio' with the class 'question-class'
    questions = driver.find_elements(By.CLASS_NAME, 'question-class')  # Update with the actual class name
    for question in questions:
        options = question.find_elements(By.TAG_NAME, 'input')
        random.choice(options).click()  # Randomly select one option per question
    
    # Submit the form (assuming the submit button has id='submit')
    driver.find_element(By.ID, 'submit').click()


# Call the function to fill and submit the survey
fill_survey()

# Sleep for a few seconds to observe the result (optional)
time.sleep(5)

# Close the browser
driver.quit()
