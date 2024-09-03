from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote
from bs4 import BeautifulSoup
import time

# Specify the path to your chromedriver
chrome_service = Service('C:/Users/1234a/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe')

# Initialize the WebDriver with the Service object
driver = webdriver.Chrome(service=chrome_service)

# Maximize the window to avoid layout issues
driver.maximize_window()

def fetch_all_job_data(role, location="United States", geo_id="103644278", time_filter="r86400"):
    # URL encode the role to make it safe for a URL
    encoded_role = quote(role)
    
    # Construct the LinkedIn job search URL
    url = f'https://www.linkedin.com/jobs/search/?keywords={encoded_role}&location={quote(location)}&geoId={geo_id}&f_TPR={time_filter}&f_JT=C&position=1&pageNum=0'
    
    # Open the LinkedIn Jobs page
    driver.get(url)
    
    # Wait for the job results to appear
    try:
        job_elements = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'ul.jobs-search__results-list li'))
        )
        
        # Loop through each job in the list on the first page
        for index in range(len(job_elements)):
            # Refetch job elements to avoid stale element reference
            job_elements = driver.find_elements(By.CSS_SELECTOR, 'ul.jobs-search__results-list li')
            job_element = job_elements[index]
            
            # Click the job to load the description
            job_element.click()
            
            # Wait for the job description to load
            job_description_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'show-more-less-html__markup.relative.overflow-hidden'))
            )
            
            # Extract the inner HTML of the job description
            job_description_html = job_description_element.get_attribute("innerHTML").strip()
            
            # Use BeautifulSoup to convert the HTML to text
            soup = BeautifulSoup(job_description_html, 'html.parser')
            job_description_text = soup.get_text(separator="\n").strip()
            
            print(f"Job {index + 1} Description (Text):\n{job_description_text}\n{'-'*80}\n")
            
            # Pause for a few seconds before moving to the next job
            time.sleep(3)  # Adjust time as needed
            
    except Exception as e:
        # Handle the error more gracefully
        print(f"An error occurred: {e}")

# Prompt the user to input the role
role = input("Enter the job role you want to search for: ")

# Fetch and display the job descriptions for all roles on the first page
fetch_all_job_data(role)


##    # Ask the user if they want to quit the browser
##quit_browser = input("Quit browser? (Y/N): ").strip().upper()
##
### Close the browser based on user input
##if quit_browser == 'Y':
##    driver.quit()
##else:
##    print("Browser will remain open.")



driver.quit()









##from selenium import webdriver
##from selenium.webdriver.chrome.service import Service
##from selenium.webdriver.common.by import By
##from selenium.webdriver.support.ui import WebDriverWait
##from selenium.webdriver.support import expected_conditions as EC
##import time
##from urllib.parse import quote
##
### Specify the path to your chromedriver
##chrome_service = Service('C:/Users/1234a/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe')
##
### Initialize the WebDriver with the Service object
##driver = webdriver.Chrome(service=chrome_service)
##
### Maximize the window to avoid layout issues
##driver.maximize_window()
##
### List of roles to search for
##roles = [
##    "DevOps Engineer",
##    "Java Developer",
##    "Data Engineer",
##    "Data Analyst",
##    "Python Developer",
##    "Cloud Engineer"
##]
##
### Location and other filters (you can adjust these as needed)
##location = "United States"
##geo_id = "103644278"  # Geo ID for the United States
##time_filter = "r86400"  # Jobs posted in the last 24 hours
##
### Loop through each role
##for role in roles:
##    # URL encode the role to make it safe for a URL
##    encoded_role = quote(role)
##    
##    # Construct the LinkedIn job search URL
##    url = f'https://www.linkedin.com/jobs/search/?keywords={encoded_role}&location={quote(location)}&geoId={geo_id}&f_TPR={time_filter}&f_JT=C&position=1&pageNum=0'
##    
##    # Open a new tab
##    driver.execute_script("window.open('');")
##    
##    # Switch to the new tab
##    driver.switch_to.window(driver.window_handles[-1])
##    
##    # Open the LinkedIn Jobs page for the current role in the new tab
##    driver.get(url)
##    
##    # Wait for the job count element to appear
##    try:
##        job_count_element = WebDriverWait(driver, 20).until(
##            EC.presence_of_element_located((By.CSS_SELECTOR, 'span.results-context-header__job-count'))
##        )
##        job_count = job_count_element.text.strip()
##        print(f"Number of {role} jobs posted in the last 24 hours: {job_count}")
##    except Exception as e:
##        # Handle the error more gracefully
##        print(f"An error occurred while searching for {role}: {e}")
##    
##    # Wait for a few seconds before moving to the next role (e.g., 5 seconds)
##    time.sleep(5)
##
### Close all tabs and quit the browser
##driver.quit()




