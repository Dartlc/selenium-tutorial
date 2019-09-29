"""
    In this tutorial we are going to discuss about webelements.
    normally, webelements are used to locate the elements of the webpage
"""

"""
    To find single locator use the following elements
    
    find_element_by_id
    find_element_by_name
    find_element_by_xpath
    find_element_by_link_text
    find_element_by_partial_link_text
    find_element_by_tag_name
    find_element_by_class_name
    find_element_by_css_selector
    
"""
"""
    To find multiple locators use the following elements
    
    find_elements_by_name
    find_elements_by_xpath
    find_elements_by_link_text
    find_elements_by_partial_link_text
    find_elements_by_tag_name
    find_elements_by_class_name
    find_elements_by_css_selector
"""

import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://facebook.com")

driver.maximize_window()  # maximize the browser window

time.sleep(3)  # browser waiting sec

driver.find_element_by_id("email").send_keys("dartlc@gmail.com")  # find_element_by_id and send values

driver.find_element_by_name("pass").send_keys("hello")  # find_element_by_name and send values

driver.find_element_by_xpath("//input[@aria-label='First name']").send_keys(
    "Dartlc")  # find_element_by_xpath and send values

"""
    link_text and partial_link_text both are similar elements so use any one element 
"""

# driver.find_element_by_link_text("Forgotten account?").click()  # find_element_by_link_text

driver.find_element_by_partial_link_text("Forgo").click()  # find_element_by_partial_link_text

time.sleep(10)

"""
    if the tag name have unique then only "find_element_by_tag_name" will support otherwise it will consider the tags 
    are list.
"""

driver.find_element_by_tag_name("span")  # find_element_by_partial_link_text

driver.find_element_by_class_name("uiButton").click()  # find_element_by_class_name

"""
    if the css selector class value have compound words like("fb_logo img sp_ydUEsVjCbun sx_7e0f83") instead of space
    we are going to use ".". reason is, the webdriver does not recognize space between any values. 
"""
driver.find_element_by_css_selector("i.fb_logo.img.sp_ydUEsVjCbun.sx_7e0f83").click()  # find_element_by_css_selector

time.sleep(10)

driver.minimize_window()  # minimize the browser window

time.sleep(10)

driver.close()  # close the browser
