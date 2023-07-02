import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
import allure
import locator


@pytest.mark.usefixtures("setup")
class TestHomePage:
    @allure.title("setup")
    @allure.description("Test setup")
    def test_setup(self):
        try:
            options = Options()
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            transaction_url = "https://blockstream.info/block/000000000000000000076c036ff5119e5a5a74df77abf64203473364509f7732"
            chrome_driver_path = '/path/to/chromedriver'
            driver = webdriver.Chrome(chrome_driver_path, chrome_options=options)
            assert ("blockstream" in transaction_url)
        except WebDriverException as e:
            print("An error occurred while opening the URL:", e)
        finally:
            assert False
            driver.quit()

@pytest.fixture(scope='session')
class TestPage:
    @allure.title("Transaction Test")
    @allure.description("Validate the section has the heading 25 of 2875 Transactions")
    def test_transaction(self):
        expected_text = "25 of 2875 Transactions"
        elem_text = locator.BLOCK_DETAILS.text
        assert elem_text == expected_text, f"Element text '{elem_text}' does not match expected text '{expected_text}'"

    @allure.description("Parse & Validate the 1 in 2 Op, transaction")
    def test_homepage_title(self):
        t_id = locator.TRANSACTION_ID
        transaction_in_elements = locator.TRANSACTION_LIST_INPUT
        transaction_out_elements = locator.TRANSACTION_LIST_OUTPUT
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

        for key, value in hashMap.items():
            if value == (1, 2):
                print("Found (1,2) pairing for Transaction id:", hashMap[key])
                assert True
                driver.quit()
            else:
                assert False
                driver.quit()
