#WatchSeriesOnline module by o9r1sh

import urllib,urllib2,re,xbmcplugin,xbmcgui,sys,main,urlresolver,xbmc,os

artwork = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.videophile/resources/artwork/', ''))
base_url = 'http://www.watchseries-online.eu'

def CATEGORIES():
        main.addDir('A-Z','none',44,artwork + '/main/a-z.png')
        main.addDir('Latest Episodes',base_url + '/2009/10/recent-episodes.html',46,artwork + '/main/recentlyadded.png')
        main.addDir('Search','none',15,artwork + '/main/search.png')

def LETTERS():
        main.addDir("#",base_url + "/2005/07/index.html#goto_'",12,artwork + '/letters/num.png')
        main.addDir("A",base_url + "/2005/07/index.html#goto_A",12,artwork + '/letters/a.png')
        main.addDir("B",base_url + "/2005/07/index.html#goto_B",12,artwork + '/letters/b.png')
        main.addDir("C",base_url + "/2005/07/index.html#goto_C",12,artwork + '/letters/c.png')
        main.addDir("D",base_url + "/2005/07/index.html#goto_D",12,artwork + '/letters/d.png')
        main.addDir("E",base_url + "/2005/07/index.html#goto_E",12,artwork + '/letters/e.png')
        main.addDir("F",base_url + "/2005/07/index.html#goto_F",12,artwork + '/letters/f.png')
        main.addDir("G",base_url + "/2005/07/index.html#goto_G",12,artwork + '/letters/g.png')
        main.addDir("H",base_url + "/2005/07/index.html#goto_H",12,artwork + '/letters/h.png')
        main.addDir("I",base_url + "/2005/07/index.html#goto_I",12,artwork + '/letters/i.png')
        main.addDir("J",base_url + "/2005/07/index.html#goto_J",12,artwork + '/letters/j.png')
        main.addDir("K",base_url + "/2005/07/index.html#goto_K",12,artwork + '/letters/k.png')
        main.addDir("L",base_url + "/2005/07/index.html#goto_L",12,artwork + '/letters/l.png')
        main.addDir("M",base_url + "/2005/07/index.html#goto_M",12,artwork + '/letters/m.png')
        main.addDir("N",base_url + "/2005/07/index.html#goto_N",12,artwork + '/letters/n.png')
        main.addDir("O",base_url + "/2005/07/index.html#goto_O",12,artwork + '/letters/o.png')
        main.addDir("P",base_url + "/2005/07/index.html#goto_P",12,artwork + '/letters/p.png')
        main.addDir("Q",base_url + "/2005/07/index.html#goto_Q",12,artwork + '/letters/q.png')
        main.addDir("R",base_url + "/2005/07/index.html#goto_R",12,artwork + '/letters/r.png')
        main.addDir("S",base_url + "/2005/07/index.html#goto_S",12,artwork + '/letters/s.png')
        main.addDir("T",base_url + "/2005/07/index.html#goto_T",12,artwork + '/letters/t.png')
        main.addDir("U",base_url + "/2005/07/index.html#goto_U",12,artwork + '/letters/u.png')
        main.addDir("V",base_url + "/2005/07/index.html#goto_V",12,artwork + '/letters/v.png')
        main.addDir("W",base_url + "/2005/07/index.html#goto_W",12,artwork + '/letters/w.png')
        main.addDir("X",base_url + "/2005/07/index.html#goto_X",12,artwork + '/letters/x.png')
        main.addDir("Y",base_url + "/2005/07/index.html#goto_Y",12,artwork + '/letters/y.png')
        main.addDir("Z",base_url + "/2005/07/index.html#goto_Z",12,artwork + '/letters/z.png')
                       
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
                                                main.addSDir(name,url,13,'')

                                elif az == "B":
                                          if letter == 'B':
                                                  main.addSDir(name,url,13,'')

                                elif az == "C":
                                          if letter == 'C':
                                                  main.addSDir(name,url,13,'')

                                elif az == "D":
                                          if letter == 'D':
                                                  main.addSDir(name,url,13,'')

                                elif az == "E":
                                          if letter == 'E':
                                                  main.addSDir(name,url,13,'')

                                elif az == "F":
                                          if letter == 'F':
                                                  main.addSDir(name,url,13,'')

                                elif az == "G":
                                          if letter == 'G':
                                                  main.addSDir(name,url,13,'')

                                elif az == "H":
                                          if letter == 'H':
                                                  main.addSDir(name,url,13,'')

                                elif az == "I":
                                          if letter == 'J':
                                                  main.addSDir(name,url,13,'')

                                elif az == "K":
                                          if letter == 'K':
                                                  main.addSDir(name,url,13,'')

                                elif az == "L":
                                          if letter == 'L':
                                                  main.addSDir(name,url,13,'')

                                elif az == "M":
                                          if letter == 'M':
                                                  main.addSDir(name,url,13,'')

                                elif az == "N":
                                          if letter == 'N':
                                                  main.addSDir(name,url,13,'')

                                elif az == "O":
                                          if letter == 'O':
                                                  main.addSDir(name,url,13,'')

                                elif az == "P":
                                          if letter == 'P':
                                                  main.addSDir(name,url,13,'')

                                elif az == "Q":
                                          if letter == 'Q':
                                                  main.addSDir(name,url,13,'')

                                elif az == "R":
                                          if letter == 'R':
                                                  main.addSDir(name,url,13,'')

                                elif az == "S":
                                          if letter == 'S':
                                                  main.addSDir(name,url,13,'')

                                elif az == "T":
                                          if letter == 'T':
                                                  main.addSDir(name,url,13,'')

                                elif az == "U":
                                          if letter == 'U':
                                                  main.addSDir(name,url,13,'')

                                elif az == "V":
                                          if letter == 'V':
                                                  main.addSDir(name,url,13,'')

                                elif az == "W":
                                          if letter == 'W':
                                                  main.addSDir(name,url,13,'')

                                elif az == "X":
                                          if letter == 'X':
                                                  main.addSDir(name,url,13,'')

                                elif az == "Y":
                                          if letter == 'Y':
                                                  main.addSDir(name,url,13,'')

                                elif az == "Z":
                                          if letter == 'Z':
                                                  main.addSDir(name,url,13,'')

                                elif az == "'":
                                        if letter.isdigit():
                                                main.addSDir(name,url,13,'')
                                 
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
                                try:
                                        main.addDir(name,url,14,'')
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
        thumb = main.GET_SHOW_THUMB(show_name)
        if len(np) > 0:
                np_url = np[0]
                main.addDir('Next Page',np_url,13,artwork + '/main/next.png')

        for url,name in match:
                name = re.sub('&#215;','X',name)
                
                try:
                        main.addEDir(name,url,14,thumb,show_name)
                except:
                        continue

        main.AUTOVIEW('episodes')

