#Cartoon Freak Module by o9r1sh October 2013

import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmcaddon,sys,main,xbmc,os
import urlresolver

artwork = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.videophile/resources/artwork/', ''))
base_url = 'http://www.cartoonfreak.net'

def CARTOONS():
        INDEX(base_url + '/cartoon/')

def ANIME():
        main.addDir('Anime Series','none','cartoonFreakAnimeSeries',artwork + '')
        main.addDir('Anime Movies','none','cartoonFreakAnimeMovies',artwork + '')

def ANIMESERIES():
        main.addDir('All', base_url + '/anime/','cartoonFreakIndex',artwork + '')
        main.addDir('A', base_url + '/anime/?alpha=a','cartoonFreakIndex',artwork + '')
        main.addDir('B', base_url + '/anime/?alpha=b','cartoonFreakIndex',artwork + '')
        main.addDir('C', base_url + '/anime/?alpha=c','cartoonFreakIndex',artwork + '')
        main.addDir('D', base_url + '/anime/?alpha=d','cartoonFreakIndex',artwork + '')
        main.addDir('E', base_url + '/anime/?alpha=e','cartoonFreakIndex',artwork + '')
        main.addDir('F', base_url + '/anime/?alpha=g','cartoonFreakIndex',artwork + '')
        main.addDir('H', base_url + '/anime/?alpha=h','cartoonFreakIndex',artwork + '')
        main.addDir('I', base_url + '/anime/?alpha=i','cartoonFreakIndex',artwork + '')
        main.addDir('J', base_url + '/anime/?alpha=j','cartoonFreakIndex',artwork + '')
        main.addDir('K', base_url + '/anime/?alpha=k','cartoonFreakIndex',artwork + '')
        main.addDir('L', base_url + '/anime/?alpha=l','cartoonFreakIndex',artwork + '')
        main.addDir('M', base_url + '/anime/?alpha=m','cartoonFreakIndex',artwork + '')
        main.addDir('N', base_url + '/anime/?alpha=n','cartoonFreakIndex',artwork + '')
        main.addDir('O', base_url + '/anime/?alpha=o','cartoonFreakIndex',artwork + '')
        main.addDir('P', base_url + '/anime/?alpha=p','cartoonFreakIndex',artwork + '')
        main.addDir('Q', base_url + '/anime/?alpha=q','cartoonFreakIndex',artwork + '')
        main.addDir('R', base_url + '/anime/?alpha=r','cartoonFreakIndex',artwork + '')
        main.addDir('S', base_url + '/anime/?alpha=s','cartoonFreakIndex',artwork + '')
        main.addDir('T', base_url + '/anime/?alpha=t','cartoonFreakIndex',artwork + '')
        main.addDir('U', base_url + '/anime/?alpha=u','cartoonFreakIndex',artwork + '')
        main.addDir('V', base_url + '/anime/?alpha=v','cartoonFreakIndex',artwork + '')
        main.addDir('W', base_url + '/anime/?alpha=w','cartoonFreakIndex',artwork + '')
        main.addDir('X', base_url + '/anime/?alpha=x','cartoonFreakIndex',artwork + '')
        main.addDir('Y', base_url + '/anime/?alpha=y','cartoonFreakIndex',artwork + '')
        main.addDir('Z', base_url + '/anime/?alpha=z','cartoonFreakIndex',artwork + '')

def ANIMEMOVIES():
        main.addDir('All', base_url + '/movie/','cartoonFreakMovieIndex',artwork + '')
        main.addDir('A', base_url + '/movie/?alpha=a','cartoonFreakMovieIndex',artwork + '')
        main.addDir('B', base_url + '/movie/?alpha=b','cartoonFreakMovieIndex',artwork + '')
        main.addDir('C', base_url + '/movie/?alpha=c','cartoonFreakMovieIndex',artwork + '')
        main.addDir('D', base_url + '/movie/?alpha=d','cartoonFreakMovieIndex',artwork + '')
        main.addDir('E', base_url + '/movie/?alpha=e','cartoonFreakMovieIndex',artwork + '')
        main.addDir('F', base_url + '/movie/?alpha=f','cartoonFreakMovieIndex',artwork + '')
        main.addDir('G', base_url + '/movie/?alpha=g','cartoonFreakMovieIndex',artwork + '')
        main.addDir('H', base_url + '/movie/?alpha=h','cartoonFreakMovieIndex',artwork + '')
        main.addDir('I', base_url + '/movie/?alpha=i','cartoonFreakMovieIndex',artwork + '')
        main.addDir('J', base_url + '/movie/?alpha=j','cartoonFreakMovieIndex',artwork + '')
        main.addDir('K', base_url + '/movie/?alpha=k','cartoonFreakMovieIndex',artwork + '')
        main.addDir('L', base_url + '/movie/?alpha=l','cartoonFreakMovieIndex',artwork + '')
        main.addDir('M', base_url + '/movie/?alpha=m','cartoonFreakMovieIndex',artwork + '')
        main.addDir('N', base_url + '/movie/?alpha=n','cartoonFreakMovieIndex',artwork + '')
        main.addDir('O', base_url + '/movie/?alpha=o','cartoonFreakMovieIndex',artwork + '')
        main.addDir('P', base_url + '/movie/?alpha=p','cartoonFreakMovieIndex',artwork + '')
        main.addDir('Q', base_url + '/movie/?alpha=q','cartoonFreakMovieIndex',artwork + '')
        main.addDir('R', base_url + '/movie/?alpha=r','cartoonFreakMovieIndex',artwork + '')
        main.addDir('S', base_url + '/movie/?alpha=s','cartoonFreakMovieIndex',artwork + '')
        main.addDir('T', base_url + '/movie/?alpha=t','cartoonFreakMovieIndex',artwork + '')
        main.addDir('U', base_url + '/movie/?alpha=u','cartoonFreakMovieIndex',artwork + '')
        main.addDir('V', base_url + '/movie/?alpha=v','cartoonFreakMovieIndex',artwork + '')
        main.addDir('W', base_url + '/movie/?alpha=w','cartoonFreakMovieIndex',artwork + '')
        main.addDir('X', base_url + '/movie/?alpha=x','cartoonFreakMovieIndex',artwork + '')
        main.addDir('Y', base_url + '/movie/?alpha=y','cartoonFreakMovieIndex',artwork + '')
        main.addDir('Z', base_url + '/movie/?alpha=Z','cartoonFreakMovieIndex',artwork + '')
    
