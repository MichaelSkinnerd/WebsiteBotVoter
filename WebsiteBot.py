from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the driver (e.g., Chrome)
driver = webdriver.Chrome()

#Number of times the Bot will run.
num_iterations = 200

for i in range(num_iterations):
# Open the webpage
    driver.get('Insert URL Here')

    # Wait for 5 seconds
    time.sleep(5)

    wait = WebDriverWait(driver, 10)
    # Find the checkboxes by 'aria-labelledby' (replace 'labelledbyValue' with the actual values)
    checkbox1 = wait.until(EC.presence_of_element_located((By.XPATH,  '//input[@value="2000\'s"]')))
    checkbox2 = wait.until(EC.presence_of_element_located((By.XPATH,  '//input[@value="Other"]')))

    # Click the checkboxes if they are not already selected
    if not checkbox1.is_selected():
        checkbox1.click()
    if not checkbox2.is_selected():
        checkbox2.click()

    # Locate the input box using the aria-label attribute **Used for company Music Poll
    input_box = driver.find_element(By.XPATH, '//input[@aria-label="Single line text"]')
    input_box.send_keys('Polka')
    time.sleep(5)

    # Find the submit button by the text on it and click it
    submit_button = driver.find_element(By.XPATH, "//button[contains(.,'Submit')]")
    submit_button.click()

    # Close the browser session
    time.sleep(5)
    #Message that will appear in output when a run is complete
    print(f"Runs {i+1} completed.")

#End Bot when runs are complete
driver.quit()

