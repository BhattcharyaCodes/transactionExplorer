# transactionExplorer
BITGO

Pre-requisites:
1) Install Java 8, set path variable
2) Install Python 3.6 or above
3) Downlaod & unzip Chromedriver compatible to your driver from, 
https://chromedriver.chromium.org/downloads , OR
https://chromedriver.storage.googleapis.com/index.html .
4) Place the chrome exec file in /usr/local/bin or /usr/bin and add it to $PATH.
6) Download and install selenium wedriver:   `  brew install selenium-server` , start selenium services using, `brew services start selenium-server`
7) Install selenium library using pip, `pip3 install selenium`

We are set with system setup.

Instructions to run the tests:
1) Clone the repo
2) Add chromedriver externally and replace the path in line no. 17 of tests.py,   --->      `chrome_driver_path = '/path/to/chromedriver'`
3) ```pip install -r requirements.txt```
4) Run the command, for allure test reports, `pytest --alluredir=<path>` , --> replace path with reports directory path

OUTPUT:
![image](https://github.com/BhattcharyaCodes/transactionExplorer/assets/26433219/150f443d-822e-43bb-8c55-1e167f29fd7b)
