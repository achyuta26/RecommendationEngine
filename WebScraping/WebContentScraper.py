#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 21:32:03 2017

@author: Achyuta
"""
import urllib2
import pandas as pd
from bs4 import BeautifulSoup
from google import search



webContentDF = pd.DataFrame(columns=['Category','URL','Title','Content'])
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

def scrape_webpage_body(url):
    req = urllib2.Request(url, headers=hdr)
    try:
        content = urllib2.urlopen(req)
        soup = BeautifulSoup(content,'html.parser')
        return soup
    except (urllib2.HTTPError,Exception):
        return '' 


def getRelevantTextFromPage(soup):
    blockOfText=""    
    blockOfTextFromWebPage = soup.find_all('p')
    for text in blockOfTextFromWebPage:
        blockOfText = blockOfText+"\n\n"+text.getText()  
    return blockOfText    

categories = ['text analytics','food blogs','apache spark','world tour','machine learning',
         'delicious recipies','deep learning','amazing gadgets','artificial intelligence','verge','macbook','music festivals around the world',
         'tomorrowland','david guetta','McDonalds burgers']
count=0
for category in categories:
  for url in search(category,stop=100):
        fullContent = scrape_webpage_body(url)
        if(len(fullContent)!=0):
            try:
                relevantContent = getRelevantTextFromPage(fullContent)
                title = fullContent.title.text
                webContentDF.loc[count]=[category,url,str(title),relevantContent]
                count = count+1
                print count
            except Exception:
                print"Could not fetch content from:\t",url
                
webContentDF.sample(frac=1)     # Random shuffling of rows
webContentDF.to_csv('/DataScraping/TextDataFromWeb.csv',encoding="utf-8")    
    


    
  
