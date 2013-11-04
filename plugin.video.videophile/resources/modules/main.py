# -*- coding: utf-8 -*-
#Main VideoPhile module by o9r1sh

#Imports_____________________________________________________________________________________________________________________________
import urllib,urllib2,re,xbmcplugin,xbmcgui,sys,urlresolver,xbmc,os,xbmcaddon,mechanize
from metahandler import metahandlers

from t0mm0.common.addon import Addon
from t0mm0.common.net import Net

try:
     import StorageServer
except:
     import storageserverdummy as StorageServer

import threading

class Thread(threading.Thread):
    def __init__(self, target, *args):
        self._target = target
        self._args = args
        threading.Thread.__init__(self)
    def run(self):
        self._target(*self._args)

#Define common.addon_____________________________________________________________________________________________________________________________
addon_id = 'plugin.video.videophile'
addon = Addon(addon_id, sys.argv)

#Define Cache for favorites_____________________________________________________________________________________________________________________________
cache = StorageServer.StorageServer("VideoPhile", 0)

#Define queries for common.addon_____________________________________________________________________________________________________________________________
mode = addon.queries['mode']
url = addon.queries.get('url', '')
name = addon.queries.get('name', '')
thumb = addon.queries.get('thumb', '')
year = addon.queries.get('year', '')
season = addon.queries.get('season', '')
episode = addon.queries.get('episode', '')
show = addon.queries.get('show', '')
types = addon.queries.get('types', '')
fanart = addon.queries.get('fanart', '')
rmode = addon.queries.get('rmode', '')
imdb_id = addon.queries.get('imdb_id', '')

#Define other needed global variables_____________________________________________________________________________________________________________________________
settings = xbmcaddon.Addon(id=addon_id)
artwork = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.videophile/resources/artwork/', ''))
grab=metahandlers.MetaData()
net = Net()

def resolvable(url):
     resolvable = False
     hmf = urlresolver.HostedMediaFile(url)
     if hmf:
          resolvable = True

     if 'uploadcrazy' in url:
          resolvable = True

     if 'vidcrazy' in url:
          resolvable = True

     if 'vidx.to' in url:
          resolvable = True

     if 'epornik' in url:
          resolvable = True

     if 'video44' in url:
          resolvable = True

     if 'play44' in url:
          resolvable = True

     if 'cheesestream' in url:
          resolvable = True

     return(resolvable)

def getHost(url):
     host = None
     hmf = urlresolver.HostedMediaFile(url)
     if hmf:
          host = hmf.get_host()
          print 'ssssssss'+host

     if 'uploadcrazy' in url:
          host = 'uploadcrazy'

     if 'vidcrazy' in url:
          host = 'vidcrazy'

     if 'vidx.to' in url:
          host = 'vidx'

     if 'epornik' in url:
          host = 'epornik'

     if 'video44' in url:
          host = 'video44'

     if 'play44' in url:
          host = 'play44'

     if 'cheesestream' in url:
          host = 'cheesestream'
     
     return(host)
          
#Functions for handling favorites_____________________________________________________________________________________________________________________________
def addFavorite():
     saved_favs = cache.get('favourites_' + types)
     favs = []
     if saved_favs:
          favs = eval(saved_favs)
          if favs:
               if (name, url ,rmode, thumb, show, year, season, episode) in favs:
                    addon.show_small_popup(title='Item Already In Favorites', msg=name + ' Is Already In Your Favorites', delay=int(5000), image=thumb)
                    return
     favs.append((name, url ,rmode, thumb, show, year, season, episode))         
     cache.set('favourites_' + types, str(favs))
     addon.show_small_popup(title='Item Added To Favorites', msg=name + ' Was Added To Your Favorites', delay=int(5000), image=thumb)

def removeFavorite():
    saved_favs = cache.get('favourites_' + types)
    if saved_favs:
        favs = eval(saved_favs)
        favs.remove((name, url ,rmode, thumb, show, year, season, episode))   
        cache.set('favourites_' + types, str(favs))
        xbmc.executebuiltin("XBMC.Container.Refresh")

