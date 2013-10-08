#WeWatchMoviesFree Module by o9r1sh October 2013

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
base_url = 'http://www.wewatchmoviesfree.net/'

def CATEGORIES():
        main.addDir('Recently Added',base_url,39,artwork + 'recentlyadded.png')
        main.addDir('A-Z','none',40,artwork + 'a-z.png')
        main.addDir('Genres','none',41,artwork + 'genres.png')
        main.addDir('Search','none',42,artwork + 'search.png')

def LETTERS():
        main.addDir('A',base_url + '/category/a',39,artwork + 'a.png')
        main.addDir('B',base_url + '/category/b',39,artwork + 'b.png')
        main.addDir('C',base_url + '/category/c',39,artwork + 'c.png')
        main.addDir('D',base_url + '/category/d',39,artwork + 'd.png')
        main.addDir('E',base_url + '/category/e',39,artwork + 'e.png')
        main.addDir('F',base_url + '/category/f',39,artwork + 'f.png')
        main.addDir('G',base_url + '/category/g',39,artwork + 'g.png')
        main.addDir('H',base_url + '/category/h',39,artwork + 'h.png')
        main.addDir('I',base_url + '/category/i',39,artwork + 'i.png')
        main.addDir('J',base_url + '/category/j',39,artwork + 'j.png')
        main.addDir('K',base_url + '/category/k',39,artwork + 'k.png')
        main.addDir('L',base_url + '/category/l',39,artwork + 'l.png')
        main.addDir('M',base_url + '/category/m',39,artwork + 'm.png')
        main.addDir('N',base_url + '/category/n',39,artwork + 'n.png')
        main.addDir('O',base_url + '/category/o',39,artwork + 'o.png')
        main.addDir('P',base_url + '/category/p',39,artwork + 'p.png')
        main.addDir('Q',base_url + '/category/q',39,artwork + 'q.png')
        main.addDir('R',base_url + '/category/r',39,artwork + 'r.png')
        main.addDir('S',base_url + '/category/s',39,artwork + 's.png')
        main.addDir('T',base_url + '/category/t',39,artwork + 't.png')
        main.addDir('U',base_url + '/category/u',39,artwork + 'u.png')
        main.addDir('V',base_url + '/category/v',39,artwork + 'v.png')
        main.addDir('W',base_url + '/category/w',39,artwork + 'w.png')
        main.addDir('X',base_url + '/category/x',39,artwork + 'x.png')
        main.addDir('Y',base_url + '/category/y',39,artwork + 'y.png')
        main.addDir('Z',base_url + '/category/z',39,artwork + 'z.png')

def GENRES():
        main.addDir('Action',base_url + '/category/action',39,artwork + 'action.png')
        main.addDir('Adventure',base_url + '/category/adventure',39,artwork + 'adventure.png')
        main.addDir('Animation',base_url + '/category/animation',39,artwork + 'animation.png')
        main.addDir('Biography',base_url + '/category/biography',39,artwork + 'biography.png')
        main.addDir('Bollywood',base_url + '/category/bollywood',39,artwork + 'bollywood.png')
        main.addDir('Comedy',base_url + '/category/comedy',39,artwork + 'comedy.png')
        main.addDir('Crime',base_url + '/category/crime',39,artwork + 'crime.png')
        main.addDir('Documentary',base_url + '/category/documentary',39,artwork + 'docsg.png')
        main.addDir('Drama',base_url + '/category/drama',39,artwork + 'drama.png')
        main.addDir('Family',base_url + '/category/family',39,artwork + 'family.png')
        main.addDir('Fantasy',base_url + '/category/fantasy',39,artwork + 'fantasy.png')
        main.addDir('Film-Noir',base_url + '/category/general',39,artwork + 'film-noir.png')
        main.addDir('History',base_url + '/category/history',39,artwork + 'historyg.png')
        main.addDir('Horror',base_url + '/category/horror',39,artwork + 'horror.png')
        main.addDir('Musical',base_url + '/category/musical',39,artwork + 'musical.png')
        main.addDir('Mystery',base_url + '/category/mystery',39,artwork + 'mystery.png')
        main.addDir('Reality TV',base_url + '/category/reality-tv',39,artwork + 'reality.png')
        main.addDir('Romance',base_url + '/category/romance',39,artwork + 'romance.png')
        main.addDir('Sci-Fi',base_url + '/category/sci-fi',39,artwork + 'sci-fi.png')
        main.addDir('Short',base_url + '/category/short',39,artwork + 'short.png')
        main.addDir('Sports',base_url + '/category/sport',39,artwork + 'sport.png')
        main.addDir('Thriller',base_url + '/category/thriller',39,artwork + 'thriller.png')
        main.addDir('War',base_url + '/category/war',39,artwork + 'war.png')
        main.addDir('Western',base_url + '/category/western',39,artwork + 'western.png')

def INDEX(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('<a\nhref="(.+?)" rel=".+?" > <img\nclass=".+?" src="(.+?)" width=".+?" height=".+?" title="Watch (.+?) Online Free" >').findall(link)
        np=re.compile("rel='next' href='(.+?)' /><link").findall(link)
        if len(np) > 0:
                next_page = np[0]
                main.addDir('Next Page',next_page,39,artwork + 'next.png')
        
        for url,thumbnail,name in match:
                try:
                        main.addMDir(name,url,43,thumbnail,year)
                except:
                        continue
        main.AUTOVIEW('movies')

def VIDEOLINKS(name,url,thumb):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('<a\nhref="(.+?)" class="ext-link"').findall(link)
        for url in match:
                head,sep,tail = url.partition('=')
                print'llllllllllllllllllll' + tail
                hmf = urlresolver.HostedMediaFile(tail)
                if hmf:
                        host = hmf.get_host()
                        hthumb = main.GETHOSTTHUMB(host)
                        try:
                                main.addHDir(name,tail,9,thumb,hthumb)
                        except:
                                continue

def SEARCH():
        search = ''
        keyboard = xbmc.Keyboard(search,'Search')
        keyboard.doModal()
        if keyboard.isConfirmed():
                search = keyboard.getText()
                search = search.replace(' ','+')
                
                url = base_url + '/?s=' + search 
                
                INDEX(url)