def INDEX(url):
        o_url = url
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('<li id="(.+?)"><div class="anime-list-item"><a href="(.+?)" class="thumbnail"><img data-src=".+?" alt=".+?" src="(.+?)" class="primary" /><span class="play"></span><span class=".+?">(.+?)</span><span class="anime-data">').findall(link)
        np=re.compile('<a class="pagination-next btn btn-inverse" href="(.+?)">').findall(link)
        if len(np) > 0:
                np_url = np[0]
                next_page = base_url + np_url
                main.addDir('Next Page',next_page,'cartoonFreakIndex',artwork + '/main/next.png')
        for vid,url,thumbnail,name in match:
                if 'anime' in o_url:       
                        try:
                                main.addSDir(name,url,'cartoonFreakAnimeEpisodes',thumbnail)
                        except:
                                continue
                else:
                                
                        try:
                                main.addSDir(name,url,'cartoonFreakEpisodes',thumbnail)
                        except:
                                continue
                
        main.AUTOVIEW('tvshows')

def MOVIEINDEX(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('<li id="(.+?)"><div class="anime-list-item"><a href="(.+?)" class="thumbnail"><img data-src=".+?" alt=".+?" src="(.+?)" class="primary" /><span class="play"></span><span class=".+?">(.+?)</span><span class="anime-data">').findall(link)
        np=re.compile('<a class="pagination-next btn btn-inverse" href="(.+?)">').findall(link)
        if len(np) > 0:
                np_url = np[0]
                next_page = base_url + np_url
                main.addDir('Next Page',next_page,'cartoonFreakMovieIndex',artwork + '/main/next.png')
        for vid,url,thumbnail,name in match:
                try:
                        main.addMDir(name,url,'cartoonFreakMovieEpisodes',thumbnail,'')
                except:
                        continue
                
        main.AUTOVIEW('movies')

def MOVIEEPISODES(url,thumb):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('<li class=".+?"><a href="(.+?)"><i class="icon-chevron-right"></i>(.+?)</a></li>').findall(link)
        for url, name in match:
                VIDEOLINKS(name,url,thumb)
        main.AUTOVIEW('movies')           

def EPISODES(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('<li class=".+?"><a href="(.+?)"><i class="icon-chevron-right"></i>(.+?)</a></li>').findall(link)
        for url, name in match:
                name = re.sub(' Episode ','x',name)
                show,sep,numbers = name.partition('Season')
                name = show + '' + numbers
                name = name.replace("&#8217;","")
                try:
                        main.addEDir(name,url,'cartoonFreakVideoLinks','',show)
                except:
                        continue
        main.AUTOVIEW('episodes')

def ANIMEEPISODES(url,thumb):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('<li class=".+?"><a href="(.+?)"><i class="icon-chevron-right"></i>(.+?)</a></li>').findall(link)
        for url, name in match:
                try:
                        main.addSDir(name,url,'cartoonFreakVideoLinks',thumb)
                except:
                        continue
        main.AUTOVIEW('episodes')
        
def VIDEOLINKS(name,url,thumb):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('<iframe src="(.+?)" width=".+?" height=".+?" scrolling=".+?" frameborder=".+?"></iframe>').findall(link)
        htumb = None
        for url in match:
                try:
                        req = urllib2.Request(url)
                        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                        response = urllib2.urlopen(req)
                        link=response.read()
                        response.close()
                        links=re.compile("file': '(.+?)'").findall(link)
                        if len(links) > 0:
                                vid = links[0]
                                if 'uploadcrazy' in url:
                                        hthumb = artwork + '/hosts/uploadcrazy.png'

                                if 'vidcrazy' in url:
                                        hthumb = artwork + '/hosts/vidcrazy.png'

                                if 'animeonair' in url:
                                        hthumb = artwork + '/hosts/vidboxone.png'
                                

                                try:
                                        main.addHDir(name,vid,'resolve',thumb,hthumb)
                                except:
                                        continue
                except:
                        continue
                        


