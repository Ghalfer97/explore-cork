import requests
import random
import pandas as pd
import os
import csv
import numpy as np
import time
from bs4 import BeautifulSoup
from shapely.geometry import Point
#import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#x=https://www.google.com/maps/place/The+Shelbourne+Bar/@51.8970925,-8.4844752,14z/data=!4m10!1m2!2m1!1spubs+cork!3m6!1s0x4844900e60fdd20f:0x54cfdd2b85a16f78!8m2!3d51.9014208!4d-8.4683764!15sCglwdWJzIGNvcmtaCyIJcHVicyBjb3JrkgEJaXJpc2hfcHVimgEkQ2hkRFNVaE5NRzluUzBWSlEwRm5TVVJETm5CMlozRlJSUkFC4AEA!16s%2Fg%2F1s04cl7x3?entry=ttu
#search_area="https://www.google.com/maps/search/pubs/@{51.8990771},{-8.4725976},16.91z"
#search_area="https://www.google.com/maps/search/restaurants+in+cork"
#response=requests.get(search_area)
#html_content=response.text
#soup=BeautifulSoup(html_content,"html.parser")
#pubs=soup.find_all("div",class_="section-result-details-container")

results=set()
delay = 10
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('start-maximized')
chrome_options.add_argument('disable-infobars')
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.optanon-allow-all.accept-cookies-button"))).click()
#exit()

if 1==1:
    #@51.8945394,-8.4942599,
    list_of_possible_keywords=['cocktail','bars','pubs','gastropubs'] #'restaurant'
    i=0
    for z in range(1,5):
        x=random.uniform(51.84,51.9)
        y=random.uniform(-8.44,-8.5)
        for i in range(0,4):
            search_area=f"https://www.google.com/maps/search/{list_of_possible_keywords[i]}+cork/@{x},{y},14z/data=!4m2!2m1!6e5?entry=ttu"
            i+=1
            #print(i)
            driver.get(search_area)
            time.sleep(10)
            message = driver.find_elements(by=By.CSS_SELECTOR, value="div")
            #message = driver.find_elements(by=By.CSS_SELECTOR, value="button") #Found The Shelbourne bar
            #for a_message in message:
            #	print (a_message.text) #Found address of shelbourne, style of pub, delivery,etc
            #message[200].find_element(By.CSS_SELECTOR, "div.fontHeadlineSmall").text #Found shelbourne bar

            #driver.close()
            index_number=0
            for a_message in message:
                try:
                    pub_name=a_message.find_element(By.CSS_SELECTOR, "div.fontHeadlineSmall")
                    results.add(str(pub_name.text))
                    #print(pub_name.text,index_number)
                    index_number+=1
                    avg_rating = a_message.find_element(By.CLASS_NAME,"section-star-display")
                    total_reviews = a_message.find_element(By.CLASS_NAME,"section-rating-term")
                    address = a_message.find_element(By.CSS_SELECTOR,"[data-item-id='address']")
                    phone_number = a_message.find_element(By.CSS_SELECTOR,"[data-tooltip='Copy phone number']")
                    website = a_message.find_element(By.CSS_SELECTOR,"[data-item-id='authority']")
                except:
                    pass
                #try:
                #    results.add(str(pub_name.text))#+';'+str(avg_rating.text))
                #    print(pub_name.text,index_number)
                #except:
                #    pass
    

    madelyns_pubs = ['Sin é','The Corner House','Mutton Lane Inn',"Arthur Mayne's Pharmacy","Fionnbarra","The Long Valley Bar","The Raven Bar","Vicarstown Bar","The Friary","BarBarossa OliverPlunkett Street",
                     "Barbarella","Tom Barry's","Mr Bradley's","The Abbey Tavern","The Pav","Crack Jenny's","Paddy the Farmers","Coughlans Bar","Crane Lane","An Bróg Bar + Kitchen","Brick Lane",
                     "Conway's Yard","Abbott's Ale House","Maureen's","The Shelbourne Bar","The Oliver Plunkett","Fred Zeppelins","Old Oak","Clancy's Cork","The Oval","The Park","Spailpin Fanach",
                     "O'Sho","Rearden's Bar","Dwyers of Cork","Costigan's Pub","The Courtyard on Sober Lane","Rosie Maddison's","The Roundy","Deep South","Perch - Rooftop at SoHo","Gaia",
                     "Impala","Chambers","The Welcome Inn","The Poor Relation","Cask","The Mardyke Entertainment Complex","Fordes Bar","The Beer Garden","The Woodford","Franciscan Well Brewery & Brewpub",
                     "The Hyde Out","Bru Bar","Paladar","Rising Sons Brewery","The Rob Roy","Gables","Cissie Youngs","Annie Mac's","Bierhaus","An Sibín","Upstairs"]
    fearghals_pubs=['Sin é','The Corner House','Mutton Lane Inn',"Arthur Mayne's Pharmacy","Fionnbarra","The Long Valley Bar","The Raven Bar","Vicarstown Bar","The Friary","BarBarossa OliverPlunkett Street",
                    "Barbarella","Tom Barry's","Mr Bradley's","The Pav","Crack Jenny's","Coughlans Bar","Crane Lane","An Bróg Bar + Kitchen","Conway's Yard","Abbott's Ale House",
                    "The Shelbourne Bar","The Oliver Plunkett","Fred Zeppelins","Old Oak","Clancy's Cork","The Oval","Spailpin Fanach","O'Sho","Rearden's Bar","Dwyers of Cork","Costigan's Pub",
                    "The Courtyard on Sober Lane","Rosie Maddison's","The Roundy","Deep South","Perch - Rooftop at SoHo","Gaia","Impala","Chambers","The Welcome Inn","The Poor Relation","Cask",
                    "The Mardyke Entertainment Complex","Fordes Bar","The Beer Garden","The Woodford","Franciscan Well Brewery & Brewpub","The Hyde Out","Paladar","Rising Sons Brewery","The Rob Roy","Gables",
                    "Cissie Youngs","Annie Mac's","Bierhaus","The Hi-B Bar","An Sibín","Ryan's Bar","Canty's Bar","Barcadia Video Arcade","Upstairs"]
    rows=[]
    rows.extend(results)
    pubs_df=pd.DataFrame({'Pub_Name':rows})
    pubs_df.to_csv("output_files/test_pubs_in_cork.csv",index=False)
