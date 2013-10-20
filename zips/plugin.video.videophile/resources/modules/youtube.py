#Youtube documentary module by o9r1sh

import urllib,urllib2,re,xbmcplugin,xbmcgui,sys,main,urlresolver,xbmc,os

artwork = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.videophile/resources/artwork/', ''))
base_url = 'http://www.youtube.com'

def INDEX(url):
        inc = 0
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        np=re.compile('<a href="(.+?)" class="yt-uix-button  yt-uix-pager-button yt-uix-sessionlink yt-uix-button-default yt-uix-button-size-default" data-sessionlink="ei=.+?" data-page=".+?"><span class="yt-uix-button-content">Next \xc2\xbb </span></a>').findall(link)
        if len(np) > 0:
                next_page = base_url + np[0]
                main.addDir('Next Page',next_page,16,artwork + '/main/next.png')
        match=re.compile('data-context-item-title="(.+?)"').findall(link)
        times=re.compile('data-context-item-time="(.+?)"').findall(link)
        ids=re.compile('data-context-item-id="(.+?)"').findall(link)
        thumbs=re.compile('<img alt=".+?" src="(.+?)" width=".+?" >').findall(link)
        thumb = ''
        for name in match:
                try:
                        name = match[inc]
                except:
                        name = ''
                try:
                        time = times[inc]
                        time = time[:5]
                        time = time[:-3]
                except:
                        time = 0
                try:
                        vid = ids[inc]
                except:
                        vid = ''
                #try:
                        #thumb = 'http:' + thumbs[inc]
                        #thumb = thumb[2:]
                #except:
                        #thumb = ''

                url = base_url + '/watch?v=' + vid
                if name != '__title__':
                        if time > 22:
                                try:
                                        main.addDir(name,url,9,thumb)
                                except:
                                        continue
                
                inc += 1



