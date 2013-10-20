#VideoPhile addon by o9r1sh

import urllib,urllib2,re,xbmcplugin,xbmcgui,sys,xbmc,urlresolver,xbmcaddon
from resources.modules import main,mooviemaniac,wsoeu,youtube,nmvl,fma,zmovie,wwmf,videocloud,iwo,freeomovie,tvrelease

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

text_file = None
if not os.path.exists(xbmc.translatePath("special://home/userdata/addon_data/plugin.video.videophile/")):
        os.makedirs(xbmc.translatePath("special://home/userdata/addon_data/plugin.video.videophile/"))

        if not os.path.exists(xbmc.translatePath("special://home/userdata/addon_data/plugin.video.videophile/sec.0")):
                pin = ''
                notice = xbmcgui.Dialog().ok('Notice','VideoPhile now contains an adult section, for safety reasons','after pressing ok you will be asked to set a password','that will be used to gain access to the adult section')
                keyboard = xbmc.Keyboard(pin,'Please Choose A New Password')
                keyboard.doModal()
                if keyboard.isConfirmed():
                        pin = keyboard.getText()
        text_file = open(xbmc.translatePath("special://home/userdata/addon_data/plugin.video.videophile/sec.0"), "w")
        text_file.write(pin)
        text_file.close()
           
def CATEGORIES():
        if settings.getSetting('adult') == 'true':
                main.addDir('Adults Only','none',6,artwork + '/main/adult.png')
        if settings.getSetting('movies') == 'true':
                main.addDir('Movies','none',1,artwork + '/main/movie.png')
        if settings.getSetting('hdmovies') == 'true':
                main.addDir('HD Movies','none',4,artwork + '/main/hd.png')
        if settings.getSetting('shows') == 'true':        
                main.addDir('TV Shows','none',2,artwork + '/main/tv.png')
        if settings.getSetting('docs') == 'true':
                main.addDir('Documentaries','none',3,artwork + '/main/docs.png')
        if settings.getSetting('search') == 'true':
                main.addDir('VideoPhile Searchs','none',5,artwork + '/main/search.png')
        if settings.getSetting('resolver') == 'true':
                main.addDir('Resolver Settings','none',8,artwork + '/main/resolver.png')
        
def MOVIESECTIONS():
        if settings.getSetting('mooviemaniac') == 'true':
                main.addDir('MoovieManiac','none',10,artwork + '/main/mmaniac.png')
        if settings.getSetting('newmyvideolinks') == 'true':
                main.addDir('NewMyVideoLinks','none',17,artwork + '/main/nmvl.png')
        if settings.getSetting('freemoviesaddict') == 'true':
                main.addDir('FreeMoviesAddict','none',22,artwork + '/main/fma.png')
        if settings.getSetting('zmovie') == 'true':
                main.addDir('Watch-Movies / Z-Movie','none',35,artwork + '/main/zmovie.png')
        if settings.getSetting('wwmf') == 'true':
                main.addDir('WeWatchMoviesFree','none',38,artwork + '/main/wwmf.png')
        if settings.getSetting('videocloud') == 'true':
                main.addDir('VideoCloud','none',48,artwork + '/main/videocloud.png')
        if settings.getSetting('iwatchonline') == 'true':
               main.addDir('I-WatchOnline','none',50,artwork + '/main/iwatchonline.png')
        if settings.getSetting('tvrelease') == 'true':
                main.addDir('TV Release','none',131,artwork + '/main/tvrelease.png')

def HDMOVIESECTIONS():
        if settings.getSetting('newmyvideolinks') == 'true':
                main.addDir('NewMyVideoLinks Yify Movies','none',127,artwork + '/main/nmvl.png')
        if settings.getSetting('tvrelease') == 'true':
                main.addDir('TV Release','none',126,artwork + '/main/tvrelease.png')
        
def TVSECTIONS():
        if settings.getSetting('wsoeu') == 'true':
                main.addDir('WatchSeries-Online','none',11,artwork + '/main/wso.png')
        if settings.getSetting('newmyvideolinks') == 'true':
                main.addDir('NewMyVideoLinks','none',20,artwork + '/main/nmvl.png')
        if settings.getSetting('tvrelease') == 'true':
                main.addDir('TV Release','none',132,artwork + '/main/tvrelease.png')

