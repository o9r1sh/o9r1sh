#ZMovie Module by o9r1sh October 2013

import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmcaddon,sys,main,xbmc,os
import urlresolver

addon_id = 'plugin.video.videophile'
from t0mm0.common.addon import Addon
addon = Addon(addon_id, sys.argv)

mode = addon.queries['mode']
url = addon.queries.get('url', '')
name = addon.queries.get('name', '')
thumb = addon.queries.get('thumb', '')
year = addon.queries.get('year', '')
types = addon.queries.get('types', '')

artwork = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.videophile/resources/artwork/', ''))
base_url = 'http://www2.zmovie.tw'

def CATEGORIES():
        main.addDir('New Releases',base_url + '/movies/new',32,artwork + 'newreleases.png')
        main.addDir('Featured',base_url + '/movies/featured',32,artwork + 'featured.png')
        main.addDir('Recently Added',base_url + '/movies/recent',32,artwork + 'recentlyadded.png')
        main.addDir('A-Z','none',33,artwork + 'a-z.png')
        main.addDir('Genres','none',34,artwork + 'genres.png')

def LETTERS():
        main.addDir('#',base_url + '/search/alpha/0-9',32,artwork + '#.png')
        main.addDir('A',base_url + '/search/alpha/A',32,artwork + 'a.png')
        main.addDir('B',base_url + '/search/alpha/B',32,artwork + 'b.png')
        main.addDir('C',base_url + '/search/alpha/C',32,artwork + 'c.png')
        main.addDir('D',base_url + '/search/alpha/D',32,artwork + 'd.png')
        main.addDir('E',base_url + '/search/alpha/E',32,artwork + 'e.png')
        main.addDir('F',base_url + '/search/alpha/F',32,artwork + 'f.png')
        main.addDir('G',base_url + '/search/alpha/G',32,artwork + 'g.png')
        main.addDir('H',base_url + '/search/alpha/H',32,artwork + 'h.png')
        main.addDir('I',base_url + '/search/alpha/I',32,artwork + 'i.png')
        main.addDir('J',base_url + '/search/alpha/J',32,artwork + 'j.png')
        main.addDir('K',base_url + '/search/alpha/K',32,artwork + 'k.png')
        main.addDir('L',base_url + '/search/alpha/L',32,artwork + 'l.png')
        main.addDir('M',base_url + '/search/alpha/M',32,artwork + 'm.png')
        main.addDir('N',base_url + '/search/alpha/N',32,artwork + 'n.png')
        main.addDir('O',base_url + '/search/alpha/O',32,artwork + 'o.png')
        main.addDir('P',base_url + '/search/alpha/P',32,artwork + 'p.png')
        main.addDir('Q',base_url + '/search/alpha/Q',32,artwork + 'q.png')
        main.addDir('R',base_url + '/search/alpha/R',32,artwork + 'r.png')
        main.addDir('S',base_url + '/search/alpha/S',32,artwork + 's.png')
        main.addDir('T',base_url + '/search/alpha/T',32,artwork + 't.png')
        main.addDir('U',base_url + '/search/alpha/U',32,artwork + 'u.png')
        main.addDir('V',base_url + '/search/alpha/V',32,artwork + 'v.png')
        main.addDir('W',base_url + '/search/alpha/W',32,artwork + 'w.png')
        main.addDir('X',base_url + '/search/alpha/X',32,artwork + 'x.png')
        main.addDir('Y',base_url + '/search/alpha/Y',32,artwork + 'y.png')
        main.addDir('Z',base_url + '/search/alpha/Z',32,artwork + 'z.png')

