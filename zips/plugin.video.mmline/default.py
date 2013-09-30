import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmcaddon
import urlresolver
from metahandler import metahandlers



artwork = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.mmline/art/', ''))
base_url = 'http://www.megamovieline.com'
settings = xbmcaddon.Addon(id='<plugin.video.mmline>')
grab=metahandlers.MetaData()


def AUTO_VIEW(content):
        if content:
                xbmcplugin.setContent(int(sys.argv[1]), content)
                if settings.getSetting('auto-view') == 'true':
                        if content == 'movies':
                                xbmc.executebuiltin("Container.SetViewMode(%s)" % settings.getSetting('movies-view') )
                        else:
                                xbmc.executebuiltin("Container.SetViewMode(%s)" % settings.getSetting('default-view') )
                else:
                        xbmc.executebuiltin("Container.SetViewMode(%s)" % settings.getSetting('default-view') )

def GRABMETA(name,year):
        meta = grab.get_meta('movie',name,year,None,None,overlay=6)
        infoLabels = {'rating': meta['rating'],'duration': meta['duration'],'genre': meta['genre'],'mpaa':"rated %s"%meta['mpaa'],
        'plot': meta['plot'],'title': meta['title'],'writer': meta['writer'],'cover_url': meta['cover_url'],
        'director': meta['director'],'cast': meta['cast'],'backdrop_url': meta['backdrop_url'],'tmdb_id': meta['tmdb_id'],'year': meta['year']}
                
        return infoLabels

def CATEGORIES():
        addDir('A-Z',base_url + '/movies/sort/alphabet/page/1',1,artwork + 'a-z.png','','dir')
        addDir('Recently Added',base_url + '/movies/sort/recently/page/1',1,artwork + 'recent.png','','dir')
        addDir('Popular',base_url + '/movies/sort/popular/page/1',1,artwork + 'popular.png','','dir')
        addDir('Highly Rated',base_url + '/movies/sort/ratings/page/1',1,artwork + 'highly.png','','dir')
        addDir('Genres','None',4,artwork + 'genres.png','','dir')
        addDir('Search','None',29,artwork + 'search.png','','dir')
        addDir('Resolver Settings','None',31,artwork + 'resolver.png','','')

        AUTO_VIEW('')
        
def INDEX(url):     
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('<a href="/(.+?) " >').findall(link)
        if len(match) > 0:
                addDir('Next Page',base_url + '/' + str(match[0]),1,artwork + 'next.png','','')
        match=re.compile('<a href="(.+?)"><img src="(.+?)" width=".+?" title=".+?" alt="(.+?)"></a>').findall(link)
        inc = 0
        if len(match) > 0:
                for url,thumbnail,name in match:
                        inc += 1
                        if inc > 8:
                                movie_name = name[:-6]
                                year = name[-6:]
                                movie_name = movie_name.decode('UTF-8','ignore')
                                
                                data = GRABMETA(movie_name,year)
                                
                                favtype = 'movie'
                                addDir(movie_name,base_url + url,2,base_url+thumbnail,data,favtype)

        AUTO_VIEW('movies')
                        
def VIDEOLINKS(url,name):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('<a target="_blank" href="(.+?)">.+?</a>').findall(link)
        if len(match) > 0:
                for url in match:
                        hmf = urlresolver.HostedMediaFile(url)
                        if hmf:
                                host = hmf.get_host()
                                if host.endswith('.com'):
                                        host = host[:-4]
                                if host.endswith('.eu'):
                                        host = host[:-3]
                                if host.endswith('.in'):
                                        host = host[:-3]
                                if host.endswith('.es'):
                                        host = host[:-3]
                                if host.endswith('.tv'):
                                        host = host[:-3]
                                if host.endswith('.net'):
                                        host = host[:-4]
                                if host.endswith('.me'):
                                        host = host[:-3]
                                if host.startswith('www.'):
                                        host = host[4:]
                                
                                addDir(name,url,3,artwork + host + '.png','','')

        AUTO_VIEW('')
        
def RESOLVE(name,url):
        addLink(name,urlresolver.resolve(url),artwork + 'play.png')
        AUTO_VIEW('')
        
