def donate(url, recurs = False, ocd = False, type = 'credit', first_name = None, last_name = None, mail = None, address = None, credit_card = '4111111111111111'):

    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions
    from faker import Faker

    # create new Faker
    fake = Faker()
    faker_first_name = fake.first_name()
    faker_last_name = fake.last_name()
    faker_mail = (first_name + last_name).lower() + '@mailinator.com'
    faker_address = fake.building_number() + ' ' + fake.street_name()
    # create a new Firefox session
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    #driver.maximize_window()

    # navigate to 1608 p2p form
    driver.get(url)

    # amount field
    amount = driver.find_element_by_xpath('.//*[@id=\'edit-submitted-donation-amount\']/div[3]').click()

    # First Name
    if first_name is None:
        driver.find_element_by_id("edit-submitted-donor-information-first-name").send_keys(faker_first_name)
    else:
        driver.find_element_by_id("edit-submitted-donor-information-first-name").send_keys(first_name)

    # Last Name
    if first_name is None:
        driver.find_element_by_id("edit-submitted-donor-information-last-name").send_keys(faker_last_name)
    else:
        driver.find_element_by_id("edit-submitted-donor-information-last-name").send_keys(last_name)


    # Email Address
    if mail is None:
        driver.find_element_by_id("edit-submitted-donor-information-mail").send_keys(faker_mail)
    else:
        driver.find_element_by_id("edit-submitted-donor-information-mail").send_keys(mail)

    # Address
    if address is None:
        driver.find_element_by_id("edit-submitted-billing-information-address").send_keys(faker_address)
    else:
        driver.find_element_by_id("edit-submitted-billing-information-address").send_keys(address)

    # City
    driver.find_element_by_id("edit-submitted-billing-information-city").send_keys("Durham")

    # State/Province
    driver.find_element_by_xpath(
        "//select[@id='edit-submitted-billing-information-state']/option[@value='NC']").click()

    # Zip
    driver.find_element_by_id("edit-submitted-billing-information-zip").send_keys("27705")

    ### Billing Information

    if type == 'credit':

    # Credit Card Number
        driver.find_element_by_id("edit-submitted-payment-information-payment-fields-credit-card-number").send_keys(
        credit_card)

    # Expiration Year
    driver.find_element_by_xpath(
        "//select[@id='edit-submitted-payment-information-payment-fields-credit-expiration-date-card-expiration-year']/option[@value='2020']").click()

    # CVV
    driver.find_element_by_id("edit-submitted-payment-information-payment-fields-credit-card-cvv").send_keys('123')

    if recurs == True:
        driver.find_element_by_id("edit-submitted-payment-information-recurs-monthly-1").click()

    if ocd == True:
        driver.find_element_by_id("edit-submitted-payment-information-payment-fields-credit-ocd").click()

    # Submit
    driver.find_element_by_id('edit-submit').click()


    # Check for confirmation
    #driver.implicitly_wait(30)  # seconds
    #element = driver.find_element_by_tag_name('h1')
    #assert element.text == 'Thank you for your donation!'

current_form = 'https://qa.jacksonriverdev.com/node/3'

donate(current_form,recurs=True, ocd=True, mail="testing@jacksonriver.com", first_name='Antwan', last_name='Authorize', credit_card='2223000010309711', address="1300 Carolina Ave")

#donate(current_form,recurs=True, ocd=False)
