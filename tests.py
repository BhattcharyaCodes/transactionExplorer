import pytest as pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
import allure

from locator import WebLocators
from util import chromeSession


class TestTransactionPage:
    @allure.title("setup")
    @allure.description("Test setup")
    def setUp(self):
        # self.driver = webdriver.Chrome()
        try:
            self.driver = webdriver.Chrome(options=chromeSession.chrome_options)
            self.driver.get(chromeSession.transaction_url)
        except WebDriverException as e:
            print("An error occurred while opening the URL:", e)

    @allure.title("Transaction Test 1")
    @allure.description("Validate the section has the heading 25 of 2875 Transactions")
    def test_transaction(self):
        try:
            expected_text = "25 of 2875 Transactions"
            elem = self.driver.find_element(By.CSS_SELECTOR, str(WebLocators.BLOCK_DETAILS))
            elem_text = elem.text
            print(elem_text)
            assert elem_text == expected_text, f"Element text '{elem_text}' does not match expected text '{expected_text}'"
        except NoSuchElementException:
            print("Element not found on the page.")
        finally:
            self.driver.quit()
    @allure.title("Transaction Test 2")
    @allure.description("Parse & Validate the 1 in 2 Op, transaction")
    def test_homepage(self):
        hashmap = {}
        try:
            t_id = self.driver.find_elements(By.CSS_SELECTOR, str(WebLocators.TRANSACTION_IDS))
            transaction_in_elements = self.driver.find_elements(By.CSS_SELECTOR, str(WebLocators.TRANSACTION_LIST_INPUTS))
            transaction_out_elements = self.driver.find_elements(By.CSS_SELECTOR, str(WebLocators.TRANSACTION_LIST_OUTPUTS))
            tid_size = []
            for el in t_id:
                tid_size.append(el.text)
                # key = tid_size[el]
            tin_size = []
            for el in transaction_in_elements:
                tin_size.append(el.size)
            tout_size = []
            for el in transaction_out_elements:
                tout_size.append(el.size)

            for i in list(range(25)):
             hashmap[id(tid_size[i])] = (tin_size[i],tout_size[i])
        except NoSuchElementException:
            print("Element not found on the page.")
        """
                    First the total elements inside the vins will be found using the size of the elements inside vins,
                    we save the value for each length of element in a hash map. There will be a loop for 25 transactions,
                    each loop will generate the size of the vins div. Similarly the same will be done for the vouts and saving
                    the output in the same hashmap
                For each transaction, the transaction hash can also be saved in the same hashmap when the loop is running
                At the end of the loop, the hash map that corresponds to a 1:2 ins and outs will be the one we need to print
                Print out the transaction id for that on console
        """
        for key, value in hashmap.items():
            if {value[0]} == 1 & {value[1]} == 2:
                print("Found (1,2) pairing for Transaction id:", hashMap[{key}])
                assert True
            else:
                assert False
                self.driver.quit()

    def teardown(self):
        self.driver.close()


if __name__ == "__main__":
    test = TestTransactionPage()
    test.setUp()
    test.test_transaction()
    test.test_homepage()
    # test.tearDown()