def getFavorites(url):
     if url == 'movie':
          saved_favs = cache.get('favourites_' + 'movie')
          if saved_favs:
               favs = sorted(eval(saved_favs), key=lambda fav: fav[1])
               for fav in favs:
                         addMDir(fav[0], fav[1] ,fav[2], fav[3], fav[4], True)
          AUTOVIEW('movies')

     elif url == 'tvshow':
          saved_favs = cache.get('favourites_' + 'tvshow')
          if saved_favs:
               favs = sorted(eval(saved_favs), key=lambda fav: fav[1])
               for fav in favs:
                         addSDir(fav[0], fav[1] ,fav[2], fav[3], True)
                    
          AUTOVIEW('tvshows')

     elif url == 'cartoon':
          saved_favs = cache.get('favourites_' + 'cartoon')
          if saved_favs:
               favs = sorted(eval(saved_favs), key=lambda fav: fav[1])
               for fav in favs:
                         addToonDir(fav[0], fav[1] ,fav[2], fav[3], True)
                    
          AUTOVIEW('tvshows')

     elif url == 'anime':
          saved_favs = cache.get('favourites_' + 'anime')
          if saved_favs:
               favs = sorted(eval(saved_favs), key=lambda fav: fav[1])
               for fav in favs:
                         addAnimeDir(fav[0], fav[1] ,fav[2], fav[3], True)
                    
          AUTOVIEW('tvshows')

#Metadata Function_____________________________________________________________________________________________________________________________     
def getMeta(types,name,year,show,season,episode):
     show_meta = 0
     meta = 0
     if types=='movie':
          meta = grab.get_meta('movie',name,year)
     elif types=='tvshow':
          meta = grab.get_meta('tvshow',name)
     elif types=='episode':
          try:
               show_meta = grab.get_meta('tvshow',show)
          except:
               show_meta = 0
          if show_meta == 0:
               return 0
          else:
               imdb_id = show_meta['imdb_id']
               meta = grab.get_episode_meta(show,imdb_id,season,episode)
     return(meta)

#Directory Functions_____________________________________________________________________________________________________________________________

#Standard directory funtion to be used when not doing scrapes on the directory_____________________________________________________________________________________________________________________________
def addDir(name,url,mode,thumb):
     if thumb == '':
          thumb = artwork + '/main/noepisode.png'
     params = {'url':url, 'mode':mode, 'name':name, 'thumb':thumb, 'year':year, 'types':'movie'}
     addon.add_directory(params, {'title':name}, img= thumb, fanart= artwork + '/main/fanart.jpg')

#Movie directory function to be used when adding a movie, all metadata scrapes and context menu items are handled within_____________________________________________________________________________________________________________________________
def addMDir(name,url,mode,thumb,year,isfav):
     meta = {}
     contextMenuItems = []

     title = re.split('\d\d\d\d',name)

     if title[0] == '':
          title = name
     if settings.getSetting('metadata') == 'true':
          meta = getMeta('movie',title[0],year,'','','')
     year = re.sub('[()]','',year)
     if year == '':
          try:
               year = meta['year']
          except:
               year = ''
     if year == 0:
          year = ''
     if settings.getSetting('metadata') == 'true':

          if year == '':
               meta['title'] = name

          else:
               meta['title'] = name + ' ' + '(' + str(year) + ')'
     
          if thumb == '':
               thumb = meta['cover_url']

          if meta['backdrop_url'] == '':
                  fanart = artwork + '/main/fanart.jpg'
          else:
                  fanart = meta['backdrop_url']
                  
     params = {'url':url, 'mode':mode, 'name':title[0], 'thumb':thumb, 'year':year, 'types':'movie'}

     if isfav == False:
          contextMenuItems.append(('Add To VideoPhile Favourites', 'XBMC.RunPlugin(%s)' % addon.build_plugin_url({'url':url, 'mode':'addFavorite', 'name':name, 'thumb':thumb, 'year':year, 'types':'movie', 'rmode':mode})))

     elif isfav == True:
          contextMenuItems.append(('Remove From VideoPhile Favourites', 'XBMC.RunPlugin(%s)' % addon.build_plugin_url({'url':url, 'mode':'removeFavorite', 'name':name, 'thumb':thumb, 'year':year, 'types':'movie', 'rmode':mode})))

     contextMenuItems.append(('Movie Information', 'XBMC.Action(Info)'))
     
     if os.path.exists(xbmc.translatePath("special://home/addons/plugin.video.collective")):
                        contextMenuItems.append(('Search The Collective', 'XBMC.Container.Update(%s?mode=51&url=url&name=%s)' % ('plugin://plugin.video.collective/', name)))
     if settings.getSetting('metadata') == 'true':
          addon.add_directory(params, meta, contextMenuItems, img= thumb, fanart=fanart)
     else:
          addon.add_directory(params, {'title':name},contextMenuItems, img=thumb, fanart= artwork + '/main/fanart.jpg')

