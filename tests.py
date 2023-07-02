import pytest as pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
import allure

from locator import WebLocators


# @pytest.mark.smoke()
class TestTransactionPage:
    @allure.title("setup")
    @allure.description("Test setup")
    def __init__(self):
        try:
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument("--window-size=1920x1080")
            chrome_options.add_argument("--verbose")
            transaction_url = "https://blockstream.info/block" \
                              "/000000000000000000076c036ff5119e5a5a74df77abf64203473364509f7732"
            chrome_driver_path = 'usr/local/bin/chromedriver'
            # '/path/to/chromedriver'
            self.driver = webdriver.Chrome()
                # chrome_driver_path, options=chrome_options)
            self.driver.get(transaction_url)
        except WebDriverException as e:
            print("An error occurred while opening the URL:", e)

    # @pytest.fixture(scope='session')
    @allure.title("Transaction Test 1")
    @allure.description("Validate the section has the heading 25 of 2875 Transactions")
    def test_transaction(self):
        expected_text = "25 of 2875 Transactions"
        elem_text = self.driver.find_element(WebLocators.BLOCK_DETAILS).text
        assert elem_text == expected_text, f"Element text '{elem_text}' does not match expected text '{expected_text}'"

    @allure.title("Transaction Test 2")
    @allure.description("Parse & Validate the 1 in 2 Op, transaction")
    def test_homepage(self):
        t_id = self.driver.find_elements(WebLocators.TRANSACTION_ID)
        transaction_in_elements = self.driver.find_elements(WebLocators.TRANSACTION_LIST_INPUT)
        transaction_out_elements = self.driver.find_elements(WebLocators.TRANSACTION_LIST_OUTPUT)
        hashMap = {}

        #     First the total elements inside the vins will be found using the size of the elements inside vins,
        #     we save the value for each length of element in a hash map. There will be a loop for 25 transactions,
        #     each loop will generate the size of the vins div. Similarly the same will be done for the vouts and saving
        #     the output in the same hashmap
        # For each transaction, the transaction hash can also be saved in the same hashmap when the loop is running
        # At the end of the loop, the hash map that corresponds to a 1:2 ins and outs will be the one we need to print
        # Print out the transaction id for that on console

        for i in list(range(25)):
            key = t_id[i].text
            t_in = transaction_in_elements[i].size
            t_out = transaction_out_elements[i].size
            value = (t_in, t_out)
            hashMap[key] = value
            print(hashMap[key, value])

        for key, value in hashMap.items():
            if value == (1, 2):
                print("Found (1,2) pairing for Transaction id:", hashMap[key])
                assert True
                self.driver.quit()
            else:
                assert False
                self.driver.quit()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    test = TestTransactionPage()
    # test.test_setup()
    test.test_transaction()
    test.test_homepage()
    test.tearDown()
