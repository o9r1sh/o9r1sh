import urllib,urllib2,re,xbmcplugin,xbmcgui
import urlresolver,xbmcaddon

base_url = 'http://filmikz.net/'
artwork = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.filmikz/art/', ''))

settings = xbmcaddon.Addon(id='<plugin.video.filikz>')
adult_content = settings.getSetting('adult_content')

def CATEGORIES():
        if adult_content == 'true':
                addDir('Adult Movies',base_url + 'index.php?genre=14',1,artwork + 'adult.png','')  
        addDir('Recently Added Movies',base_url + 'index.php',1,artwork + 'new_movies.png','')
        addDir('Recently Added Episodes',base_url + 'index.php?genre=15',1,artwork + 'new_episodes.png','')
        addDir('Movie Genres',base_url,3,artwork + 'genres.png','')
        addDir('Search',base_url,5,artwork + 'search.png','')
def INDEX(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        pages=re.compile("<a style=\'color:red;\' href=\'(.+?)'>(.+?)</a>").findall(link)
        
        if url == base_url + 'index.php':
                next_page = str(pages[10][0])
                addDir('Next Page',base_url + next_page,1,artwork + 'next.png','')

        elif url == base_url + 'index.php?genre=15':
                next_page = str(pages[10][0])
                addDir('Next Page',base_url + next_page,1,artwork + 'next.png','')

        elif url == base_url + 'index.php?genre=3':
                next_page = str(pages[10][0])
                addDir('Next Page',base_url + next_page,1,artwork + 'next.png','')

        elif url == base_url + 'index.php?genre=2':
                next_page = str(pages[10][0])
                addDir('Next Page',base_url + next_page,1,artwork + 'next.png','')

        elif url == base_url + 'index.php?genre=11':
                next_page = str(pages[10][0])
                addDir('Next Page',base_url + next_page,1,artwork + 'next.png','')

        elif url == base_url + 'index.php?genre=12':
                next_page = str(pages[10][0])
                addDir('Next Page',base_url + next_page,1,artwork + 'next.png','')

        elif url == base_url + 'index.php?genre=1':
                next_page = str(pages[10][0])
                addDir('Next Page',base_url + next_page,1,artwork + 'next.png','')

        elif url == base_url + 'index.php?genre=5':
                next_page = str(pages[10][0])
                addDir('Next Page',base_url + next_page,1,artwork + 'next.png','')

        elif url == base_url + 'index.php?genre=6':
                next_page = str(pages[10][0])
                addDir('Next Page',base_url + next_page,1,artwork + 'next.png','')

        elif url == base_url + 'index.php?genre=13':
                next_page = str(pages[10][0])
                addDir('Next Page',base_url + next_page,1,artwork + 'next.png','')

        elif url == base_url + 'index.php?genre=4':
                next_page = str(pages[10][0])
                addDir('Next Page',base_url + next_page,1,artwork + 'next.png','')

        elif url == base_url + 'index.php?genre=14':
                next_page = str(pages[10][0])
                addDir('Next Page',base_url + next_page,1,artwork + 'next.png','')
                
        else:
                next_page = str(pages[11][0])
                addDir('Next Page',base_url + next_page,1,artwork + 'next.png','')
        
        match=re.compile('<img src="(.+?)" width=".+?" height=".+?" border=".+?" /></a></div></td>\n                           \n                            <td width=".+?" valign=".+?" class=".+?"  align=".+?"><p><strong>(.+?): </strong></p>\n                                <p>(.+?)</p>\n                              <p><span class=".+?"><a href="/(.+?)">').findall(link)
        for thumbnail,name,plot,url in match:
                if adult_content == 'false':
                        if 'XXX' in url:
                                continue
                        else:
                                addDir(name,base_url + url,2,base_url + thumbnail,plot)
                else:
                         addDir(name,base_url + url,2,base_url + thumbnail,plot)

def VIDEOLINKS(url,name):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        multi_part=re.compile('<input type=button value="(.+?)" onClick="javascript:popUp((.+?))">').findall(link)
        
        for name, url,url2 in multi_part:
                req = urllib2.Request(base_url + re.sub("[')(]", '', url))
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                response = urllib2.urlopen(req)
                link=response.read()
                response.close()
                links2=re.compile('<frameset  cols=".+?">\n  <frame src="(.+?)" />\n  <frame src=".+?" />').findall(link)
                if name.find("NowDownload") == -1 and name.find("Billionuploads") ==-1:
                        addDir(name,links2[0],4,artwork  + name +'.png','')
                

def RESOLVE(name,url):
        if 'ePornik' in name:
                
                req = urllib2.Request(url)
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                response = urllib2.urlopen(req)
                link=response.read()
                response.close()
                elink=re.compile('s1.addVariable(.+?);').findall(link)

                dirty = re.sub("[',)(]", '', (elink[5]))
                clean =   dirty[7:-1]

                addLink('Play Video',clean,artwork + 'play.png')

                
        else:
                addLink('Play Video',urlresolver.resolve(url),artwork + 'play.png')                                

def GENRES():
        addDir('Action',base_url +'index.php?genre=3',1,artwork + 'action.png','')
        addDir('Drama',base_url +'index.php?genre=2',1,artwork + 'drama.png','')
        addDir('Thriller',base_url +'index.php?genre=11',1,artwork + 'thriller.png','')
        addDir('Western',base_url +'index.php?genre=12',1,artwork + 'western.png','')
        addDir('Comedy',base_url +'index.php?genre=1',1,artwork + 'comedy.png','')
        addDir('Horror',base_url +'index.php?genre=5',1,artwork + 'horror.png','')
        addDir('Animation',base_url +'index.php?genre=6',1,artwork + 'animation.png','')
        addDir('Adventure',base_url +'index.php?genre=13',1,artwork + 'adventure.png','')
        addDir('Sci-Fi',base_url +'index.php?genre=4',1,artwork + 'scifi.png','')

def SEARCH():
        search = ''
        keyboard = xbmc.Keyboard(search,'Search')
        keyboard.doModal()
        if keyboard.isConfirmed():
                search = keyboard.getText()
                
                url = base_url + 'index.php?search=' + search
                
                req = urllib2.Request(url)
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                response = urllib2.urlopen(req)
                link=response.read()
                response.close()
                match=re.compile('<img src="(.+?)" width=".+?" height=".+?" border=".+?" /></a></div></td>\n                           \n                            <td width=".+?" valign=".+?" class=".+?"  align=".+?"><p><strong>(.+?): </strong></p>\n                                <p>(.+?)</p>\n                              <p><span class=".+?"><a href="/(.+?)">').findall(link)
                for thumbnail,name,plot,url in match:
                        if 'XXX' in url:
                                continue
                        else:
                                addDir(name,base_url + url,2,base_url + thumbnail,plot)
                
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


def addDir(name,url,mode,iconimage,plot):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name , "Plot": plot })
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
        GENRES()
elif mode==4:
        print ""+url
        RESOLVE(name,url)
elif mode==5:
        print ""+url
        SEARCH()



xbmcplugin.endOfDirectory(int(sys.argv[1]))
