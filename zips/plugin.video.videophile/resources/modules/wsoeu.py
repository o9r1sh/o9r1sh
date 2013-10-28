#WatchSeriesOnline module by o9r1sh

import urllib,urllib2,re,xbmcplugin,xbmcgui,sys,main,urlresolver,xbmc,os

artwork = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.videophile/resources/artwork/', ''))
base_url = 'http://www.watchseries-online.eu'

def CATEGORIES():
        main.addDir('A-Z','none','watchSeriesOnlineLetters',artwork + '/main/a-z.png')
        main.addDir('Latest Episodes',base_url + '/2009/10/recent-episodes.html','watchSeriesOnlineRecentEpisodes',artwork + '/main/recentlyadded.png')
        main.addDir('Search','none','watchSeriesOnlineSearch',artwork + '/main/search.png')

def LETTERS():
        main.addDir("#",base_url + "/2005/07/index.html#goto_'",'watchSeriesOnlineSeriesIndex',artwork + '/letters/num.png')
        main.addDir("A",base_url + "/2005/07/index.html#goto_A",'watchSeriesOnlineSeriesIndex',artwork + '/letters/a.png')
        main.addDir("B",base_url + "/2005/07/index.html#goto_B",'watchSeriesOnlineSeriesIndex',artwork + '/letters/b.png')
        main.addDir("C",base_url + "/2005/07/index.html#goto_C",'watchSeriesOnlineSeriesIndex',artwork + '/letters/c.png')
        main.addDir("D",base_url + "/2005/07/index.html#goto_D",'watchSeriesOnlineSeriesIndex',artwork + '/letters/d.png')
        main.addDir("E",base_url + "/2005/07/index.html#goto_E",'watchSeriesOnlineSeriesIndex',artwork + '/letters/e.png')
        main.addDir("F",base_url + "/2005/07/index.html#goto_F",'watchSeriesOnlineSeriesIndex',artwork + '/letters/f.png')
        main.addDir("G",base_url + "/2005/07/index.html#goto_G",'watchSeriesOnlineSeriesIndex',artwork + '/letters/g.png')
        main.addDir("H",base_url + "/2005/07/index.html#goto_H",'watchSeriesOnlineSeriesIndex',artwork + '/letters/h.png')
        main.addDir("I",base_url + "/2005/07/index.html#goto_I",'watchSeriesOnlineSeriesIndex',artwork + '/letters/i.png')
        main.addDir("J",base_url + "/2005/07/index.html#goto_J",'watchSeriesOnlineSeriesIndex',artwork + '/letters/j.png')
        main.addDir("K",base_url + "/2005/07/index.html#goto_K",'watchSeriesOnlineSeriesIndex',artwork + '/letters/k.png')
        main.addDir("L",base_url + "/2005/07/index.html#goto_L",'watchSeriesOnlineSeriesIndex',artwork + '/letters/l.png')
        main.addDir("M",base_url + "/2005/07/index.html#goto_M",'watchSeriesOnlineSeriesIndex',artwork + '/letters/m.png')
        main.addDir("N",base_url + "/2005/07/index.html#goto_N",'watchSeriesOnlineSeriesIndex',artwork + '/letters/n.png')
        main.addDir("O",base_url + "/2005/07/index.html#goto_O",'watchSeriesOnlineSeriesIndex',artwork + '/letters/o.png')
        main.addDir("P",base_url + "/2005/07/index.html#goto_P",'watchSeriesOnlineSeriesIndex',artwork + '/letters/p.png')
        main.addDir("Q",base_url + "/2005/07/index.html#goto_Q",'watchSeriesOnlineSeriesIndex',artwork + '/letters/q.png')
        main.addDir("R",base_url + "/2005/07/index.html#goto_R",'watchSeriesOnlineSeriesIndex',artwork + '/letters/r.png')
        main.addDir("S",base_url + "/2005/07/index.html#goto_S",'watchSeriesOnlineSeriesIndex',artwork + '/letters/s.png')
        main.addDir("T",base_url + "/2005/07/index.html#goto_T",'watchSeriesOnlineSeriesIndex',artwork + '/letters/t.png')
        main.addDir("U",base_url + "/2005/07/index.html#goto_U",'watchSeriesOnlineSeriesIndex',artwork + '/letters/u.png')
        main.addDir("V",base_url + "/2005/07/index.html#goto_V",'watchSeriesOnlineSeriesIndex',artwork + '/letters/v.png')
        main.addDir("W",base_url + "/2005/07/index.html#goto_W",'watchSeriesOnlineSeriesIndex',artwork + '/letters/w.png')
        main.addDir("X",base_url + "/2005/07/index.html#goto_X",'watchSeriesOnlineSeriesIndex',artwork + '/letters/x.png')
        main.addDir("Y",base_url + "/2005/07/index.html#goto_Y",'watchSeriesOnlineSeriesIndex',artwork + '/letters/y.png')
        main.addDir("Z",base_url + "/2005/07/index.html#goto_Z",'watchSeriesOnlineSeriesIndex',artwork + '/letters/z.png')
                       
