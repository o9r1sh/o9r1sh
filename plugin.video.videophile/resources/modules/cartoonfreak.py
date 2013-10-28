#Cartoon Freak Module by o9r1sh October 2013

import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmcaddon,sys,main,xbmc,os
import urlresolver

artwork = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.videophile/resources/artwork/', ''))
base_url = 'http://www.cartoonfreak.net'

def CARTOONS():
        INDEX(base_url + '/cartoon/')

def ANIME():
        main.addDir('Anime Series','none','cartoonFreakAnimeSeries',artwork + '/main/tv.png')
        main.addDir('Anime Movies','none','cartoonFreakAnimeMovies',artwork + '/main/movie.png')

def ANIMESERIES():
        main.addDir('All', base_url + '/anime/','cartoonFreakIndex',artwork + '/main/all.png')
        main.addDir('A', base_url + '/anime/?alpha=a','cartoonFreakIndex',artwork + '/letters/a.png')
        main.addDir('B', base_url + '/anime/?alpha=b','cartoonFreakIndex',artwork + '/letters/b.png')
        main.addDir('C', base_url + '/anime/?alpha=c','cartoonFreakIndex',artwork + '/letters/c.png')
        main.addDir('D', base_url + '/anime/?alpha=d','cartoonFreakIndex',artwork + '/letters/d.png')
        main.addDir('E', base_url + '/anime/?alpha=e','cartoonFreakIndex',artwork + '/letters/e.png')
        main.addDir('F', base_url + '/anime/?alpha=f','cartoonFreakIndex',artwork + '/letters/f.png')
        main.addDir('G', base_url + '/anime/?alpha=g','cartoonFreakIndex',artwork + '/letters/g.png')
        main.addDir('H', base_url + '/anime/?alpha=h','cartoonFreakIndex',artwork + '/letters/h.png')
        main.addDir('I', base_url + '/anime/?alpha=i','cartoonFreakIndex',artwork + '/letters/i.png')
        main.addDir('J', base_url + '/anime/?alpha=j','cartoonFreakIndex',artwork + '/letters/j.png')
        main.addDir('K', base_url + '/anime/?alpha=k','cartoonFreakIndex',artwork + '/letters/k.png')
        main.addDir('L', base_url + '/anime/?alpha=l','cartoonFreakIndex',artwork + '/letters/l.png')
        main.addDir('M', base_url + '/anime/?alpha=m','cartoonFreakIndex',artwork + '/letters/m.png')
        main.addDir('N', base_url + '/anime/?alpha=n','cartoonFreakIndex',artwork + '/letters/n.png')
        main.addDir('O', base_url + '/anime/?alpha=o','cartoonFreakIndex',artwork + '/letters/o.png')
        main.addDir('P', base_url + '/anime/?alpha=p','cartoonFreakIndex',artwork + '/letters/p.png')
        main.addDir('Q', base_url + '/anime/?alpha=q','cartoonFreakIndex',artwork + '/letters/q.png')
        main.addDir('R', base_url + '/anime/?alpha=r','cartoonFreakIndex',artwork + '/letters/r.png')
        main.addDir('S', base_url + '/anime/?alpha=s','cartoonFreakIndex',artwork + '/letters/s.png')
        main.addDir('T', base_url + '/anime/?alpha=t','cartoonFreakIndex',artwork + '/letters/t.png')
        main.addDir('U', base_url + '/anime/?alpha=u','cartoonFreakIndex',artwork + '/letters/u.png')
        main.addDir('V', base_url + '/anime/?alpha=v','cartoonFreakIndex',artwork + '/letters/v.png')
        main.addDir('W', base_url + '/anime/?alpha=w','cartoonFreakIndex',artwork + '/letters/w.png')
        main.addDir('X', base_url + '/anime/?alpha=x','cartoonFreakIndex',artwork + '/letters/x.png')
        main.addDir('Y', base_url + '/anime/?alpha=y','cartoonFreakIndex',artwork + '/letters/y.png')
        main.addDir('Z', base_url + '/anime/?alpha=z','cartoonFreakIndex',artwork + '/letters/z.png')


