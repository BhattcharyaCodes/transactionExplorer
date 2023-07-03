from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from locator import WebLocators


class TestTransactionPage:
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_transaction(self):
        try:
            self.driver.get("https://blockstream.info/block" \
                            "/000000000000000000076c036ff5119e5a5a74df77abf64203473364509f7732")
            elem = self.driver.find_element(By.CSS_SELECTOR, "div.transactions>h3")
            elem_text = elem.text
            print(elem_text)
        except NoSuchElementException:
            print("Element not found on the page.")

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
        except NoSuchElementException:
            print("Element not found on the page.")




if __name__ == "__main__":
    test = TestTransactionPage()
    test.setUp()
    test.test_transaction()
    test.test_homepage()
