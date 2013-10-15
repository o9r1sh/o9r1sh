#VideoPhile addon by o9r1sh

import urllib,urllib2,re,xbmcplugin,xbmcgui,sys,xbmc,urlresolver,xbmcaddon
from resources.modules import main,mooviemaniac,wsoeu,youtube,nmvl,fma,zmovie,wwmf,videocloud

addon_id = 'plugin.video.videophile'
from t0mm0.common.addon import Addon
addon = Addon(addon_id, sys.argv)

mode = addon.queries['mode']
url = addon.queries.get('url', '')
name = addon.queries.get('name', '')
thumb = addon.queries.get('thumb', '')
year = addon.queries.get('year', '')
season = addon.queries.get('season', '')
episode = addon.queries.get('episode', '')
show = addon.queries.get('show', '')
types = addon.queries.get('types', '')

settings = xbmcaddon.Addon(id='<plugin.video.videophile>')
artwork = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.videophile/resources/artwork/', ''))

def CATEGORIES():
        if settings.getSetting('movies') == 'true':
                main.addDir('Movies','none',1,artwork + 'movie.png')
        #main.addDir('HD Movies','none',4,artwork + 'hdmovie.png')
        if settings.getSetting('shows') == 'true':        
                main.addDir('TV Shows','none',2,artwork + 'tv.png')
        if settings.getSetting('docs') == 'true':
                main.addDir('Documentaries','none',3,artwork + 'docs.png')
        if settings.getSetting('search') == 'true':
                main.addDir('VideoPhile Searchs','none',5,artwork + 'search.png')
        if settings.getSetting('resolver') == 'true':
                main.addDir('Resolver Settings','none',8,artwork + 'resolver.png')
        
def MOVIESECTIONS():
        if settings.getSetting('mooviemaniac') == 'true':
                main.addDir('MoovieManiac','none',10,artwork + 'mmaniac.png')
        if settings.getSetting('newmyvideolinks') == 'true':
                main.addDir('NewMyVideoLinks','none',17,artwork + 'nmvl.png')
        if settings.getSetting('freemoviesaddict') == 'true':
                main.addDir('FreeMoviesAddict','none',22,artwork + 'fma.png')
        if settings.getSetting('zmovie') == 'true':
                main.addDir('Watch-Movies / Z-Movie','none',35,artwork + 'zmovie.png')
        if settings.getSetting('wwmf') == 'true':
                main.addDir('WeWatchMoviesFree','none',38,artwork + 'wwmf.png')
        if settings.getSetting('videocloud') == 'true':
                main.addDir('VideoCloud','none',48,artwork + 'videocloud.png')

def HDMOVIESECTIONS():
        if settings.getSetting('newmyvideolinks') == 'true':
                main.addDir('NewMyVideoLinks','none',17,artwork + 'nmvl.png')
        
def TVSECTIONS():
        if settings.getSetting('wsoeu') == 'true':
                main.addDir('WatchSeries-Online','none',11,artwork + 'wso.png')
        if settings.getSetting('newmyvideolinks') == 'true':
                main.addDir('NewMyVideoLinks','none',20,artwork + 'nmvl.png')

def DOCSECTIONS():
        if settings.getSetting('youtubedocs') == 'true':
                main.addDir('National Geographic Documentaries','http://www.youtube.com/results?search_query=national+geographic&oq=national+geographic&gs_l=youtube.3..35i39l2j0l8.1350.5331.0.5427.19.19.0.0.0.0.106.1194.17j2.19.0...0.0...1ac.1.11.youtube._BEl_uoU7Bk',16,artwork + 'natgeo.png')
                main.addDir('BBC Documentaries','http://www.youtube.com/results?search_query=bbc&oq=bbc&gs_l=youtube.3..0l7j0i3j0l2.11848138.11848424.0.11848594.3.3.0.0.0.0.116.301.1j2.3.0...0.0...1ac.1.11.youtube.de569af2UXE',16,artwork + 'bbc.png')
                main.addDir('History Channel Documentaries','http://www.youtube.com/results?search_query=history+channel+documentary&oq=history+&gs_l=youtube.1.0.0l10.24739.26444.0.29034.8.6.0.2.2.0.121.583.5j1.6.0...0.0...1ac.1.11.youtube.9fDvAjIM7ug',16,artwork + 'history.png')
                main.addDir('Discovery Channel Documentaries','http://www.youtube.com/results?search_query=discovery+channel+documentary&oq=discovery+channel+documentary&gs_l=youtube.3..0l10.243928.245622.0.246576.10.10.0.0.0.0.110.743.9j1.10.0...0.0...1ac.1.11.youtube.oK45qI8tlys',16,artwork + 'discovery.png')

