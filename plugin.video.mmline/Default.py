import urllib,urllib2,re,xbmcplugin,xbmcgui
import urlresolver

base_url = 'http://www.megamovieline.com/'

def CATEGORIES():
        addDir('A-Z','http://www.megamovieline.com/movies/sort/alphabet/page/1',1,'')
        addDir('Recently Added','http://www.megamovieline.com/movies/sort/recently/page/1',1,'')
        addDir('Popular','http://www.megamovieline.com/movies/sort/popular/page/1',1,'')
        addDir('Highly Rated','http://www.megamovieline.com/movies/sort/ratings/page/1',1,'')

def INDEX(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('<a href="/(.+?) " >').findall(link)
        print(match)
        if len(match) > -1:
                addDir('Next Page',base_url + str(match[0]),1,'')
        match=re.compile('<a href="(.+?)"><img src="(.+?)" width=".+?" title=".+?" alt="(.+?)"></a>').findall(link)
        inc = 0
        for url,thumbnail,name in match:
                inc += 1
                if inc > 8:
                        addDir(name,base_url + url,2,base_url + thumbnail)

def VIDEOLINKS(url,name):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('<a target="_blank" href="(.+?)">.+?</a>').findall(link)
        for url in match:
                if 'putlocker' in url:
                        addDir('Putlocker',url,3,'')
                if 'sockshare' in url:
                        addDir('Sockshare',url,3,'')
                if 'filenuke' in url:
                        addDir('Filenuke',url,3,'')
                if 'nowvideo' in url:
                        addDir('Nowvideo',url,3,'')
                if 'youtube' in url:
                        addDir('Youtube',url,3,'')
                if 'stagevu' in url:
                        addDir('Stagevu',url,3,'')
                if 'divxstage' in url:
                        addDir('Divxstage',url,3,'')
        


def RESOLVE(url):
        addLink('Play Movie',urlresolver.resolve(url),'')
        
                
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


def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
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
        RESOLVE(url)



xbmcplugin.endOfDirectory(int(sys.argv[1]))