def GENRES():
        main.addDir('Action',base_url + '/search/genre/Action',32,artwork + 'action.png')
        main.addDir('Adventure',base_url + '/search/genre/Adventure',32,artwork + 'adventure.png')
        main.addDir('Animation',base_url + '/search/genre/Animation',32,artwork + 'animation.png')
        main.addDir('Biography',base_url + '/search/genre/Biography',32,artwork + 'biography.png')
        main.addDir('Comedy',base_url + '/search/genre/Comedy',32,artwork + 'comedy.png')
        main.addDir('Crime',base_url + '/search/genre/Crime',32,artwork + 'crime.png')
        main.addDir('Documentary',base_url + '/search/genre/Documentary',32,artwork + 'docsg.png')
        main.addDir('Drama',base_url + '/search/genre/Drama',32,artwork + 'drama.png')
        main.addDir('Family',base_url + '/search/genre/Family',32,artwork + 'family.png')
        main.addDir('Fantasy',base_url + '/search/genre/Fantasy',32,artwork + 'fantasy.png')
        main.addDir('Film-Noir',base_url + '/search/genre/Film-Noir',32,artwork + 'film-noir.png')
        main.addDir('History',base_url + '/search/genre/History',32,artwork + 'historyg.png')
        main.addDir('Hindi',base_url + '/search/genre/Hindi',32,artwork + 'hindi.png')
        main.addDir('Horror',base_url + '/search/genre/Horror',32,artwork + 'horror.png')
        main.addDir('Korean',base_url + '/search/genre/Korean',32,artwork + 'korean.png')
        main.addDir('Music',base_url + '/search/genre/Music',32,artwork + 'music.png')
        main.addDir('Musical',base_url + '/search/genre/Musical',32,artwork + 'musical.png')
        main.addDir('Mystery',base_url + '/search/genre/Mystery',32,artwork + 'mystery.png')
        main.addDir('News',base_url + '/search/genre/News',32,artwork + 'news.png')
        main.addDir('Reality',base_url + '/search/genre/Reality%20TV',32,artwork + 'reality.png')
        main.addDir('Romance',base_url + '/search/genre/Romance',32,artwork + 'romance.png')
        main.addDir('Sci-Fi',base_url + '/search/genre/Sci-Fi',32,artwork + 'sci-fi.png')
        main.addDir('Short',base_url + '/search/genre/Short',32,artwork + 'short.png')
        main.addDir('Sport',base_url + '/search/genre/Sport',32,artwork + 'sport.png')
        main.addDir('Talk Show',base_url + '/search/genre/Talk%20Show',32,artwork + 'talk.png')
        main.addDir('Thriller',base_url + '/search/genre/Thriller',32,artwork + 'thriller.png')
        main.addDir('War',base_url + '/search/genre/War',32,artwork + 'war.png')
        main.addDir('Western',base_url + '/search/genre/Western',32,artwork + 'western.png')

def INDEX(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('<a href="(.+?)" title="(.+?)"> <img src="(.+?)"  alt=".+?" height=".+?" width=".+?"/></a>').findall(link)
        np=re.compile("..</span> <a class=.+? href='(.+?)'> Next+").findall(link)
        if len(np) > 0:
                next_page = np[0]
                main.addDir('Next Page',next_page,32,artwork + 'next.png')
                                              
        for url,name,thumbnail in match:
                head, sep, tail = name.partition(')')
                name = head[:-5]
                year = head[-5:] + sep
                try:
                        main.addMDir(name,url,36,thumbnail,year)
                except:
                        continue
        main.AUTOVIEW('movies')

def VIDEOLINKS(name,url,thumb):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('class="atest" target="_blank"   href="(.+?) ">').findall(link)
        for url in match:
                hmf = urlresolver.HostedMediaFile(url)
                if hmf:
                        host = hmf.get_host()
                        hthumb = main.GETHOSTTHUMB(host)
                        try:
                                main.addHDir(name,url,9,thumb,hthumb)
                        except:
                                continue

def SEARCH():
        search = ''
        keyboard = xbmc.Keyboard(search,'Search')
        keyboard.doModal()
        if keyboard.isConfirmed():
                search = keyboard.getText()
                search = search.replace(' ','+')
                
                url = base_url + 'index.php?s=' + search 
                
                INDEX(url)