def DOCSECTIONS():
        if settings.getSetting('youtubedocs') == 'true':
                main.addDir('National Geographic Documentaries','http://www.youtube.com/results?search_query=national+geographic&oq=national+geographic&gs_l=youtube.3..35i39l2j0l8.1350.5331.0.5427.19.19.0.0.0.0.106.1194.17j2.19.0...0.0...1ac.1.11.youtube._BEl_uoU7Bk',16,artwork + '/main/natgeo.png')
                main.addDir('BBC Documentaries','http://www.youtube.com/results?search_query=bbc&oq=bbc&gs_l=youtube.3..0l7j0i3j0l2.11848138.11848424.0.11848594.3.3.0.0.0.0.116.301.1j2.3.0...0.0...1ac.1.11.youtube.de569af2UXE',16,artwork + '/main/bbc.png')
                main.addDir('History Channel Documentaries','http://www.youtube.com/results?search_query=history+channel+documentary&oq=history+&gs_l=youtube.1.0.0l10.24739.26444.0.29034.8.6.0.2.2.0.121.583.5j1.6.0...0.0...1ac.1.11.youtube.9fDvAjIM7ug',16,artwork + '/main/history.png')
                main.addDir('Discovery Channel Documentaries','http://www.youtube.com/results?search_query=discovery+channel+documentary&oq=discovery+channel+documentary&gs_l=youtube.3..0l10.243928.245622.0.246576.10.10.0.0.0.0.110.743.9j1.10.0...0.0...1ac.1.11.youtube.oK45qI8tlys',16,artwork + '/main/discovery.png')

def MASTERSEARCH():
        if settings.getSetting('wsoeu') == 'true':
                main.addDir('WatchSeries-Online','none',15,artwork + '/main/wso.png')
        if settings.getSetting('newmyvideolinks') == 'true':
                main.addDir('NewMyVideoLinks','none',21,artwork + '/main/nmvl.png')
        if settings.getSetting('wwmf') == 'true':
                main.addDir('WeWatchMoviesFree','none',42,artwork + '/main/wwmf.png')
        if settings.getSetting('tvrelease') == 'true':
                main.addDir('TV Release','none',128,artwork + '/main/tvrelease.png')
def ADULT():
        pin = ''
        keyboard = xbmc.Keyboard(pin,'Please Enter Your Password')
        keyboard.doModal()
        if keyboard.isConfirmed():
                pin = keyboard.getText()
        text_file = open(xbmc.translatePath("special://home/userdata/addon_data/plugin.video.videophile/sec.0"), "r")
        line = file.readline(text_file)
        if pin == line:
                main.addDir('FreeoMovie','none',133,artwork + '/main/freeomovie.png')
        else:
                notice = xbmcgui.Dialog().ok('Wrong Password','The password you entered is incorrect')

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

elif mode==6:
        print ""+url
        ADULT()

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

elif mode==127:
        print ""+url
        nmvl.HDMOVIES()

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
#I-WatchOnline modes____________________________________________________________
elif mode==50:
        print ""+url
        iwo.MOVIE_CATEGORIES()

elif mode==51:
        print ""+url
        iwo.MOVIE_INDEX(url)

elif mode==52:
        print ""+url
        iwo.VIDEOLINKS(name,url,thumb)

elif mode==53:
        print ""+url
        iwo.HD_MOVIES()

elif mode==54:
        print ""+url
        iwo.LETTERS()

elif mode==55:
        print ""+url
        iwo.HD_LETTERS()

elif mode==56:
        print ""+url
        iwo.GENRES()

elif mode==57:
        print ""+url
        iwo.HD_GENRES()

elif mode==58:
        print ""+url
        iwo.ACTION()

elif mode==59:
        print ""+url
        iwo.ADVENTURE()

elif mode==60:
        print ""+url
        iwo.ANIMATION()

elif mode==61:
        print ""+url
        iwo.BIOGRAPHY()

