# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 17:04:23 2019

@author: AvantikaDG
"""

from bs4 import BeautifulSoup

categories = ["gaming_sites", "porn_sites", "kids_sites", "recreation_sites", "shopping_sites", "sports_sites"]
sites = []
extras = ['facebook.com', 'twitter.com', 'instagram.com', 'reddit.com', '9gag.com', '4chan.com']

for category in categories:
    file = open("Sites/"+category+".txt", "r")
    contents = file.read()
    file.close()
    soup = BeautifulSoup(contents, "html.parser")
    for link in soup.find_all("a"):
        s = link.get("href")
        if s is not None and r"/siteinfo/" in s:
            sites.append(s[10:])
sites.extend(extras)
file = open("sites.txt","w") 
file.write(str(sites)) 
file.close()

        
