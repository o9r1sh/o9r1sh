#FreeMoviesAddict Module by o9r1sh September 2013

import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmcaddon,sys,main,xbmc,os,mechanize
import urlresolver

artwork = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.videophile/resources/artwork/', ''))
base_url = 'http://www.freeomovie.com'

def CATEGORIES():
        main.addDir('Recent Videos',base_url,'freeOMovieIndex',artwork + '/main/recentlyadded.png')
        main.addDir('Full Movies',base_url,'freeOMovieIndex',artwork + '/main/movie.png')
        main.addDir('Categories','none','freeOMovieGenres',artwork + '/main/categories.png')
        
def GENRES():
        main.addDir('All Girl',base_url + '/category/all-girl/','freeOMovieIndex',artwork + '/adult/allgirl.png')
        main.addDir('All Sex',base_url + '/category/all-sex/','freeOMovieIndex',artwork + '/adult/allsex.png')
        main.addDir('Amateur',base_url + '/category/amateur/','freeOMovieIndex',artwork + '/adult/amateur.png')
        main.addDir('Anal',base_url + '/category/anal/','freeOMovieIndex',artwork + '/adult/anal.png')
        main.addDir('Anime / Cartoon',base_url + '/category/animecartoon/','freeOMovieIndex',artwork + '/adult/anime.png')
        main.addDir('Asian',base_url + '/category/asian/','freeOMovieIndex',artwork + '/adult/asian.png')
        main.addDir('Big Butts',base_url + '/category/big-butts/','freeOMovieIndex',artwork + '/adult/bigbutts.png')
        main.addDir('Big Dicks',base_url + '/category/big-dicks/','freeOMovieIndex',artwork + '/adult/bigdicks.png')
        main.addDir('Big Tits',base_url + '/category/big-tits/','freeOMovieIndex',artwork + '/adult/bigtits.png')
        main.addDir('Black',base_url + '/category/black/','freeOMovieIndex',artwork + '/adult/black.png')
        main.addDir('Blow Job',base_url + '/category/blowjob/','freeOMovieIndex',artwork + '/adult/blowjob.png')
        main.addDir('Classic',base_url + '/category/classic/','freeOMovieIndex',artwork + '/adult/classic.png')
        main.addDir('Clips',base_url + '/category/clips/','freeOMovieIndex',artwork + '/adult/clips.png')
        main.addDir('Compilation',base_url + '/category/compilation/','freeOMovieIndex',artwork + '/adult/compilation.png')
        main.addDir('Couples',base_url + '/category/couples/','freeOMovieIndex',artwork + '/adult/couples.png')
        main.addDir('Cream Pie',base_url + '/category/cream-pie/','freeOMovieIndex',artwork + '/adult/creampie.png')
        main.addDir('Double Penetration',base_url + '/category/dp/','freeOMovieIndex',artwork + '/adult/doublepenetration.png')
        main.addDir('Feature',base_url + '/category/feature/','freeOMovieIndex',artwork + '/adult/feature.png')
        main.addDir('Fetish',base_url + '/category/fetish/','freeOMovieIndex',artwork + '/adult/fetish.png')
        main.addDir('Foreign',base_url + '/category/foreign/','freeOMovieIndex',artwork + '/adult/foreign.png')
        main.addDir('French',base_url + '/category/french/','freeOMovieIndex',artwork + '/adult/french.png')
        main.addDir('Full Movie',base_url + '/category/full-movie/','freeOMovieIndex',artwork + '/adult/fullmovie.png')
        main.addDir('Gang Bang',base_url + '/category/gang-bang/','freeOMovieIndex',artwork + '/adult/gangbang.png')
        main.addDir('German',base_url + '/category/german/','freeOMovieIndex',artwork + '/adult/german.png')
        main.addDir('Gonzo',base_url + '/category/gonzo/','freeOMovieIndex',artwork + '/adult/gonzo.png')
        main.addDir('Group Sex',base_url + '/category/group-sex/','freeOMovieIndex',artwork + '/adult/groupsex.png')
        main.addDir('Hardcore',base_url + '/category/hardcore/','freeOMovieIndex',artwork + '/adult/hardcore.png')
        main.addDir('Interracial',base_url + '/category/interracial/','freeOMovieIndex',artwork + '/adult/interracial.png')
        main.addDir('Italian',base_url + '/category/italian/','freeOMovieIndex',artwork + '/adult/italian.png')
        main.addDir('Lesbian',base_url + '/category/lesbian/','freeOMovieIndex',artwork + '/adult/lesbian.png')
        main.addDir('Mature',base_url + '/category/matureolder/','freeOMovieIndex',artwork + '/adult/mature.png')
        main.addDir('Milf',base_url + '/category/milf-cougar/','freeOMovieIndex',artwork + '/adult/milf.png')
        main.addDir('Parody',base_url + '/category/parody/','freeOMovieIndex',artwork + '/adult/parody.png')
        main.addDir('Plot Based',base_url + '/category/plot-based/','freeOMovieIndex',artwork + '/adult/plotbased.png')
        main.addDir('Star Power',base_url + '/category/star-power/','freeOMovieIndex',artwork + '/adult/starpower.png')
        main.addDir('Teen',base_url + '/category/teen/','freeOMovieIndex',artwork + '/adult/teen.png')

def INDEX(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('<a href="(.+?)" title=".+?">\r\n\r\n\t\t\t\t\t\t\t\t\t\r\n                                    <img src="(.+?)" alt="(.+?)" width=".+?" height=".+?" />').findall(link)
        np=re.compile("<link rel='next' href='(.+?)' />").findall(link)
        if len(np) > 0:
                np_url = np[0]
                main.addDir('Next Page',np_url,'freeOMovieIndex',artwork + '/main/next.png')
        for url,thumbnail,name in match:
                
                try:
                        main.addDir(name,url,'freeOMovieVideoLinks',thumbnail)
                except:
                        continue
                
        main.AUTOVIEW('movies')

def VIDEOLINKS(name,url,thumb):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('<a href="(.+?)" target="_blank">').findall(link)
        for url in match:
                if 'vidx.to' in url:
                        main.addHDir(name,url,'resolve',thumb,artwork + 'hosts/vidx.png')
                        
                else:
                        hmf = urlresolver.HostedMediaFile(url)
                        if hmf:
                                host = hmf.get_host()
                                hthumb = main.GETHOSTTHUMB(host)
                                try:
                                        main.addHDir(name,url,'resolve',thumb,hthumb)
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