def INDEXSHOWS(url):
        az = url[-1:]
        letter = ''
        inc = 0
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('<a href="(.+?)">(.+?)</a>').findall(link)
           
        stop = len(match) - 5
        for url,name in match:
                letter = name[:1]
                inc += 1
                if 'season' in name or 'Season' in name:
                        continue
                if inc > 52:
                        if inc < stop:
                                if az == "A":
                                        if letter == 'A':
                                                main.addSDir(name,url,'watchSeriesOnlineEpisodesIndex','')

                                elif az == "B":
                                          if letter == 'B':
                                                  main.addSDir(name,url,'watchSeriesOnlineEpisodesIndex','')

                                elif az == "C":
                                          if letter == 'C':
                                                  main.addSDir(name,url,'watchSeriesOnlineEpisodesIndex','')

                                elif az == "D":
                                          if letter == 'D':
                                                  main.addSDir(name,url,'watchSeriesOnlineEpisodesIndex','')

                                elif az == "E":
                                          if letter == 'E':
                                                  main.addSDir(name,url,'watchSeriesOnlineEpisodesIndex','')

                                elif az == "F":
                                          if letter == 'F':
                                                  main.addSDir(name,url,'watchSeriesOnlineEpisodesIndex','')

                                elif az == "G":
                                          if letter == 'G':
                                                  main.addSDir(name,url,'watchSeriesOnlineEpisodesIndex','')

                                elif az == "H":
                                          if letter == 'H':
                                                  main.addSDir(name,url,'watchSeriesOnlineEpisodesIndex','')

                                elif az == "I":
                                          if letter == 'J':
                                                  main.addSDir(name,url,'watchSeriesOnlineEpisodesIndex','')

                                elif az == "K":
                                          if letter == 'K':
                                                  main.addSDir(name,url,'watchSeriesOnlineEpisodesIndex','')

                                elif az == "L":
                                          if letter == 'L':
                                                  main.addSDir(name,url,'watchSeriesOnlineEpisodesIndex','')

                                elif az == "M":
                                          if letter == 'M':
                                                  main.addSDir(name,url,'watchSeriesOnlineEpisodesIndex','')

                                elif az == "N":
                                          if letter == 'N':
                                                  main.addSDir(name,url,'watchSeriesOnlineEpisodesIndex','')

                                elif az == "O":
                                          if letter == 'O':
                                                  main.addSDir(name,url,'watchSeriesOnlineEpisodesIndex','')

                                elif az == "P":
                                          if letter == 'P':
                                                  main.addSDir(name,url,'watchSeriesOnlineEpisodesIndex','')

                                elif az == "Q":
                                          if letter == 'Q':
                                                  main.addSDir(name,url,'watchSeriesOnlineEpisodesIndex','')

                                elif az == "R":
                                          if letter == 'R':
                                                  main.addSDir(name,url,'watchSeriesOnlineEpisodesIndex','')

                                elif az == "S":
                                          if letter == 'S':
                                                  main.addSDir(name,url,'watchSeriesOnlineEpisodesIndex','')

                                elif az == "T":
                                          if letter == 'T':
                                                  main.addSDir(name,url,'watchSeriesOnlineEpisodesIndex','')

                                elif az == "U":
                                          if letter == 'U':
                                                  main.addSDir(name,url,'watchSeriesOnlineEpisodesIndex','')

                                elif az == "V":
                                          if letter == 'V':
                                                  main.addSDir(name,url,'watchSeriesOnlineEpisodesIndex','')

                                elif az == "W":
                                          if letter == 'W':
                                                  main.addSDir(name,url,'watchSeriesOnlineEpisodesIndex','')

                                elif az == "X":
                                          if letter == 'X':
                                                  main.addSDir(name,url,'watchSeriesOnlineEpisodesIndex','')

                                elif az == "Y":
                                          if letter == 'Y':
                                                  main.addSDir(name,url,'watchSeriesOnlineEpisodesIndex','')

                                elif az == "Z":
                                          if letter == 'Z':
                                                  main.addSDir(name,url,'watchSeriesOnlineEpisodesIndex','')

                                elif az == "'":
                                        if letter.isdigit():
                                                main.addSDir(name,url,'watchSeriesOnlineEpisodesIndex','')
                                 
        main.AUTOVIEW('tvshows')

