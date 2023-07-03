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

    @allure.title("Transaction Test 2")
    @allure.description("Parse & Validate the 1 in 2 Op, transaction")
    def test_homepage(self):
        try:
            t_id = self.driver.find_elements(By.CSS_SELECTOR, str(WebLocators.TRANSACTION_IDS))
            transaction_in_elements = self.driver.find_elements(By.CSS_SELECTOR,
                                                                str(WebLocators.TRANSACTION_LIST_INPUTS))
            transaction_out_elements = self.driver.find_elements(By.CSS_SELECTOR,
                                                                 str(WebLocators.TRANSACTION_LIST_OUTPUTS))
            tid_size = []
            tin_size = []
            tout_size = []
            for el in t_id:
                tid_size.append(el.text)
            #2nd appproach using list of elements
            for i in range(25):
                for el in transaction_in_elements:
                    print(el)
                    count_of_divs_in = len(el.find_elements_by_xpath("./div"))
                    print("tin_size", count_of_divs_in)
                    if count_of_divs_in == 1:
                        for el in transaction_out_elements:
                            count_of_divs_out = len(el.find_elements_by_xpath("./div"))
                            if count_of_divs_out == 2:
                                print("tout_size", count_of_divs_out)
                                print(tid_size[i])
                                return
            self.driver.close()
        except NoSuchElementException:
            print("Element not found on the page.")
            self.driver.close()

    """
                    First the total elements inside the vins will be found using the size of the elements inside vins,
                    we save the value for each length of element in a hash map. There will be a loop for 25 transactions,
                    each loop will generate the size of the vins div. Similarly the same will be done for the vouts and saving
                    the output in the same hashmap
                For each transaction, the transaction hash can also be saved in the same hashmap when the loop is running
                At the end of the loop, the hash map that corresponds to a 1:2 ins and outs will be the one we need to print
                Print out the transaction id for that on console
        """


if __name__ == "__main__":
    test = TestTransactionPage()
    test.setUp()
    test.test_transaction()
    test.test_homepage()
