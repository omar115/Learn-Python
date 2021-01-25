from selenium import webdriver
from joblib import Parallel, delayed
from PIL import Image
import os


def take_screenshot(url):
    driver = webdriver.Chrome()
    driver.get(url)
    ss = driver.get_screenshot_as_base64()
    # ss = driver.find_element_by_xpath('/html/body/div[2]/div[4]/span[1]/center/div[1]/img').screenshot('abc.png')
    
    driver.close()
    # return ss

def login(url):
    driver = webdriver.Chrome()
    driver.get(url)
    # driver.close()
    

urls = ['https://www.echsbpa.utiitsl.com/ECHS/','https://provider.ihx.in/#/']
# take_screenshot(url)
Parallel(n_jobs=1, prefer="threads")(delayed(login)(url) for url in urls)