def VIDEOLINKS(url,name,thumb):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('<a target=".+?" id=".+?" href="(.+?)">(.+?)</a>').findall(link)
        inc = 0
        for url,host in match:
                dirty_url = match[inc][0]
                trash, sep,desired = dirty_url.partition('=')
                inc+=1
                cleaned_url = ''
                grabbed = desired
                if 'novamov' in host:
                        trash,sep,desired = grabbed.partition('/video/')
                        cleaned_url = 'http://www.novamov.com' + sep + desired

                elif 'videoweed' in host:
                        trash,sep,desired = grabbed.partition('/file/')
                        cleaned_url = 'http://www.videoweed.es' + sep + desired

                elif 'divxstage' in host:
                        trash,sep,desired = grabbed.partition('/video/')
                        cleaned_url = 'http://www.divxstage.eu' + sep + desired

                elif 'movshare' in host:
                        trash,sep,desired = grabbed.partition('/video/')
                        cleaned_url = 'http://www.movshare.net' + sep + desired

                elif 'nowvideo' in host:
                        trash,sep,desired = grabbed.partition('/video/')
                        cleaned_url = 'http://www.nowvideo.eu' + sep + desired

                #elif 'vidxden' in host:
                #        cleaned_url = grabbed

                #elif 'vidbux' in host:
                #        cleaned_url = grabbed

                elif 'allmyvideos' in host:
                        trash,sep,desired = grabbed.partition('.net/')
                        cleaned_url = 'http://www.allmyvideos' + sep + desired

                elif 'muchshare' in host:
                        trash,sep,desired = grabbed.partition('.net/')
                        cleaned_url = 'http://www.allmyvideos' + sep + desired

                elif 'flashx' in host:
                        trash,sep,desired = grabbed.partition('/video/')
                        cleaned_url = 'http://www.flashx.tv' + sep + desired

                elif 'movreel' in host:
                        trash,sep,desired = grabbed.partition('.com/')
                        cleaned_url = 'http://www.movreel' + sep + desired

                elif '180upload' in host:
                        trash,sep,desired = grabbed.partition('.com/')
                        cleaned_url = 'http://www.180upload' + sep + desired

                elif 'billionuploads' in host:
                        trash,sep,desired = grabbed.partition('.com/')
                        cleaned_url = 'http://www.billionuploads' + sep + desired

                elif 'vidbull' in host:
                        trash,sep,desired = grabbed.partition('.com/')
                        cleaned_url = 'http://www.vidbull' + sep + desired

                elif 'movzap' in host:
                        trash,sep,desired = grabbed.partition('.com/')
                        cleaned_url = 'http://www.movzap' + sep + desired

                elif 'videozed' in host:
                        trash,sep,desired = grabbed.partition('.net/')
                        cleaned_url = 'http://www.videozed' + sep + desired

                elif 'putlocker' in host:
                        trash,sep,desired = grabbed.partition('/file/')
                        cleaned_url = 'http://www.putlocker.com' + sep + desired

                elif 'sockshare' in host:
                        trash,sep,desired = grabbed.partition('/file/')
                        cleaned_url = 'http://www.sockshare.com' + sep + desired

                elif 'filebox' in host:
                        trash,sep,desired = grabbed.partition('.com/')
                        cleaned_url = 'http://www.filebox' + sep + desired

                elif 'cyberlocker' in host:
                        trash,sep,desired = grabbed.partition('.ch/')
                        cleaned_url = 'http://www.cyberlocker' + sep + desired
                        
                else:
                        continue

                if cleaned_url == '':
                        continue
                else:
                        hmf = urlresolver.HostedMediaFile(cleaned_url)
                        if hmf:
                                host = hmf.get_host()
                                hthumb = main.GETHOSTTHUMB(host)
                                try:
                                        print main.thumb
                                        main.addHDir(name,hmf.get_url(),9,thumb,hthumb)
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
                        main.addDir(name,url,14,'')
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


                


