#'' module by o9r1sh

import urllib,urllib2,re,xbmcplugin,xbmcgui,sys,main,urlresolver,xbmc,os

from t0mm0.common.net import Net
net = Net()

artwork = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.videophile/resources/artwork/', ''))
base_url = 'http://fullepisode.info'

def CATEGORIES():
        main.addDir('Recently Added',base_url,'fullEpisodeIndex', artwork + '/main/recentlyadded.png')
        main.addDir('Search','none','fullEpisodeSearch', artwork + '/main/search.png')

def INDEX(url):
        link = net.http_GET(url).content
        match=re.compile('<a href="(.+?)" class="post-info-title" title="Permanent Link to (.+?)">').findall(link)
        np=re.compile("<a href=\'(.+?)' class=\'(.+?)\'>.+?</a>").findall(link)
        for url,name in np:
                if name == 'nextpostslink':
                        main.addDir('Next Page',url,'fullEpisodeIndex',artwork + '/main/next.png')
        for url, name in match:
                head,sep,tail = name.partition('Season')
                show = head
                numbers = tail.replace('Episode','x')
                numbers = numbers.replace(' ','')
                name = show + numbers
                try:
                        main.addEDir(name,url,'fullEpisodeVideoLinks','',show)
                except:
                        continue

        main.AUTOVIEW('episodes')

def VIDEOLINKS(url,name,thumb):
        link = net.http_GET(url).content
        match=re.compile('<a rel="nofollow" target="_blank" href="(.+?)">').findall(link)
        for url in match:
                if main.resolvable(url):
                        hthumb = main.GETHOSTTHUMB(main.getHost(url))
                try:
                        main.addHDir(name,url,'resolve',thumb,hthumb)
                except:
                        continue
       
def SEARCH():
        search = ''
        keyboard = xbmc.Keyboard(search,'Search')
        keyboard.doModal()
        if keyboard.isConfirmed():
                search = keyboard.getText()
                search = search.replace(' ','+')
                
                url = base_url + '/?s=' + search 
                
                INDEX(url)

def MASTERSEARCH(search):
                search = search.replace(' ','+')
                url = base_url + '/?s=' + search
                
                INDEX(url)


                

