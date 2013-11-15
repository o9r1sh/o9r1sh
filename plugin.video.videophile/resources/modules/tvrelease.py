#TV Release Module by o9r1sh September 2013
import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmcaddon,sys,main,xbmc,os
import urlresolver

from t0mm0.common.net import Net
net = Net()

artwork = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.videophile/resources/artwork/', ''))
base_url = 'http://tv-release.net'
settings = main.settings

def TV_CATEGORIES():
        main.addDir('XVID Episodes',base_url + '/category/tvshows/tvxvid/','tvreleaseIndex',artwork + '/main/xvidtv.png')
        main.addDir('MP4 Episodes',base_url + '/category/tvshows/tvmp4/','tvreleaseIndex',artwork + '/main/mp4tv.png')
        main.addDir('480P Episodes',base_url + '/category/tvshows/tv480p','tvreleaseIndex',artwork + '/main/sdtv.png')
        main.addDir('720P Episodes',base_url + '/category/tvshows/tv720p/','tvreleaseIndex',artwork + '/main/hdtv.png')
        main.addDir('Foreign Episodes',base_url + '/category/tvshows/tv-foreign','tvreleaseIndex',artwork + '/main/foreign.png')
        main.addDir('Search',base_url + 'none','tvreleaseSearch',artwork + '/main/search.png')

def HDMOVIES():
        INDEX(base_url + '/category/movies/movies720p')

        
def MOVIE_CATEGORIES():
        main.addDir('XVID Movies',base_url + '/category/movies/moviesxvid','tvreleaseIndex',artwork + '/main/xvidmovies.png')
        main.addDir('480P Movies',base_url + '/category/movies/movies480p','tvreleaseIndex',artwork + '/main/sdmovies.png')
        main.addDir('720P Movies',base_url + '/category/movies/movies720p','tvreleaseIndex',artwork + '/main/hdmovies.png')
        main.addDir('DVD-R Movies',base_url + '/category/movies/moviesdvdr','tvreleaseIndex',artwork + '/main/dvdrmovies.png')
        main.addDir('Foreign Movies',base_url + '/category/movies/moviesforeign','tvreleaseIndex',artwork + '/main/foreign.png')
        
def INDEX(url):
        np_url = ''
        types = None
        link = net.http_GET(url).content
        match=re.compile('a href="(.+?)"><b><font size=".+?">(.+?)</font></b></a>').findall(link)
        np=re.compile("<span class='zmg_pn_current'>(.+?)</span>").findall(link)
        np_url = None
        cur_page = None
        if len(np) > 0:
                cur_page = np[0]
                cur_page = int(cur_page)
                next_page = int(cur_page) + 1
                if cur_page == 1:
                        np_url = url + '/page/' + str(next_page)

                else:
                        head,sep,tail = url.partition('/page/')
                        np_url = head + sep + str(next_page)

                if '&cat' in url:
                                head,sep,tail = url.partition('?s')
                                np_url = base_url + '/page/' + str(next_page) +'/' + sep + tail

                
                if settings.getSetting('nextpagetop') == 'true':       
                        main.addDir('[COLOR blue]Next Page[/COLOR]',np_url,'tvreleaseIndex',artwork + '/main/next.png')

        for url,name in match:
                try:
                        if 'Filech' in name:
                                continue
                        else:
                                show = re.split('[Ss]\d\d[Ee]\d\d',name)
                
                                if len(show) == 2:
                                        types = 'episode'
                                else:
                                        types = 'movie'

                                if types == 'episode':
                                        try:        
                                                main.addEDir(name,url,'tvreleaseVideoLinks','',show[0])
                                        except:
                                                continue
                        
                                if types == 'movie':
                                        try:        
                                                main.addMDir(name,url,'tvreleaseVideoLinks','','',False)      
                                        except:
                                                continue
                except:
                        continue
        if types == 'episode':
                main.AUTOVIEW('episodes')
        else:
                main.AUTOVIEW('movies')
        if len(np) > 0:
                if settings.getSetting('nextpagebottom') == 'true':       
                        main.addDir('[COLOR blue]Next Page[/COLOR]',np_url,'tvreleaseIndex',artwork + '/main/next.png')


def VIDEOLINKS(name,url,thumb):
        link = net.http_GET(url).content
        match=re.compile("<a target='_blank' href='(.+?)'>").findall(link)
        for url in match:
                if main.resolvable(url):
                        main.addHDir(name,url,'resolve','')

def SEARCH():
        search = ''
        keyboard = xbmc.Keyboard(search,'Search')
        keyboard.doModal()
        if keyboard.isConfirmed():
                search = keyboard.getText()
                search = search.replace(' ','%20')
                url = base_url + '/?s=' + search + '&cat='
                
                INDEX(url)

def MASTERSEARCH(search):
        url = base_url + '/?s=' + search + '&cat='    
        INDEX(url)

