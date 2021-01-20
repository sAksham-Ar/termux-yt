import requests
from bs4 import BeautifulSoup
import re
import os
import sys
def getvideos(search_term):
    try:
        url="https://invidious.snopyta.org/search?q="+search_term
        r = requests.get(url, stream=True)
        page = BeautifulSoup(r.content, 'html.parser')
    except Exception as e:
        print(str(e))
        return
    results=page.find_all(href=re.compile("/watch?"))
    results= results[1::2]
    links=[result.attrs['href'] for result in results]
    titles=[result.text for result in results]
    youtube_link="https://www.youtube.com"+links[0]
    return titles[0],youtube_link
try:
    files = [f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), f))]
except:
    print("files failed!")
search_term=sys.argv[1]
for file in files:
    if search_term.lower() in file.lower():
         cmd="termux-media-player play "+file
         try:
            os.system(cmd)
         except:
            print("fails at first")
         exit()
title,link=getvideos(search_term)
try:
    cmd="youtube-dl -x -o '%(title)s.%(ext)s' "+link
    os.system(cmd)
except:
    print("fails at second")
try:
    cmd="termux-media-player play '"+title+".opus'"
    os.system(cmd)
except:
    print("fails at third")