#TV Show directory function to be used when adding a TV Show, all metadata scrapes and context menu items are handled within__________
def addSDir(name,url,mode,thumb,isfav):
     contextMenuItems = []
     meta = {}
     
     params = {'url':url, 'mode':mode, 'name':name, 'thumb':thumb, 'year':year, 'types':types, 'show':name}

     if settings.getSetting('metadata') == 'true':
          meta = grab.get_meta('tvshow',name)
          if meta['backdrop_url'] == '':
               fanart = artwork + '/main/fanart.jpg'
          else:
               fanart = meta['backdrop_url']
     else:
          fanart = artwork + '/main/fanart.jpg'
          

     if settings.getSetting('metadata') == 'true':
               if settings.getSetting('banners') == 'false':
                    if thumb == '':
                         thumb = meta['cover_url']
               else:
                    thumb = meta['banner_url']
     if thumb == '':
          thumb = artwork + '/main/noepisode.png'
     
     contextMenuItems.append(('Show Information', 'XBMC.Action(Info)'))

     if isfav == False:
          contextMenuItems.append(('Add To VideoPhile Favourites', 'XBMC.RunPlugin(%s)' % addon.build_plugin_url({'url':url, 'mode':'addFavorite', 'name':name, 'thumb':thumb, 'types':'tvshow', 'rmode':mode})))

     if isfav == True:
          contextMenuItems.append(('Remove From VideoPhile Favourites', 'XBMC.RunPlugin(%s)' % addon.build_plugin_url({'url':url, 'mode':'removeFavorite', 'name':name, 'thumb':thumb, 'types':'tvshow', 'rmode':mode})))


     if os.path.exists(xbmc.translatePath("special://home/addons/plugin.video.collective")):
                        contextMenuItems.append(('Search The Collective', 'XBMC.Container.Update(%s?mode=52&url=url&name=%s)' % ('plugin://plugin.video.collective/', name)))
     if settings.getSetting('metadata') == 'true':
          addon.add_directory(params, meta, contextMenuItems, img=thumb, fanart=fanart)
     else:
          addon.add_directory(params, {'title':name}, contextMenuItems, img= thumb, fanart=fanart)

#Cartoon directory function to be used when adding a Cartoon Series, all metadata scrapes and context menu items are handled within___
def addToonDir(name,url,mode,thumb,isfav):
     contextMenuItems = []
     meta = {}
     
     params = {'url':url, 'mode':mode, 'name':name, 'thumb':thumb, 'year':year, 'types':'cartoon', 'show':name}

     if settings.getSetting('metadata') == 'true':
          meta = grab.get_meta('tvshow',name)
          if meta['backdrop_url'] == '':
               fanart = artwork + '/main/fanart.jpg'
          else:
               fanart = meta['backdrop_url']
     else:
          fanart = artwork + '/main/fanart.jpg'
          
     
     if settings.getSetting('metadata') == 'true':
               if settings.getSetting('banners') == 'false':
                    if thumb == '':
                         thumb = meta['cover_url']
               else:
                    thumb = meta['banner_url']
     if thumb == '':
          thumb = artwork + '/main/noepisode.png'
     
     contextMenuItems.append(('Show Information', 'XBMC.Action(Info)'))

     if isfav == False:
          contextMenuItems.append(('Add To VideoPhile Favourites', 'XBMC.RunPlugin(%s)' % addon.build_plugin_url({'url':url, 'mode':'addFavorite', 'name':name, 'thumb':thumb, 'types':'cartoon', 'rmode':mode})))

     if isfav == True:
          contextMenuItems.append(('Remove From VideoPhile Favourites', 'XBMC.RunPlugin(%s)' % addon.build_plugin_url({'url':url, 'mode':'removeFavorite', 'name':name, 'thumb':thumb, 'types':'cartoon', 'rmode':mode})))


     if os.path.exists(xbmc.translatePath("special://home/addons/plugin.video.collective")):
                        contextMenuItems.append(('Search The Collective', 'XBMC.Container.Update(%s?mode=52&url=url&name=%s)' % ('plugin://plugin.video.collective/', name)))
     if settings.getSetting('metadata') == 'true':
          addon.add_directory(params, meta, contextMenuItems, img=thumb, fanart=fanart)
     else:
          addon.add_directory(params, {'title':name},contextMenuItems , img= thumb, fanart=fanart)

