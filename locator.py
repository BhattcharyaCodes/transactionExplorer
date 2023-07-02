from selenium.webdriver.common.by import By
driver = None
# https://blockstream.info/block/000000000000000000076c036ff5119e5a5a74df77abf64203473364509f7732
# Below the block details div, you will see the transaction list section.
# div.transactions>h3

BLOCK_DETAILS = driver.find_element(By.CSS_SELECTOR, "div.transactions>h3")
TRANSACTION_ID = driver.find_elements(By.CSS_SELECTOR, ".txn>a")
TRANSACTION_LIST_INPUT = driver.find_elements(By.CSS_SELECTOR, ".transaction-box>div.ins-and-outs>div.vins")
TRANSACTION_LIST_OUTPUT = driver.find_elements(By.CSS_SELECTOR, ".transaction-box>div.ins-and-outs>div.vouts")