def RECENTEPS(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('<a href="(.+?)">(.+?)</a>').findall(link)
        inc = 0
        for url,name in match:        
                inc += 1
                if inc > 25:
                        if name == 'TV':
                                continue
                        else:
                                show = re.split('[Ss]\d\d[Ee]\d\d',name)
                                try:
                                        main.addEDir(name,url,'watchSeriesOnlineVideoLinks','',show[0])
                                except:
                                        continue
        main.AUTOVIEW('episodes')

def INDEXEPS(url,name):
        thumb = ''
        show_name = name
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('<a href="(.+?)" rel=".+?" title=".+?">\n(.+?)\n</a>').findall(link)
        np=re.compile('</a></li><li><a href="(.+?)" class="next">').findall(link)
        if show_name == 'Next Page':
                real_show=re.compile('Episodes Available for: &#8216;(.+?)&#8217;').findall(link)
                if len(real_show) > 0:
                        show_name = real_show[0]
                        
        if len(np) > 0:
                np_url = np[0]
                main.addDir('Next Page',np_url,'watchSeriesOnlineEpisodesIndex',artwork + '/main/next.png')

        for url,name in match:
                name = re.sub('&#215;','X',name)
                
                try:
                        main.addEDir(name,url,'watchSeriesOnlineVideoLinks',thumb,show_name)
                except:
                        continue

        main.AUTOVIEW('episodes')

def VIDEOLINKS(url,name,thumb):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('<a target="_blank" id="hovered" href="(.+?)">.+?</a>').findall(link)
        for url in match:
                if 'fanstash' in url:
                        continue
                else:
                        try:
                                req = urllib2.Request(url)
                                req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                                response = urllib2.urlopen(req)
                                links=response.read()
                                response.close()
                                reallink=re.compile('<a class="myButton" href="(.+?)">Click Here to Play</a>').findall(links)
                                if len(reallink) > 0:
                                        file_link = reallink[0]

                        
                                        hmf = urlresolver.HostedMediaFile(str(file_link))
                                        if hmf:
                                                host = hmf.get_host()
                                                hthumb = main.GETHOSTTHUMB(host)
                                                try:
                                                        print main.thumb
                                                        main.addHDir(name,hmf.get_url(),'resolve',thumb,hthumb)
                                                except:
                                                        continue
                        except:
                                continue

def SEARCHINDEX(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('<a href="(.+?)" rel="bookmark" title=".+?">\n\t\t\t(.+?)\t\t\t</a>').findall(link)
        np=re.compile('<a href="(.+?)" class="next">&raquo;</a>').findall(link)
        if len(np) > 0:
                np_url = np[0]
                np_url = re.sub('#038;','',np_url)
                #main.addDir('Next Page',np_url,45,'')
        for url,name in match:
                name = re.sub('&#215;','X',name)
                try:
                        main.addDir(name,url,'watchSeriesOnlineEpisodesIndex','')
                except:
                        continue
                
def SEARCH():
        search = ''
        keyboard = xbmc.Keyboard(search,'Search')
        keyboard.doModal()
        if keyboard.isConfirmed():
                search = keyboard.getText()
                search = search.replace(' ','+')
                
                url = base_url + '/?s=' + search + '&search='
                print url
                
                SEARCHINDEX(url)


                


