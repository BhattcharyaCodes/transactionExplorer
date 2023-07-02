# from selenium.webdriver.common.by import By
#
#
# # https://blockstream.info/block/000000000000000000076c036ff5119e5a5a74df77abf64203473364509f7732
# # Below the block details div, you will see the transaction list section
#
class WebLocators:
    BLOCK_DETAILS = "div.transactions>h3"
    TRANSACTION_IDS = ".txn>a"
    TRANSACTION_LIST_INPUTS = ".transaction-box>div.ins-and-outs>div.vins"
    TRANSACTION_LIST_OUTPUTS = ".transaction-box>div.ins-and-outs>div.vouts"

# hashmap = {}
#
# # Example key-value pairs
# obj1 = "Value 1"
# obj2 = "Value 2"
# obj3 = "Value 3"
#
# # Assigning values to the hashmap
# hashmap[id(obj1)] = ("Tuple 1", "String 1")
# hashmap[id(obj2)] = ("Tuple 2", "String 2")
# hashmap[id(obj3)] = ("Tuple 3", "String 3")
#
# # Printing the elements of the hashmap
# for key, value in hashmap.items():
#     print(f"ID: {key}")
#     print(f"Tuple Value: {value[0]}")
#     print(f"String Value: {value[1]}")
#     print()