def MASTERSEARCH():
        if settings.getSetting('wsoeu') == 'true':
                main.addDir('WatchSeries-Online','none',15,artwork + 'wso.png')
        if settings.getSetting('newmyvideolinks') == 'true':
                main.addDir('NewMyVideoLinks','none',21,artwork + 'nmvl.png')
        if settings.getSetting('wwmf') == 'true':
                main.addDir('WeWatchMoviesFree','none',42,artwork + 'wwmf.png')
                      
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param
          
params=get_params()
url=None
name=None
mode=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

#Default modes__________________________________________________________________
if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()
       
elif mode==1:
        print ""+url
        MOVIESECTIONS()

elif mode==2:
        print ""+url
        TVSECTIONS()

elif mode==3:
        print ""+url
        DOCSECTIONS()

elif mode==4:
        print ""+url
        HDMOVIESECTIONS()

elif mode==5:
        print ""+url
        MASTERSEARCH()

elif mode==8:
        print ""+url
        urlresolver.display_settings()
#Main modes_____________________________________________________________________
elif mode==9:
        print ""+url
        main.RESOLVE(name,url,thumb)
#MoovieManic modes______________________________________________________________
elif mode==10:
        print ""+url
        mooviemaniac.CATEGORIES()

elif mode==47:
        print ""+url
        mooviemaniac.INDEX(url)
#WatchSeries-Online modes_______________________________________________________
elif mode==11:
        print ""+url
        wsoeu.CATEGORIES()

elif mode==12:
        print ""+url
        wsoeu.INDEXSHOWS(url)

elif mode==13:
        print ""+url
        wsoeu.INDEXEPS(url,name)

elif mode==14:
        print ""+url
        wsoeu.VIDEOLINKS(url,name,thumb)

elif mode==15:
        print ""+url
        wsoeu.SEARCH()

elif mode==44:
        print ""+url
        wsoeu.LETTERS()

elif mode==45:
        print ""+url
        wsoeu.SEARCHINDEX(url)

elif mode==46:
        print ""+url
        wsoeu.RECENTEPS(url)
#Youtube documentaries modes____________________________________________________
elif mode==16:
        print ""+url
        youtube.INDEX(url)
#NewMyVideoLinks modes__________________________________________________________
elif mode==17:
        print ""+url
        nmvl.CATEGORIES()

elif mode==18:
        print ""+url
        nmvl.INDEX(url)
        
elif mode==19:
        print ""+url
        nmvl.VIDEOLINKS(name,url,thumb,year)

elif mode==20:
        print ""+url
        nmvl.TVCATEGORIES()

elif mode==21:
        print ""+url
        nmvl.SEARCH()
#Free Movies Addict modes_______________________________________________________
elif mode==22:
        print ""+url
        fma.CATEGORIES()

elif mode==26:
        print ""+url
        fma.INDEX(url)

elif mode==27:
        print ""+url
        fma.VIDEOLINKS(name,url,thumb)

elif mode==28:
        print ""+url
        fma.GENRES()

elif mode==29:
        print ""+url
        fma.YEARS()

elif mode==30:
        print ""+url
        fma.LETTERS()
#Z-Movie modes__________________________________________________________________
elif mode==32:
        print ""+url
        zmovie.INDEX(url)

elif mode==33:
        print ""+url
        zmovie.LETTERS()

elif mode==34:
        print ""+url
        zmovie.GENRES()

elif mode==35:
        print ""+url
        zmovie.CATEGORIES()

elif mode==36:
        print ""+url
        zmovie.VIDEOLINKS(name,url,thumb)
#We Watch Movies Free___________________________________________________________
elif mode==38:
        print ""+url
        wwmf.CATEGORIES()
        
elif mode==39:
        print ""+url
        wwmf.INDEX(url)

elif mode==40:
        print ""+url
        wwmf.LETTERS()

elif mode==41:
        print ""+url
        wwmf.GENRES()

elif mode==42:
        print ""+url
        wwmf.SEARCH()

elif mode==43:
        print ""+url
        wwmf.VIDEOLINKS(name,url,thumb)
#Videocloud modes_______________________________________________________________
elif mode==48:
        print ""+url
        videocloud.CATEGORIES()

elif mode==49:
        print ""+url
        videocloud.INDEX(url)
        
xbmcplugin.endOfDirectory(int(sys.argv[1]))
