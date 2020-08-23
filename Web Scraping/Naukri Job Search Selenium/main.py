import os
import time
from selenium import webdriver
import pandas as pd
import matplotlib.pyplot as plt

driver = webdriver.Chrome(r"D:/chromedriver.exe")
"""
jobs = {
    "roles" : ['Data Scientist', 'Data Engineer', 'ETL Developer', 'Machine Learning Engineer', 'AI Engineer', 'Spark Developer'],
    "title_contains" : [
                        'Data Science', 'ETL', 'Machine Learning', 'ML', 'Deep Learning', 'DL', 'AI', 'Artificial Intelligence', 
                        'Data Hub', 'DataHub', 'InfoCenter', 'Info Center', 'DH&IC', 'DH-IC'
    ],
    "locations" : [],
    "experience" : [],
    "skills" : [
                'Python', 'Spark', 'PySpark', 'Informatica', 'SAP BODS', 'SAP Data Services', 'Tensorflow', 
                'Tensor Flow', 'PyTorch', 'Py Torch', 'GCP', 'Google Cloud Platform', 'Amazon Web Services', 
                'AWS', 'Data Science'
    ]
}
"""

search_skills = [
    'Python', 'Spark', 'PySpark', 'Informatica', 'SAP BODS', 'SAP Data Services', 'Tensorflow', 
    'Tensor Flow', 'PyTorch', 'Py Torch', 'GCP', 'Google Cloud Platform', 'Amazon Web Services', 
    'AWS', 'Data Science'
]

for skill in search_skills : 
    driver.get("https://www.naukri.com/top-skill-jobs")
    time.sleep(5)
    inp = driver.find_element_by_class_name('sugInp')
    inp.send_keys('Data Scientist')
    loc = driver.find_element_by_class_name('sugInp.w135')
    search = driver.find_element_by_class_name('qsbSrch.blueBtn')
    search.click()
    time.sleep(5)
    details = []
    curr_page = 0
    while True : 
        pages = driver.find_element_by_class_name('fleft.pages')
        pages = pages.find_elements_by_tag_name('a')
        total_pages = len(pages)
        if curr_page >= total_pages : 
            break
        page = pages[curr_page]
        href = page.get_attribute('href')
        driver.get(href)
        time.sleep(5)
        lst = driver.find_elements_by_class_name('jobTuple.bgWhite.br4.mb-8')
        #print(len(lst))
        for item in lst : 
            title = item.find_element_by_class_name('title.fw500.ellipsis').text
            company = item.find_element_by_class_name('subTitle.ellipsis.fleft').text
            try : 
                rating = item.find_element_by_class_name('starRating.fleft.dot').text
            except : 
                rating = 'N/A'
            exp_n_sal = item.find_elements_by_class_name('ellipsis.fleft.fs12.lh16')
            desc = item.find_element_by_class_name('fleft.icon-16.lh16.mr-4.naukicon.naukicon-desc').text
            skills = item.find_elements_by_class_name('fleft.fs12.grey-text.lh16.dot')
            #print(title, company, rating,[i.text for i in exp_n_sal], desc, [i.text for i in skills], sep = '\n')
            details.append([title, company, rating,[i.text for i in exp_n_sal], desc, [i.text for i in skills]])
            #print('\n')

        curr_page += 1

    details_df = pd.DataFrame(details)
    #print(details_df.head())
    details_df.to_csv(f"{skill}.csv", index = False)

