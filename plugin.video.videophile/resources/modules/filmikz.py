#Filmikz module by o9r1sh

import urllib,urllib2,re,xbmcplugin,xbmcgui,sys,main,urlresolver,xbmc,os

from t0mm0.common.net import Net
net = Net()

artwork = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.videophile/resources/artwork/', ''))
base_url = 'http://filmikz.ch/'

def ADULT_CATEGORIES():
        main.addDir('Adult Movies',base_url + 'index.php?genre=14','filmikzAdultIndex',artwork + '/main/movie.png')  
        main.addDir('Adult Search','none','filmikzAdultSearch',artwork + '/main/search.png')  

def ADULT_INDEX(url):
        link = net.http_GET(url).content
        match=re.compile('<img src="(.+?)" width=".+?" height=".+?" border=".+?" /></a></div></td>\n                           \n                            <td width=".+?" valign=".+?" class=".+?"  align=".+?"><p><strong>(.+?): </strong></p>\n                                <p>.+?</p>\n                              <p><span class=".+?"><a href="/(.+?)">').findall(link)
        np=re.compile("href='(.+?)'>(.+?)</a></td><td><a style='color:red").findall(link)
        for url,name in np:
                if '&rsaquo' in name:
                        url = base_url + url
                        main.addDir('Next Page',url,'filmikzAdultIndex', artwork + 'main/next.png')
                        
        for thumbnail,name,url in match:
                url = base_url + url
                thumbnail = base_url + thumbnail
                main.addDir(name,url,'filmikzVideoLinks',thumbnail)
                                 
def VIDEOLINKS(url,name,thumb):
        link = net.http_GET(url).content
        match=re.compile('<input type=button value="(.+?)" onClick="javascript:popUp((.+?))">').findall(link)
        for host, url,url2 in match:
                url = base_url + url
                url = re.sub("[')(]", '', url)
                link = net.http_GET(url).content
                links2=re.compile('<frameset  cols=".+?">\n  <frame src="(.+?)" />\n  <frame src=".+?" />').findall(link)
                if len(links2) > 0:
                        url = str(links2[0])
                if main.resolvable(url):
                        hthumb = main.GETHOSTTHUMB(main.getHost(url))
                try:
                        main.addHDir(name,url,'resolve',thumb,hthumb)
                except:
                        continue
       
         
def ADULT_SEARCH():
        search = ''
        keyboard = xbmc.Keyboard(search,'Search')
        keyboard.doModal()
        if keyboard.isConfirmed():
                search = keyboard.getText()
                search = re.sub(' ','+', search)
                
                url = base_url + 'index.php?search=' + search
                ADULT_INDEX(url)
                



                


