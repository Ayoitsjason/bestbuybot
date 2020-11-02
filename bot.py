from selenium import webdriver
from config import keys
import time
import check_price, send_email


def order(k):
    driver = webdriver.Chrome('chromedriver')

    driver.get(k['product_url'])

    driver.find_element_by_xpath('//*[@id="pdpMain"]/section/div[4]/div/div[3]/form/button/span[1]').click()
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="cart-checkout-btn"]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="dwfrm_singleshipping_email_emailAddress"]').send_keys(k["email"])
    driver.find_element_by_xpath('//*[@id="dwfrm_singleshipping_shippingAddress_addressFields_firstName"]').send_keys(k["firstname"])
    driver.find_element_by_xpath('//*[@id="dwfrm_singleshipping_shippingAddress_addressFields_lastName"]').send_keys(k["lastname"])
    driver.find_element_by_xpath('//*[@id="dwfrm_singleshipping_shippingAddress_addressFields_address1"]').send_keys(k["address"])
    driver.find_element_by_xpath('//*[@id="dwfrm_singleshipping_shippingAddress_addressFields_address2"]').click()
    driver.find_element_by_xpath('//*[@id="dwfrm_singleshipping_shippingAddress_addressFields_city"]').send_keys(k["city"])
    driver.find_element_by_xpath('//*[@id="dwfrm_singleshipping_shippingAddress_addressFields_states_state"]/option[7]').click()
    driver.find_element_by_xpath('//*[@id="dwfrm_singleshipping_shippingAddress_addressFields_postal"]').send_keys(k["zip"])
    driver.find_element_by_xpath('//*[@id="dwfrm_singleshipping_shippingAddress_addressFields_country"]').click()
    driver.find_element_by_xpath('//*[@id="dwfrm_singleshipping_shippingAddress_addressFields_phone"]').send_keys(k["phone"])
    driver.find_element_by_xpath('//*[@id="dwfrm_singleshipping_shippingAddress_useAsBillingAddress"]').click()
    driver.find_element_by_xpath('//*[@id="dwfrm_singleshipping_shippingAddress"]/fieldset[2]/div/button[1]/span').click()
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="is-CREDIT_CARD"]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="dwfrm_billing_paymentMethods_creditCard_owner"]').send_keys(k["owner"])
    time.sleep(2)
    print(k["cardnumber"])
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[4]/div/div[1]/form/fieldset[3]/div[1]/div[1]/div[2]/div[2]/div[1]/input').send_keys(k["cardnumber"])
    print('test 2')
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="dwfrm_billing_paymentMethods_creditCard_expiration_month"]/option[8]').click()
    driver.find_element_by_xpath('//*[@id="dwfrm_billing_paymentMethods_creditCard_expiration_year"]/option[3]').click()
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[4]/div/div[1]/form/fieldset[3]/div[1]/div[1]/div[2]/div[4]/div/div[3]/div[1]/input').send_keys(k["cvv"])

    print('finished')

if __name__ == '__main__':
    order(keys)