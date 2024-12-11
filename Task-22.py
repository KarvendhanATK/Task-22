from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver 
driver = webdriver.Chrome()
driver.maximize_window()
# Navigate to the URL
driver.get("https://www.instagram.com/guviofficial/")
time.sleep(5) 

# Extract the total number of Followers and Following using Relative  XPATH 
# Use XPATH to locate the Followers and Following counts
followers_xpath = "//header[@class='x1qjc9v5 x78zum5 x1q0g3np x2lah0s x1n2onr6 x1xl8k2i x1qsaojo xc2v4qs x1ez9qw7 x1kcpa7z']//li[2]//div[1]//button[1]"  
following_xpath = "//header[@class='x1qjc9v5 x78zum5 x1q0g3np x2lah0s x1n2onr6 x1xl8k2i x1qsaojo xc2v4qs x1ez9qw7 x1kcpa7z']//li[3]//div[1]//button[1]"

followers_element = driver.find_element(By.XPATH, followers_xpath)
following_element = driver.find_element(By.XPATH, following_xpath)

followers = followers_element.get_attribute("innerText")
following = following_element.get_attribute("innerText")
time.sleep(5)

print(f"Followers: {followers}")
print(f"Following: {following}")

# Close the browser
driver.quit()
