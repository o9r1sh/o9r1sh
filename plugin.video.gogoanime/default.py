import urllib,urllib2,re,sys,xbmcplugin,xbmcgui,httplib
import cookielib,os,string,cookielib,StringIO
import xbmcaddon
import urlresolver
import mechanize

artwork = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.gogoanime/art', ''))
imgurl = 'http://www.gogoanime.com/images/'
showurl = 'http://www.gogoanime.com/category/'

def CATEGORIES():
        addDir('Anime Full List','http://www.gogoanime.com/free-anime-list',1,artwork + 'fulllist.png')

                       
def INDEXSHOWS(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('<a href="http://www.gogoanime.com/category/(.+?)" title=".+?">(.+?)</a>').findall(link)
        for url,name in match:

                if "<span>" not in name:
                       addDir(name,showurl + str(url),2,imgurl + str(url))
               

def INDEXEPS(url):
        np = urllib2.Request(url)
        np.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        res = urllib2.urlopen(np)
        lnk =  lnk=res.read()
        res.close()
        page=re.compile('class="current">.+?</span><a href="(.+?)" class="page" title=".+?">.+?</a>').findall(lnk)
        
        
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('<a href="(.+?)" rel="(.+?)" title=".+?">(.+?)</a>').findall(link)
        for url in page:
                if(len(page) > 0):
                        addDir('Next Page',page[0],2,artwork + 'next.png')
                        
        for url,thumbnail,name in match:
                addDir(name,url,3,thumbnail)

def VIDEOLINKS(url,name):
        req = urllib2.Request(url)
        br =  mechanize.Browser()
        br.open(url)
        response1 = br.follow_link(url_regex = "http://www.video44.net")
        newurl = br.geturl()
        
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('src="(.+?)"').findall(link)

        print match
        for url in match:
                if "videoweed.es" in url:
                        req = urllib2.Request(url)
                        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                        response = urllib2.urlopen(req)
                        link=response.read()
                        response.close()
                        match=re.compile('flashvars.advURL="(.+?)"').findall(link)
                        try:
                                addLink('Videoweed',urlresolver.resolve(match[0]),artwork + 'vidweed.png')
                        except:
                                continue

        if "video44.net" in newurl:
                req = urllib2.Request(newurl)
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                response = urllib2.urlopen(req)
                link=response.read()
                response.close()
                match=re.compile(' file: "(.+?)"').findall(link)
                addLink('Video44',match[0],artwork + 'video44.png')

        
             
        

            
                
                
                                
        

                
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
        INDEXSHOWS(url)

elif mode==2:
        print ""+url
        INDEXEPS(url)
        
elif mode==3:
        print ""+url
        VIDEOLINKS(url,name)



xbmcplugin.endOfDirectory(int(sys.argv[1]))