#Anime directory function to be used when adding a Anime Series, all metadata scrapes and context menu items are handled within______
def addAnimeDir(name,url,mode,thumb, isfav):
     contextMenuItems = []
     meta = {}
     
     params = {'url':url, 'mode':mode, 'name':name, 'thumb':thumb, 'year':year, 'types':'anime', 'show':name}

     if settings.getSetting('metadata') == 'true':
          meta = grab.get_meta('tvshow',name)
          if meta['backdrop_url'] == '':
               fanart = artwork + '/main/fanart.jpg'
          else:
               fanart = meta['backdrop_url']
     else:
          fanart = artwork + '/main/fanart.jpg'

     if settings.getSetting('metadata') == 'true':
          if meta['backdrop_url'] == '':
               fanart = artwork + '/main/fanart.jpg'
          else:
               fanart = meta['backdrop_url']
     
     if settings.getSetting('metadata') == 'true':
               if settings.getSetting('banners') == 'false':
                    if thumb == '':
                         thumb = meta['cover_url']
               else:
                    thumb = meta['banner_url']
     if thumb == '':
          thumb = artwork + '/main/noepisode.png'
     
     contextMenuItems.append(('Show Information', 'XBMC.Action(Info)'))

     if isfav == False:
          contextMenuItems.append(('Add To VideoPhile Favourites', 'XBMC.RunPlugin(%s)' % addon.build_plugin_url({'url':url, 'mode':'addFavorite', 'name':name, 'thumb':thumb, 'types':'anime', 'rmode':mode})))

     if isfav == True:
          contextMenuItems.append(('Remove From VideoPhile Favourites', 'XBMC.RunPlugin(%s)' % addon.build_plugin_url({'url':url, 'mode':'removeFavorite', 'name':name, 'thumb':thumb, 'types':'anime', 'rmode':mode})))


     if os.path.exists(xbmc.translatePath("special://home/addons/plugin.video.collective")):
                        contextMenuItems.append(('Search The Collective', 'XBMC.Container.Update(%s?mode=52&url=url&name=%s)' % ('plugin://plugin.video.collective/', name)))
     if settings.getSetting('metadata') == 'true':
          addon.add_directory(params, meta, contextMenuItems, img=thumb, fanart=fanart)
     else:
          addon.add_directory(params, {'title':name},contextMenuItems, img= thumb, fanart=fanart)

#Host directory function to be used when adding a file Host, hthumb stands for host thumb and should be grabbed using the 'GETHOSTTHUMB(host)' function before hand
def addHDir(name,url,mode,thumb,hthumb):
     fanart = artwork + '/main/fanart.jpg'
     name = re.sub('[()]','',name)
     params = {'url':url, 'mode':mode, 'name':name, 'thumb':thumb, 'year':year, 'types':types, 'season':season, 'episode':episode, 'show':show}
     addon.add_directory(params, {'title':name}, img=hthumb, fanart=fanart)