def GENRES():
        addDir('Action',base_url + '/movies/gen/Action/page/1',5,artwork + 'action.png','','dir')
        addDir('Adventure',base_url + '/movies/gen/Adventure/page/1',6,artwork + 'adventure.png','','dir')
        addDir('Animation',base_url + '/movies/gen/Animation/page/1',7,artwork + 'animation.png','','dir')
        addDir('Biography',base_url + '/movies/gen/Biography/page/1',8,artwork + 'biography.png','','dir')
        addDir('Comedy',base_url + '/movies/gen/Comedy/page/1',9,artwork + 'comedy.png','','dir')
        addDir('Crime',base_url + '/movies/gen/Crime/page/1',10,artwork + 'crime.png','','dir')
        addDir('Documentary',base_url + '/movies/gen/Documentary/page/1',11,artwork + 'documentary.png','','dir')
        addDir('Drama',base_url + '/movies/gen/Drama/page/1',12,artwork + 'drama.png','','dir')
        addDir('Family',base_url + '/movies/gen/Family/page/1',13,artwork + 'family.png','','dir')
        addDir('Fantasy',base_url + '/movies/gen/Fantasy/page/1',14,artwork + 'fantasy.png','','dir')
        addDir('History',base_url + '/movies/gen/History/page/1',15,artwork + 'history.png','','dir')
        addDir('Horror',base_url + '/movies/gen/Horror/page/1',16,artwork + 'horror.png','','dir')
        addDir('Music',base_url + '/movies/gen/Music/page/1',17,artwork + 'music.png','','dir')
        addDir('Musical',base_url + '/movies/gen/Musical/page/1',18,artwork + 'musical.png','','dir')
        addDir('Mystery',base_url + '/movies/gen/Mystery/page/1',19,artwork + 'mystery.png','','dir')
        addDir('Romance',base_url + '/movies/gen/Romance/page/1',20,artwork + 'romance.png','','dir')
        addDir('Sci-Fi',base_url + '/movies/gen/Sci-Fi/page/1',21,artwork + 'scifi.png','','dir')
        addDir('Sport',base_url + '/movies/gen/Sport/page/1',22,artwork + 'sport.png','','dir')
        addDir('Thriller',base_url + '/movies/gen/Thriller/page/1',23,artwork + 'thriller.png','','dir')
        addDir('War',base_url + '/movies/gen/War/page/1',24,artwork + 'war.png','','dir')
        addDir('Western',base_url + '/movies/gen/Western/page/1',25,artwork + 'western.png','','dir')
        addDir('Indian',base_url + '/movies/gen/Indian/page/1',26,artwork + 'indian.png','','dir')
        addDir('Short',base_url + '/movies/gen/Short/page/1',27,artwork + 'short.png','','dir')
        addDir('Classic',base_url + '/movies/gen/Classic/page/1',28,artwork + 'classic.png','','dir')

        AUTO_VIEW('')
        
def ACTION():
        addDir('A-Z',base_url + '/movies/gen/Action/sort/alphabet/page/1',1,artwork + 'a-z.png','','')
        addDir('Recently Added',base_url + '/movies/gen/Action/sort/recently/page/1',1,artwork + 'recent.png','','')
        addDir('Popular',base_url + '/movies/gen/Action/sort/popular/page/1',1,artwork + 'popular.png','','')
        addDir('Highly Rated',base_url + '/movies/gen/Action/sort/ratings/page/1',1,artwork + 'highly.png','','')

        AUTO_VIEW('')
        
def ADVENTURE():
        addDir('A-Z',base_url + '/movies/gen/Adventure/sort/alphabet/page/1',1,artwork + 'a-z.png','','')
        addDir('Recently Added',base_url + '/movies/gen/Adventure/sort/recently/page/1',1,artwork + 'recent.png','','')
        addDir('Popular',base_url + '/movies/gen/Adventure/sort/popular/page/1',1,artwork + 'popular.png','','')
        addDir('Highly Rated',base_url + '/movies/gen/Adventure/sort/ratings/page/1',1,artwork + 'highly.png','','')

        AUTO_VIEW('')
        
def ANIMATION():
        addDir('A-Z',base_url + '/movies/gen/Animation/sort/alphabet/page/1',1,artwork + 'a-z.png','','')
        addDir('Recently Added',base_url + '/movies/gen/Animation/sort/recently/page/1',1,artwork + 'recent.png','','')
        addDir('Popular',base_url + '/movies/gen/Animation/sort/popular/page/1',1,artwork + 'popular.png','','')
        addDir('Highly Rated',base_url + '/movies/gen/Animation/sort/ratings/page/1',1,artwork + 'highly.png','','')

        AUTO_VIEW('')
        
