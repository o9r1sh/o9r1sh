#NewMyVideoLinks Module by o9r1sh September 2013

import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmcaddon,sys,main,xbmc,os
import urlresolver

artwork = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.videophile/resources/artwork/', ''))

base_url = 'http://www.myvideolinks.eu'

def CATEGORIES():
        main.addDir('Yify Movies',base_url + '/category/movies/yify/','newMyVideoLinksIndex',artwork + '/main/yify.png')
        main.addDir('Recent Movies',base_url + '/category/movies/','newMyVideoLinksIndex',artwork + '/main/recentlyadded.png')
        main.addDir('Search','none','newMyVideoLinksSearch',artwork + '/main/search.png')

def HDMOVIES():
        INDEX(base_url + '/category/movies/yify/')


def TVCATEGORIES():
        main.addDir('Recent Episodes',base_url + '/category/tv-shows/','newMyVideoLinksIndex',artwork + '/main/recentlyadded.png')
        main.addDir('Search','none','newMyVideoLinksSearch',artwork + '/main/search.png')
        
def INDEX(url):
        types = None
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('<a href="(.+?)" rel="bookmark" title=".+?">(.+?)</a>').findall(link)
        np=re.compile("<span class='pages'>Page (.+?)</span>").findall(link)
        if len(np) > 0:
                numbers = np[0]
                head,sep,tail = numbers.partition('of')
                current_page = int(head)
                last_page = int(tail)
                nex = current_page + 1
                if nex < last_page:
                        if current_page == 1:
                                next_page = url + '/page/' + str(nex)
                        else:
                                a,b,c = url.partition('/page/')
                                next_page = url + a + b + str(nex)
                        main.addDir('Next Page',next_page,'newMyVideoLinksIndex',artwork + '/main/next.png')

        for url,name in match:
                if '<img src=' in name:
                        continue
                else:
                        show = re.split('[Ss]\d\d[Ee]\d\d',name)
                        
                        if len(show) == 2:
                                types = 'episode'
                        else:
                                types = 'movie'

                        if types == 'episode':
                                try:        
                                        main.addEDir(name,url,'newMyVideoLinksVideoLinks','',show[0])
                                except:
                                        continue
                                
                        if types == 'movie':
                                split = re.split('(\d\d\d\d)',name)
                                year =  str(split[1])
                                try:        
                                        main.addMDir(name,url,'newMyVideoLinksVideoLinks','',year,False)      
                                except:
                                        continue
        if types == 'episode':
                main.AUTOVIEW('episodes')
        else:
                main.AUTOVIEW('movies')

def VIDEOLINKS(name,url,thumb,year):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('<li><a href="(.+?)">.+?</a></li>').findall(link)
        for url in match:
                if len(match) > 0:
                                hmf = urlresolver.HostedMediaFile(url)
                                if hmf:
                                        host = hmf.get_host()
                                        hthumb = main.GETHOSTTHUMB(host)
                                        main.addHDir(name,url,'resolve',thumb,hthumb)

def SEARCH():
        search = ''
        keyboard = xbmc.Keyboard(search,'Search')
        keyboard.doModal()
        if keyboard.isConfirmed():
                search = keyboard.getText()
                search = search.replace(' ','+')
                
                url = base_url + '/index.php?s=' + search
                INDEX(url)


def MASTERSEARCH(search):
                url = base_url + '/index.php?s=' + search
                INDEX(url)
