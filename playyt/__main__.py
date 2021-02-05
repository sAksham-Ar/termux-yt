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
    def interface():
        os.system('cd songs')
        os.system('clear')
        while 1:
            files = [f for f in os.listdir(os.getcwd()+'/songs') if os.path.isfile(os.path.join(os.getcwd(), f))]
            i=0
            print(files)
            for file in files:
                print("{:<3} {:<50}".format(str(i+1),file))
                i+=1
            print("song_number:song to play,q:quit,d:download")
            choice=input()
            if choice=='q':
                os.system('clear')
                exit()
            elif choice=='d':
                print("Enter the name of the song:")
                search_term=input()
                title,link=getvideos(search_term)
                cmd="youtube-dl --add-metadata --audio-format mp3 -x -o '%(title)s.%(ext)s' "+link
                os.system(cmd)
            else:
                title=files[choice-1]
                cmd="termux-media-player play '"+title
    interface()
    

if __name__ == "__main__":
    playyt()