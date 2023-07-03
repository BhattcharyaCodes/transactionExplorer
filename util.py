from selenium.webdriver.chrome.options import Options


class chromeSession:
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--verbose")
    transaction_url = "https://blockstream.info/block" \
                      "/000000000000000000076c036ff5119e5a5a74df77abf64203473364509f7732"
    chrome_driver_path = 'usr/local/bin/chromedriver'