#Episode directory function to be used when adding a Episode, all metadata scrapes and context menu items are handled within_________
def addEDir(name,url,mode,thumb,show):
     ep_meta = None
     show_id = None
     meta = None
     othumb = thumb

     name = name.replace("&#8217;","")
     name = name.replace("&#8211;"," ")
                
     if settings.getSetting('metadata') == 'true':
          meta = grab.get_meta('tvshow',show)
          show_id = meta['imdb_id']

     else:
          fanart = artwork + '/main/fanart.jpg'
     
     s,e = GET_EPISODE_NUMBERS(name)

     if settings.getSetting('metadata') == 'true':
          try:
               ep_meta = grab.get_episode_meta(show,show_id,int(s),int(e))
               if ep_meta['cover_url'] == '':
                    thumb = artwork + '/main/noepisode.png'
               else:
                    thumb = str(ep_meta['cover_url'])
          except:
               ep_meta=None
               thumb = artwork + '/main/noepisode.png'
             
     else:
          thumb = othumb
          if thumb == '':
               thumb = artwork + '/main/noepisode.png'
     
     params = {'url':url, 'mode':mode, 'name':name, 'thumb':thumb, 'season':s, 'episode':e, 'show':show, 'types':'episode'}        
     if settings.getSetting('metadata') == 'true':

          if ep_meta==None:
               fanart = artwork + '/main/fanart.jpg'
               addon.add_directory(params, {'title':name}, img=thumb, fanart=fanart) 
          else:
               if meta['backdrop_url'] == '':
                    fanart = artwork + '/main/fanart.jpg'
               else:
                    fanart = meta['backdrop_url']
               ep_meta['title'] = name
               addon.add_directory(params, ep_meta, fanart=fanart, img=thumb)
     else:
          addon.add_directory(params, {'title':name},fanart=fanart, img=thumb) 

#Called within the addEDir function, returns needed season and episode numbers needed for metadata scraping___________________________

def GET_EPISODE_NUMBERS(ep_name):
     s = None
     e = None
     ep_name = re.sub('×','X',ep_name)

     S00E00 = re.findall('[Ss]\d\d[Ee]\d\d',ep_name)
     SXE = re.findall('\d[Xx]\d',ep_name)
     SXEE = re.findall('\d[Xx]\d\d',ep_name)
     SXEEE = re.findall('\d[Xx]\d\d\d',ep_name)

     SSXE = re.findall('\d\d[Xx]\d',ep_name)
     SSXEE = re.findall('\d\d[Xx]\d\d',ep_name)
     SSXEEE = re.findall('\d\d[Xx]\d\d\d',ep_name)
     
     if S00E00:
          print 'Naming Style Is ' + 'S00E00'
          S00E00 = str(S00E00)
          S00E00.strip('[Ss][Ee]')
          e = S00E00[-4:]
          e = e[:-2]
          s = S00E00[:6]
          s = s[-2:]

     if SXE:
          SXE = str(SXE)
          s = SXE[2]
          e = SXE[4]

     if SXEE:
          SXEE = str(SXEE)
          s = SXEE[2]
          e = SXEE[4] + SXEE[5]

     if SXEEE:
          SXEEE = str(SXEEE)
          s = SXEEE[2]
          e = SXEEE[4] + SXEEE[5] + SXEEE[6]

     if SSXE:
          SSXE = str(SSXE)
          s = SSXE[2] + SSXE[3]
          e = SSXE[5]

     if SSXEE:
          SSXEE = str(SSXEE)
          s = SSXEE[2] + SSXEE[3]
          e = SSXEE[5] + SSXEE[6]

     if SSXEEE:
          SSXEEE = str(SSXEEE)
          s = SSXEEE[2] + SSXEE[3]
          e = SSXEEE[5] + SSXEEE[6] + SSXEEE[7]

     
     return s,e

#Returns the host thumbnail so that you can pass it as and argument to the addHDir function__________________________________________
def GETHOSTTHUMB(host):
     if host.endswith('.com'):
          host = host[:-4]
     if host.endswith('.org'):
          host = host[:-4]
     if host.endswith('.eu'):
          host = host[:-3]
     if host.endswith('.ch'):
          host = host[:-3]
     if host.endswith('.in'):
          host = host[:-3]
     if host.endswith('.es'):
          host = host[:-3]
     if host.endswith('.tv'):
          host = host[:-3]
     if host.endswith('.net'):
          host = host[:-4]
     if host.endswith('.me'):
          host = host[:-3]
     if host.endswith('.ws'):
          host = host[:-3]
     if host.endswith('.sx'):
          host = host[:-3]
     if host.startswith('www.'):
             host = host[4:]
     if 'movzap' in host:
          host = 'movzap'

     if 'uploadcrazy' in host:
          host = 'uploadcrazy'

     if 'vidcrazy' in host:
          host = 'vidcrazy'

     if 'epornik' in host:
          host = 'epornik'
     
     host = artwork + '/hosts/' + host +'.png'
     return(host)