def BIOGRAPHY():
        addDir('A-Z',base_url + '/movies/gen/Biography/sort/alphabet/page/1',1,artwork + 'a-z.png','','')
        addDir('Recently Added',base_url + '/movies/gen/Biography/sort/recently/page/1',1,artwork + 'recent.png','','')
        addDir('Popular',base_url + '/movies/gen/Biography/sort/popular/page/1',1,artwork + 'popular.png','','')
        addDir('Highly Rated',base_url + '/movies/gen/Biography/sort/ratings/page/1',1,artwork + 'highly.png','','')

        AUTO_VIEW('')
        
def COMEDY():
        addDir('A-Z',base_url + '/movies/gen/Comedy/sort/alphabet/page/1',1,artwork + 'a-z.png','','')
        addDir('Recently Added',base_url + '/movies/gen/Comedy/sort/recently/page/1',1,artwork + 'recent.png','','')
        addDir('Popular',base_url + '/movies/gen/Comedy/sort/popular/page/1',1,artwork + 'popular.png','','')
        addDir('Highly Rated',base_url + '/movies/gen/Comedy/sort/ratings/page/1',1,artwork + 'highly.png','','')

        AUTO_VIEW('')
        
def CRIME():
        addDir('A-Z',base_url + '/movies/gen/Crime/sort/alphabet/page/1',1,artwork + 'a-z.png','','')
        addDir('Recently Added',base_url + '/movies/gen/Crime/sort/recently/page/1',1,artwork + 'recent.png','','')
        addDir('Popular',base_url + '/movies/gen/Crime/sort/popular/page/1',1,artwork + 'popular.png','','')
        addDir('Highly Rated',base_url + '/movies/gen/Crime/sort/ratings/page/1',1,artwork + 'highly.png','','')

        AUTO_VIEW('')
        
def DOCUMENTARY():
        addDir('A-Z',base_url + '/movies/gen/Documentary/sort/alphabet/page/1',1,artwork + 'a-z.png','','')
        addDir('Recently Added',base_url + '/movies/gen/Documentary/sort/recently/page/1',1,artwork + 'recent.png','','')
        addDir('Popular',base_url + '/movies/gen/Documentary/sort/popular/page/1',1,artwork + 'popular.png','','')
        addDir('Highly Rated',base_url + '/movies/gen/Documentary/sort/ratings/page/1',1,artwork + 'highly.png','','')

        AUTO_VIEW('')
        
def DRAMA():
        addDir('A-Z',base_url + '/movies/gen/Drama/sort/alphabet/page/1',1,artwork + 'a-z.png','','')
        addDir('Recently Added',base_url + '/movies/gen/Drama/sort/recently/page/1',1,artwork + 'recent.png','','')
        addDir('Popular',base_url + '/movies/gen/Drama/sort/popular/page/1',1,artwork + 'popular.png','','')
        addDir('Highly Rated',base_url + '/movies/gen/Drama/sort/ratings/page/1',1,artwork + 'highly.png','','')

        AUTO_VIEW('')
        
def FAMILY():
        addDir('A-Z',base_url + '/movies/gen/Family/sort/alphabet/page/1',1,artwork + 'a-z.png','','')
        addDir('Recently Added',base_url + '/movies/gen/Family/sort/recently/page/1',1,artwork + 'recent.png','','')
        addDir('Popular',base_url + '/movies/gen/Family/sort/popular/page/1',1,artwork + 'popular.png','','')
        addDir('Highly Rated',base_url + '/movies/gen/Family/sort/ratings/page/1',1,artwork + 'highly.png','','')

        AUTO_VIEW('')
        
def FANTASY():
        addDir('A-Z',base_url + '/movies/gen/Fantasy/sort/alphabet/page/1',1,artwork + 'a-z.png','','')
        addDir('Recently Added',base_url + '/movies/gen/Fantasy/sort/recently/page/1',1,artwork + 'recent.png','','')
        addDir('Popular',base_url + '/movies/gen/Fantasy/sort/popular/page/1',1,artwork + 'popular.png','','')
        addDir('Highly Rated',base_url + '/movies/gen/Fantasy/sort/ratings/page/1',1,artwork + 'highly.png','','')

        AUTO_VIEW('')
        
