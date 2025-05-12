from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Runs Chrome in headless mode (no GUI)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set path to chromedriver
service = Service("/usr/local/bin/chromedriver")

# Create WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to a website
driver.get("https://example.com")

# Print the title of the page
print("Page title is:", driver.title)

# Clean up
driver.quit()