#Function used for resolving video urls before  playback_____________________________________________________________________________     
def RESOLVE(name,url,thumb):
     meta=0
     try:
          meta = getMeta(types,name,year,show,season,episode)
     except:
          meta=0
     hmf = urlresolver.HostedMediaFile(url)
     host = ''
     if hmf:
          url = urlresolver.resolve(url)
          host = hmf.get_host()
     else:
          url = OTHER_RESOLVERS(url)
             
     params = {'url':url, 'name':name, 'thumb':thumb}
     if meta == 0:
          addon.add_video_item(params, {'title':name}, img=thumb)
          liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=thumb)

     else:
          addon.add_video_item(params, {'title':name}, img=meta['cover_url'])
          liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=meta['cover_url'])
          liz.setInfo('video',infoLabels=meta)

     xbmc.sleep(1000)
        
     xbmc.Player ().play(url, liz, False)

#Used to resolve urls that urlresolver doesn't support________________________________________________________________________________
def OTHER_RESOLVERS(url):
     if 'vidx.to' in url:
        br = mechanize.Browser()

        response1 = br.open(url)

        addon.show_countdown(20,'VidX.to','')
        
        br.select_form(nr=0)
        response2 = br.submit()
        link=response2.read()
        response2.close()
        xbmc.sleep(1000)
        match=re.compile('file: "(.+?)"').findall(link)
        url = match[0]

     if 'uploadcrazy' in url:
          link = net.http_GET(url).content
          links=re.compile("file': '(.+?)'").findall(link)
          if len(links) > 0:
                    url = links[0]

     if 'vidcrazy' in url:
          link = net.http_GET(url).content
          links=re.compile("file': '(.+?)'").findall(link)
          if len(links) > 0:
                    url = links[0]

     if 'animeonair' in url:
          link = net.http_GET(url).content
          links=re.compile("file': '(.+?)'").findall(link)
          if len(links) > 0:
                    url = links[0]

     if 'epornik' in url:
          link = net.http_GET(url).content
          links=re.compile('s1.addVariable(.+?);').findall(link)
          dirty = re.sub("[',)(]", '', (links[5]))
          url =   dirty[7:-1]

     if 'video44' in url:
          url = url.replace('&#038;','&')
          link = net.http_GET(url).content
          match=re.compile('file: "(.+?)"').findall(link)
          url = match[0]

     if 'play44' in url:
          url = url.replace('&#038;','&')
          link = net.http_GET(url).content
          match=re.compile("\n\t\t\t\t\t\t\t\t\t\t\t\turl: \'(.+?)'").findall(link)
          url = match[0]
          url = url.replace('%2F','/')
          url = url.replace('%3F','?')
          url = url.replace('%3D','=')
          url = url.replace('%26','&')

     if 'cheesestream' in url:
          link = net.http_GET(url).content
          match=re.compile('<source src="(.+?)"').findall(link)
          url = match[0]

               

     return str(url)

#Sets the desired view type___________________________________________________________________________________________________________     
def AUTOVIEW(content):
        if content:
                xbmcplugin.setContent(int(sys.argv[1]), content)
                if settings.getSetting('auto-view') == 'true':
                        if content == 'movies':
                                xbmc.executebuiltin("Container.SetViewMode(%s)" % settings.getSetting('movies-view'))
                        elif content == 'tvshows':
                                xbmc.executebuiltin("Container.SetViewMode(%s)" % settings.getSetting('shows-view'))
                        elif content == 'episodes':
                                xbmc.executebuiltin("Container.SetViewMode(%s)" % settings.getSetting('episodes-view'))      
                        else:
                                xbmc.executebuiltin("Container.SetViewMode(%s)" % settings.getSetting('default-view'))
                else:
                        xbmc.executebuiltin("Container.SetViewMode(%s)" % settings.getSetting('default-view') )


        
