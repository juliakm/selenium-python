from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from faker import Faker

# create new Faker
fake = Faker()
first_name = fake.first_name()
last_name = fake.last_name()
email = (first_name + last_name).lower() + '@mailinator.com'

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()


# navigate to 1608 p2p form
driver.get("https://1608-p2p-refund5.qa.jacksonriverdev.com/content/p2p-test-donation-form?p2p_pcid=26")

# amount field
amount = driver.find_element_by_xpath('.//*[@id=\'edit-submitted-donation-amount\']/div[3]').click()

# First Name
driver.find_element_by_id("edit-submitted-donor-information-first-name").send_keys(first_name)

# Last Name
driver.find_element_by_id("edit-submitted-donor-information-last-name").send_keys(last_name)

# Email Address
driver.find_element_by_id("edit-submitted-donor-information-mail").send_keys(email)

# Address
driver.find_element_by_id("edit-submitted-billing-information-address").send_keys("111 Testing Lane")

# City
driver.find_element_by_id("edit-submitted-billing-information-city").send_keys("San Diego")

# State/Province
driver.find_element_by_xpath("//select[@id='edit-submitted-billing-information-state']/option[@value='NC']").click()

# Zip
driver.find_element_by_id("edit-submitted-billing-information-zip").send_keys("27705")


### Billing Information

# Credit Card Number
driver.find_element_by_id("edit-submitted-payment-information-payment-fields-credit-card-number").send_keys("4111111111111111")

# Expiration Year
driver.find_element_by_xpath("//select[@id='edit-submitted-payment-information-payment-fields-credit-expiration-date-card-expiration-year']/option[@value='2020']").click()


# CVV
driver.find_element_by_id("edit-submitted-payment-information-payment-fields-credit-card-cvv").send_keys('123')

# Checkbox check
driver.execute_script('document.getElementById("edit-springboard-p2p-personal-campaign-action-show-name").click()')

# Submit
driver.find_element_by_id('edit-submit').click()

