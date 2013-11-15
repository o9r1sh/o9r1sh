#MoovieManiac Module by o9r1sh September 2013
import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmcaddon,sys,main,xbmc,os
import urlresolver

from t0mm0.common.net import Net
net = Net()

artwork = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.videophile/resources/artwork/', ''))
base_url = 'http://www.mooviemaniac.net'

def CATEGORIES():
        url = base_url + '/movies.htm'
        INDEX(url)
        
def INDEX(url):
        link = net.http_GET(url).content
        match=re.compile('<a href="(.+?)" target=".+?" onclick=".+?">\n  <img class=".+?" src="(.+?)" alt=".+?" title="(.+?)" onmousemove=".+?" style=".+?"/>').findall(link)

        if url == base_url + '/movies.htm':
                main.addDir('Next Page',base_url + '/movies2.htm','moovieManiacIndex',artwork + '/main/next.png')
        elif url == base_url + '/movies2.htm':
                main.addDir('Next Page',base_url + '/movies3.htm','moovieManiacIndex',artwork + '/main/next.png')
        elif url == base_url + '/movies3.htm':
                main.addDir('Next Page',base_url + '/movies4.htm','moovieManiacIndex',artwork + '/main/next.png')
                
        for url,thumbnail,name in match:
                if len(match) > 0:
                        thumbnail = base_url +'/' +  thumbnail
                        head, sep, tail = name.partition(')')
                        name = head[:-5]
                        year = head[-5:] + sep
                try:       
                        main.addMDir(name,url,'resolve',thumbnail,year,False)
                except:
                        continue

        main.AUTOVIEW('movies')


