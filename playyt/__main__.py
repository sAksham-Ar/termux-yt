import requests
from bs4 import BeautifulSoup
import re
import os
import sys
def playyt():
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
    files = [f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), f))]
    search_term=sys.argv[1]
    for file in files:
        if search_term.lower() in file.lower():
            cmd="termux-media-player play '"+file+"'"
            os.system(cmd)
            exit()
    title,link=getvideos(search_term)
    cmd="youtube-dl --add-metadata --audio-format mp3 -x -o '%(title)s.%(ext)s' "+link
    os.system(cmd)
    cmd="termux-media-player play '"+title+".mp3'"
    os.system(cmd)
if __name__ == "__main__":
    playyt()