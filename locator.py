from selenium.webdriver.common.by import By

# https://blockstream.info/block/000000000000000000076c036ff5119e5a5a74df77abf64203473364509f7732
# Below the block details div, you will see the transaction list section.
driver = None


class WebLocators(object):
    BLOCK_DETAILS = (By.CSS_SELECTOR, "div.transactions>h3")
    TRANSACTION_ID = (By.CSS_SELECTOR, ".txn>a")
    TRANSACTION_LIST_INPUT = (By.CSS_SELECTOR, ".transaction-box>div.ins-and-outs>div.vins")
    TRANSACTION_LIST_OUTPUT = (By.CSS_SELECTOR, ".transaction-box>div.ins-and-outs>div.vouts")