def ANIMEMOVIES():
        main.addDir('All', base_url + '/movie/','cartoonFreakMovieIndex',artwork + '/main/a.png')
        main.addDir('A', base_url + '/movie/?alpha=a','cartoonFreakMovieIndex',artwork + '/letters/a.png')
        main.addDir('B', base_url + '/movie/?alpha=b','cartoonFreakMovieIndex',artwork + '/letters/b.png')
        main.addDir('C', base_url + '/movie/?alpha=c','cartoonFreakMovieIndex',artwork + '/letters/c.png')
        main.addDir('D', base_url + '/movie/?alpha=d','cartoonFreakMovieIndex',artwork + '/letters/d.png')
        main.addDir('E', base_url + '/movie/?alpha=e','cartoonFreakMovieIndex',artwork + '/letters/e.png')
        main.addDir('F', base_url + '/movie/?alpha=f','cartoonFreakMovieIndex',artwork + '/letters/f.png')
        main.addDir('G', base_url + '/movie/?alpha=g','cartoonFreakMovieIndex',artwork + '/letters/g.png')
        main.addDir('H', base_url + '/movie/?alpha=h','cartoonFreakMovieIndex',artwork + '/letters/h.png')
        main.addDir('I', base_url + '/movie/?alpha=i','cartoonFreakMovieIndex',artwork + '/letters/i.png')
        main.addDir('J', base_url + '/movie/?alpha=j','cartoonFreakMovieIndex',artwork + '/letters/j.png')
        main.addDir('K', base_url + '/movie/?alpha=k','cartoonFreakMovieIndex',artwork + '/letters/k.png')
        main.addDir('L', base_url + '/movie/?alpha=l','cartoonFreakMovieIndex',artwork + '/letters/l.png')
        main.addDir('M', base_url + '/movie/?alpha=m','cartoonFreakMovieIndex',artwork + '/letters/m.png')
        main.addDir('N', base_url + '/movie/?alpha=n','cartoonFreakMovieIndex',artwork + '/letters/n.png')
        main.addDir('O', base_url + '/movie/?alpha=o','cartoonFreakMovieIndex',artwork + '/letters/o.png')
        main.addDir('P', base_url + '/movie/?alpha=p','cartoonFreakMovieIndex',artwork + '/letters/p.png')
        main.addDir('Q', base_url + '/movie/?alpha=q','cartoonFreakMovieIndex',artwork + '/letters/q.png')
        main.addDir('R', base_url + '/movie/?alpha=r','cartoonFreakMovieIndex',artwork + '/letters/r.png')
        main.addDir('S', base_url + '/movie/?alpha=s','cartoonFreakMovieIndex',artwork + '/letters/s.png')
        main.addDir('T', base_url + '/movie/?alpha=t','cartoonFreakMovieIndex',artwork + '/letters/t.png')
        main.addDir('U', base_url + '/movie/?alpha=u','cartoonFreakMovieIndex',artwork + '/letters/u.png')
        main.addDir('V', base_url + '/movie/?alpha=v','cartoonFreakMovieIndex',artwork + '/letters/v.png')
        main.addDir('W', base_url + '/movie/?alpha=w','cartoonFreakMovieIndex',artwork + '/letters/w.png')
        main.addDir('X', base_url + '/movie/?alpha=x','cartoonFreakMovieIndex',artwork + '/letters/x.png')
        main.addDir('Y', base_url + '/movie/?alpha=y','cartoonFreakMovieIndex',artwork + '/letters/y.png')
        main.addDir('Z', base_url + '/movie/?alpha=Z','cartoonFreakMovieIndex',artwork + '/letters/z.png')
    
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
                        