elif mode==62:
        print ""+url
        iwo.COMEDY()

elif mode==63:
        print ""+url
        iwo.CRIME()

elif mode==64:
        print ""+url
        iwo.DOCUMENTARY()

elif mode==65:
        print ""+url
        iwo.DRAMA()

elif mode==66:
        print ""+url
        iwo.FAMILY()

elif mode==67:
        print ""+url
        iwo.FANTASY()

elif mode==68:
        print ""+url
        iwo.FILMNOIR()

elif mode==69:
        print ""+url
        iwo.HISTORY()

elif mode==70:
        print ""+url
        iwo.HORROR()

elif mode==71:
        print ""+url
        iwo.MUSIC()

elif mode==72:
        print ""+url
        iwo.MUSICAL()

elif mode==73:
        print ""+url
        iwo.MYSTERY()

elif mode==74:
        print ""+url
        iwo.NEWS()

elif mode==75:
        print ""+url
        iwo.ROMANCE()

elif mode==76:
        print ""+url
        iwo.SCIFI()

elif mode==77:
        print ""+url
        iwo.SHORT()

elif mode==78:
        print ""+url
        iwo.SPORT()

elif mode==79:
        print ""+url
        iwo.THRILLER()

elif mode==80:
        print ""+url
        iwo.WAR()

elif mode==81:
        print ""+url
        iwo.WESTERN()


elif mode==82:
        print ""+url
        iwo.HD_ACTION()

elif mode==83:
        print ""+url
        iwo.HD_ADVENTURE()

elif mode==84:
        print ""+url
        iwo.HD_ANIMATION()

elif mode==85:
        print ""+url
        iwo.HD_BIOGRAPHY()

elif mode==86:
        print ""+url
        iwo.HD_COMEDY()

elif mode==87:
        print ""+url
        iwo.HD_CRIME()

elif mode==88:
        print ""+url
        iwo.HD_DOCUMENTARY()

elif mode==89:
        print ""+url
        iwo.HD_DRAMA()

elif mode==90:
        print ""+url
        iwo.HD_FAMILY()

elif mode==91:
        print ""+url
        iwo.HD_FANTASY()

elif mode==92:
        print ""+url
        iwo.HD_FILMNOIR()

elif mode==93:
        print ""+url
        iwo.HD_HISTORY()

elif mode==94:
        print ""+url
        iwo.HD_HORROR()

elif mode==95:
        print ""+url
        iwo.HD_MUSIC()

elif mode==96:
        print ""+url
        iwo.HD_MUSICAL()

elif mode==97:
        print ""+url
        iwo.HD_MYSTERY()

elif mode==98:
        print ""+url
        iwo.HD_NEWS()

elif mode==99:
        print ""+url
        iwo.HD_ROMANCE()

elif mode==100:
        print ""+url
        iwo.HD_SCIFI()

elif mode==101:
        print ""+url
        iwo.HD_SHORT()

elif mode==102:
        print ""+url
        iwo.HD_SPORT()

elif mode==103:
        print ""+url
        iwo.HD_THRILLER()

elif mode==104:
        print ""+url
        iwo.HD_WAR()

elif mode==105:
        print ""+url
        iwo.HD_WESTERN()


elif mode==126:
        print ""+url
        tvrelease.HDMOVIES()

elif mode==128:
        print ""+url
        tvrelease.SEARCH()
        
elif mode==129:
        print ""+url
        tvrelease.VIDEOLINKS(name,url,thumb)

elif mode==130:
        print ""+url
        tvrelease.INDEX(url) 

elif mode==131:
        print ""+url
        tvrelease.MOVIE_CATEGORIES() 

elif mode==132:
        print ""+url
        tvrelease.TV_CATEGORIES()               

elif mode==133:
        print ""+url
        freeomovie.CATEGORIES()

elif mode==134:
        print ""+url
        freeomovie.GENRES()

elif mode==135:
        print ""+url
        freeomovie.INDEX(url)

elif mode==136:
        print ""+url
        freeomovie.VIDEOLINKS(name,url,thumb)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
