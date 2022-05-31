import bs4 as Beautifulsoup
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import csv


##### Access Site #####

#-----Set Up Driver-----
driver_path = 'C:\\Users\jbean\Downloads\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path = driver_path)


#-----Get URL Function-----
def get_url(url,title,location):

    driver.get(url)
    driver.find_element_by_xpath('//*[@id="text-input-what"]').send_keys(title)
    driver.find_element_by_xpath('//*[@id="text-input-where"]').send_keys(Keys.CONTROL + "a")
    driver.find_element_by_xpath('//*[@id="text-input-where"]').send_keys(location)
    driver.find_element_by_xpath('//*[@id="jobsearch"]/button').click()
    current_url = driver.current_url

    return current_url


##### Collect Job Data #####


#-----Get Data Function-----
def get_data(url):

    jobs_data = []
    job_card_list = driver.find_elements(By.CLASS_NAME, 'job_seen_beacon')
    page_list = driver.find_elements_by_class_name('pagination-list')
    for job in job_card_list:

        job.click()
        WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "vjs-container-iframe")))
        jobs_dict = {
        "title" : driver.find_element_by_class_name('jobsearch-JobInfoHeader-title-container').text.strip("- job post").rstrip(),
        "company" : driver.find_element_by_xpath('//*[@id="viewJobSSRRoot"]/div[1]/div[1]/div/div/div/div[1]/div/div[1]/div[1]/div[1]/div[2]/div/div/div/div[1]/div[2]/div').text.strip(""),
        "location" : driver.find_element_by_xpath('//*[@id="viewJobSSRRoot"]/div[1]/div[1]/div/div/div/div[1]/div/div[1]/div[1]/div[1]/div[2]/div/div/div/div[2]').text,
        "job_desc" : driver.find_element_by_id("jobDescriptionText").text.replace('\n', ' '),
        }
        try:
            salary = driver.find_element_by_xpath('//*[@id="jobDetailsSection"]/div[2]/span').text.strip(" a year").strip()
            jobs_dict["salary"] = salary
        except:
            jobs_dict["salary"] = ''
        jobs_data.append(jobs_dict)
        driver.switch_to.parent_frame()
    
    df = pd.DataFrame(jobs_data)
    return len(page_list)


#-----Call Functions-----
EL_geology = get_url('https://www.indeed.com/','Entry Level Geologist','Anywhere')
EL_geology_data = get_data(EL_geology)
print(EL_geology_data)


EL_data_analysis = get_url('https://www.indeed.com/', 'Entry Level Data Analyst','Anywhere')
EL_data_analysis_data = get_data(EL_data_analysis)


#####Export Data#####


#-----Export-----
EL_geology_data.to_csv(r'C:\Users\jbean\OneDrive\Desktop\Job Scraper\EL_geology_df.csv')
EL_data_analysis_data.to_csv(r'C:\Users\jbean\OneDrive\Desktop\Job Scraper\EL_DA_df.csv')
