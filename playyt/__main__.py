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
        while 1:
            os.system('clear')
            files = [f for f in os.listdir(os.getcwd()+'/songs') ]
            i=0
            for file in files:
                print("{:<3} {:<50}".format(str(i+1),file))
                i+=1
            print('-'*100)
            os.system('termux-media-player info')
            print('-'*100)
            print("song_number:song to play,q:quit,d:download,p:pause,r:resume,n:next,pr:previous")
            choice=input()
            if choice=='n':
                os.system('termux-media-player stop')
                current=min(current+1,len(files))
                choice=current
            elif choice =='pr':
                os.system('termux-media-player stop')
                current=max(current-1,1)
                choice=current
            if choice=='q':
                os.system('clear')
                exit()
            elif choice=='d':
                os.system('clear')
                print("Enter the name of the song:")
                search_term=input()
                title,link=getvideos(search_term)
                cmd="youtube-dl --add-metadata --audio-format mp3 -x -o '%(title)s.%(ext)s' "+link
                os.system(cmd)
            elif choice=='p':
                os.system('termux-media-player stop')
                cmd="termx-media-player pause"
                os.system(cmd)
            elif choice=='r':
                cmd="termx-media-player resume"
                os.system(cmd)
            else:
                title=files[int(choice)-1]
                current=int(choice)
                cmd="termux-media-player play 'songs/"+title+"'"
                os.system(cmd)
    interface()
    

if __name__ == "__main__":
    playyt()