def HISTORY():
        addDir('A-Z',base_url + '/movies/gen/History/sort/alphabet/page/1',1,artwork + 'a-z.png','','')
        addDir('Recently Added',base_url + '/movies/gen/History/sort/recently/page/1',1,artwork + 'recent.png','','')
        addDir('Popular',base_url + '/movies/gen/History/sort/popular/page/1',1,artwork + 'popular.png','','')
        addDir('Highly Rated',base_url + '/movies/gen/History/sort/ratings/page/1',1,artwork + 'highly.png','','')

        AUTO_VIEW('')
        
def HORROR():
        addDir('A-Z',base_url + '/movies/gen/Horror/sort/alphabet/page/1',1,artwork + 'a-z.png','','')
        addDir('Recently Added',base_url + '/movies/gen/Horror/sort/recently/page/1',1,artwork + 'recent.png','','')
        addDir('Popular',base_url + '/movies/gen/Horror/sort/popular/page/1',1,artwork + 'popular.png','','')
        addDir('Highly Rated',base_url + '/movies/gen/Horror/sort/ratings/page/1',1,artwork + 'highly.png','','')

        AUTO_VIEW('')
        
def MUSIC():
        addDir('A-Z',base_url + '/movies/gen/Music/sort/alphabet/page/1',1,artwork + 'a-z.png','','')
        addDir('Recently Added',base_url + '/movies/gen/Music/sort/recently/page/1',1,artwork + 'recent.png','','')
        addDir('Popular',base_url + '/movies/gen/Music/sort/popular/page/1',1,artwork + 'popular.png','','')
        addDir('Highly Rated',base_url + '/movies/gen/Music/sort/ratings/page/1',1,artwork + 'highly.png','','')

        AUTO_VIEW('')
        
def MUSICAL():
        addDir('A-Z',base_url + '/movies/gen/Musical/sort/alphabet/page/1',1,artwork + 'a-z.png','','')
        addDir('Recently Added',base_url + '/movies/gen/Musical/sort/recently/page/1',1,artwork + 'recent.png','','')
        addDir('Popular',base_url + '/movies/gen/Musical/sort/popular/page/1',1,artwork + 'popular.png','','')
        addDir('Highly Rated',base_url + '/movies/gen/Musical/sort/ratings/page/1',1,artwork + 'highly.png','','')

        AUTO_VIEW('')
        
def MYSTERY():
        addDir('A-Z',base_url + '/movies/gen/Mystery/sort/alphabet/page/1',1,artwork + 'a-z.png','','')
        addDir('Recently Added',base_url + '/movies/gen/Mystery/sort/recently/page/1',1,artwork + 'recent.png','','')
        addDir('Popular',base_url + '/movies/gen/Mystery/sort/popular/page/1',1,artwork + 'popular.png','','')
        addDir('Highly Rated',base_url + '/movies/gen/Mystery/sort/ratings/page/1',1,artwork + 'highly.png','','')

        AUTO_VIEW('')
        
def ROMANCE():
        addDir('A-Z',base_url + '/movies/gen/Romance/sort/alphabet/page/1',1,artwork + 'a-z.png','','')
        addDir('Recently Added',base_url + '/movies/gen/Romance/sort/recently/page/1',1,artwork + 'recent.png','','')
        addDir('Popular',base_url + '/movies/gen/Romance/sort/popular/page/1',1,artwork + 'popular.png','','')
        addDir('Highly Rated',base_url + '/movies/gen/Romance/sort/ratings/page/1',1,artwork + 'highly.png','','')

        AUTO_VIEW('')
        
def SCIFI():
        addDir('A-Z',base_url + '/movies/gen/Sci-Fi/sort/alphabet/page/1',1,artwork + 'a-z.png','','')
        addDir('Recently Added',base_url + '/movies/gen/Sci-Fi/sort/recently/page/1',1,artwork + 'recent.png','','')
        addDir('Popular',base_url + '/movies/gen/Sci-Fi/sort/popular/page/1',1,artwork + 'popular.png','','')
        addDir('Highly Rated',base_url + '/movies/gen/Sci-Fi/sort/ratings/page/1',1,artwork + 'highly.png','','')

        AUTO_VIEW('')
        
