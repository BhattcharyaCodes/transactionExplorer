from selenium.webdriver.common.by import By


# https://blockstream.info/block/000000000000000000076c036ff5119e5a5a74df77abf64203473364509f7732
# Below the block details div, you will see the transaction list section

class WebLocators:
    BLOCK_DETAILS = "div.transactions>h3"
    TRANSACTION_IDS = ".txn>a"
    TRANSACTION_LIST_INPUTS = ".transaction-box>div.ins-and-outs>div.vins"
    TRANSACTION_LIST_OUTPUTS = ".transaction-box>div.ins-and-outs>div.vouts"
