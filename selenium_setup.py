import time

from selenium import webdriver

"""
    For linux users no need to use executable_path instead of we can change the drive file into executable file.For 
    change browser driver file to executable file please go through the "linux_setup" file. 
"""
driver = webdriver.Chrome()

"""
    For windows users use "executable_path"
"""
# driver = webdriver.Chrome(executable_path = "path(driver path)")

driver.get("https://www.flipkart.com/")  # url path

print(driver.title)  # get webpage title
print(driver.current_url)  # get webpage url

time.sleep(10)  # web open for 10 sec

driver.close()  # close the webpage