def SPORT():
        addDir('A-Z',base_url + '/movies/gen/Sport/sort/alphabet/page/1',1,artwork + 'a-z.png','','')
        addDir('Recently Added',base_url + '/movies/gen/Sport/sort/recently/page/1',1,artwork + 'recent.png','','')
        addDir('Popular',base_url + '/movies/gen/Sport/sort/popular/page/1',1,artwork + 'popular.png','','')
        addDir('Highly Rated',base_url + '/movies/gen/Sport/sort/ratings/page/1',1,artwork + 'highly.png','','')

        AUTO_VIEW('')
        
def THRILLER():
        addDir('A-Z',base_url + '/movies/gen/Thriller/sort/alphabet/page/1',1,artwork + 'a-z.png','','')
        addDir('Recently Added',base_url + '/movies/gen/Thriller/sort/recently/page/1',1,artwork + 'recent.png','','')
        addDir('Popular',base_url + '/movies/gen/Thriller/sort/popular/page/1',1,artwork + 'popular.png','','')
        addDir('Highly Rated',base_url + '/movies/gen/Thriller/sort/ratings/page/1',1,artwork + 'highly.png','','')

        AUTO_VIEW('')
        
def WAR():
        addDir('A-Z',base_url + '/movies/gen/War/sort/alphabet/page/1',1,artwork + 'a-z.png','','')
        addDir('Recently Added',base_url + '/movies/gen/War/sort/recently/page/1',1,artwork + 'recent.png','','')
        addDir('Popular',base_url + '/movies/gen/War/sort/popular/page/1',1,artwork + 'popular.png','','')
        addDir('Highly Rated',base_url + '/movies/gen/War/sort/ratings/page/1',1,artwork + 'highly.png','','')

        AUTO_VIEW('')
        
def WESTERN():
        addDir('A-Z',base_url + '/movies/gen/Western/sort/alphabet/page/1',1,artwork + 'a-z.png','','')
        addDir('Recently Added',base_url + '/movies/gen/Western/sort/recently/page/1',1,artwork + 'recent.png','','')
        addDir('Popular',base_url + '/movies/gen/Western/sort/popular/page/1',1,artwork + 'popular.png','','')
        addDir('Highly Rated',base_url + '/movies/gen/Western/sort/ratings/page/1',1,artwork + 'highly.png','','')

        AUTO_VIEW('')
        
def INDIAN():
        addDir('A-Z',base_url + '/movies/gen/Indian/sort/alphabet/page/1',1,artwork + 'a-z.png','','')
        addDir('Recently Added',base_url + '/movies/gen/Indian/sort/recently/page/1',1,artwork + 'recent.png','','')
        addDir('Popular',base_url + '/movies/gen/Indian/sort/popular/page/1',1,artwork + 'popular.png','','')
        addDir('Highly Rated',base_url + '/movies/gen/Indian/sort/ratings/page/1',1,artwork + 'highly.png','','')

        AUTO_VIEW('')
        
def SHORT():
        addDir('A-Z',base_url + '/movies/gen/Short/sort/alphabet/page/1',1,artwork + 'a-z.png','','')
        addDir('Recently Added',base_url + '/movies/gen/Short/sort/recently/page/1',1,artwork + 'recent.png','','')
        addDir('Popular',base_url + '/movies/gen/Short/sort/popular/page/1',1,artwork + 'popular.png','','')
        addDir('Highly Rated',base_url + '/movies/gen/Short/sort/ratings/page/1',1,artwork + 'highly.png','','')

        AUTO_VIEW('')
        
def CLASSIC():
        addDir('A-Z',base_url + '/movies/gen/Classic/sort/alphabet/page/1',1,artwork + 'a-z.png','','')
        addDir('Recently Added',base_url + '/movies/gen/Classic/sort/recently/page/1',1,artwork + 'recent.png','','')
        addDir('Popular',base_url + '/movies/gen/Classic/sort/popular/page/1',1,artwork + 'popular.png','','')
        addDir('Highly Rated',base_url + '/movies/gen/Classic/sort/ratings/page/1',1,artwork + 'highly.png','','')

        AUTO_VIEW('')
        
