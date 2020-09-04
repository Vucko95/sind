import shutil
from selenium import webdriver
import Xlib.display
from plan import ExecutionPlan
import os
import os.path
from pyvirtualdisplay.smartdisplay import SmartDisplay


PWD = os.getenv("PWD")
DEBUG = os.getenv("DEBUG", True)
DOWNLOADS_DIR = os.getenv("DOWNLOADS_DIR", "{}/downloads/".format(PWD))
CHROME_EXEC_PATH = os.getenv("CHROME_DRIVER", "{}/drivers/chromedriver".format(PWD))

if DEBUG :
    print(" ----- Runtime Variables ---- ")
    print("PWD: {}".format(PWD))
    print("DOWNLOADS_DIR: {}".format(DOWNLOADS_DIR))
    print("CHROME_DRIVER: {}".format(CHROME_EXEC_PATH))
    print(" ----- END / Runtime Variables ---- ")

display = SmartDisplay(visible=0, size=(1080, 1920))
display.start()

options = webdriver.ChromeOptions()

options.add_argument('--no-sandbox')

# In case you're going to download something 
# Configuration is already done 
# Download path is : DOWNLOADS_DIR
options.add_experimental_option("prefs", {
  "download.default_directory": DOWNLOADS_DIR,
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})

# Clean & Create DOWNLOADS_DIR on each run
try:
    shutil.rmtree(DOWNLOADS_DIR)
except OSError as er:
    pass
try:
    os.mkdir(DOWNLOADS_DIR) 
except OSError as er:
    if er.errno != os.errno.EEXIST:
        raise   
    pass

# Examples of variables you can define
URL = os.getenv("URL","https://google.com")
LOGIN = os.getenv("LOGIN", "LOGIN")
PASSWORD = os.getenv("PASSWORD", "PASSWORD")

driver = webdriver.Chrome(executable_path=CHROME_EXEC_PATH, chrome_options=options)
# driver.set_window_size(1080, 1920)

executionPlan = ExecutionPlan(browser=driver, display=display, login=LOGIN, password=PASSWORD)
executionPlan.run(URL)