def SEARCH():
        search = ''
        keyboard = xbmc.Keyboard(search,'Search')
        keyboard.doModal()
        if keyboard.isConfirmed():
                search = keyboard.getText()
                search = search.replace(' ','+')
                
                url = base_url + '?search_key=' + search
                
                req = urllib2.Request(url)
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                response = urllib2.urlopen(req)
                link=response.read()
                response.close()
                match=re.compile('<a href="(.+?)"><img src="(.+?)" width=".+?" title=".+?" alt="(.+?)"></a>').findall(link)

                if len(match) > 8:
                        inc = 0
                        for url,thumbnail,name in match:
                                inc += 1
                                if inc > 8:
                                        movie_name = name[:-6]
                                        year = name[-6:]
                                        movie_name = movie_name.decode('UTF-8','ignore')
                                        data = GRABMETA(movie_name,year)
                                        addDir(movie_name,base_url + url,2,base_url + thumbnail,data,'movie')
                AUTO_VIEW('movies')

def COLLECTIVESEARCH(name):
        
        search = name
        search = search.replace(' ','+')
        
        url = base_url + '?search_key=' + search
        
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('<a href="(.+?)"><img src="(.+?)" width=".+?" title=".+?" alt="(.+?)"></a>').findall(link)

        if len(match) > 8:
                inc = 0
                for url,thumbnail,name in match:
                        inc += 1
                        if inc > 8:
                                movie_name = name[:-6]
                                year = name[-6:]
                                movie_name = movie_name.decode('UTF-8','ignore')
                                data = GRABMETA(movie_name,year)
                                addDir(movie_name,base_url + url,2,base_url + thumbnail,data,'movie')
        AUTO_VIEW('movies')
                                        
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

def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return ok

def addDir(name,url,mode,iconimage,labels,favtype):
        contextMenuItems = []
    
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels=labels )
        
        if favtype == 'movie':
                contextMenuItems.append(('Movie Information', 'XBMC.Action(Info)'))

                if os.path.exists(xbmc.translatePath("special://home/addons/plugin.video.collective")):
                        contextMenuItems.append(('Search The Collective', 'XBMC.Container.Update(%s?mode=51&url=url&name=%s)' % ('plugin://plugin.video.collective/', name)))

        liz.addContextMenuItems(contextMenuItems, replaceItems=False)

        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)

        return ok        
              
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

if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES() 
elif mode==1:
        print ""+url
        INDEX(url) 
elif mode==2:
        print ""+url
        VIDEOLINKS(url,name)
elif mode==3:
        print ""+url
        RESOLVE(name,url)
elif mode==4:
        print ""+url
        GENRES()
elif mode==5:
        print ""+url
        ACTION()
elif mode==6:
        print ""+url
        ADVENTURE()
elif mode==7:
        print ""+url
        ANIMATION()
elif mode==8:
        print ""+url
        BIOGRAPHY()
elif mode==9:
        print ""+url
        COMEDY()
elif mode==10:
        print ""+url
        CRIME()
elif mode==11:
        print ""+url
        DOCUMENTARY()
elif mode==12:
        print ""+url
        DRAMA()
elif mode==13:
        print ""+url
        FAMILY()
elif mode==14:
        print ""+url
        FANTASY()
elif mode==15:
        print ""+url
        HISTORY()
elif mode==16:
        print ""+url
        HORROR()
elif mode==17:
        print ""+url
        MUSIC()
elif mode==18:
        print ""+url
        MUSICAL()
elif mode==19:
        print ""+url
        MYSTERY()
elif mode==20:
        print ""+url
        ROMANCE()
elif mode==21:
        print ""+url
        SCIFI()
elif mode==22:
        print ""+url
        SPORT()
elif mode==23:
        print ""+url
        THRILLER()
elif mode==24:
        print ""+url
        WAR()
elif mode==25:
        print ""+url
        WESTERN()
elif mode==26:
        print ""+url
        INDIAN()
elif mode==27:
        print ""+url
        SHORT()
elif mode==28:
        print ""+url
        CLASSIC()
elif mode==29:
        print ""+url
        SEARCH()
elif mode==30:
        print ""+url
        COLLECTIVESEARCH(name)
elif mode==31:
        print ""+url
        urlresolver.display_settings()
   
xbmcplugin.endOfDirectory(int(sys.argv[1]))
