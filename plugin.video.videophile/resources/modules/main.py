#Main VideoPhile module by o9r1sh

import urllib,urllib2,re,xbmcplugin,xbmcgui,sys,urlresolver,xbmc,os,xbmcaddon
from metahandler import metahandlers

addon_id = 'plugin.video.videophile'
from t0mm0.common.addon import Addon
addon = Addon(addon_id, sys.argv)

mode = addon.queries['mode']
url = addon.queries.get('url', '')
name = addon.queries.get('name', '')
thumb = addon.queries.get('thumb', '')
year = addon.queries.get('year', '')
types = addon.queries.get('types', '')


settings = xbmcaddon.Addon(id='<plugin.video.videophile>')
artwork = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.videophile/resources/artwork/', ''))
grab=metahandlers.MetaData()

def addDir(name,url,mode,thumb):   
     params = {'url':url, 'mode':mode, 'name':name, 'thumb':thumb, 'year':year, 'types':types}
     addon.add_directory(params, {'title':name}, img= thumb)

def addMDir(name,url,mode,thumb,year):
     params = {'url':url, 'mode':mode, 'name':name, 'thumb':thumb, 'year':year, 'types':types}
     meta = grab.get_meta('movie',name,year,None,None,overlay=6)
     if thumb == '':
          thumb = meta['cover_url']
     if thumb == '':
          thumb = artwork + 'nothumb.png'

     addon.add_directory(params, meta, img= thumb)
     
def addSDir(name,url,mode,thumb):
     params = {'url':url, 'mode':mode, 'name':name, 'thumb':thumb, 'year':year, 'types':types}
     meta = grab.get_meta('tvshow',name)

     if thumb == '':
          thumb = meta['cover_url']
     if thumb == '':
          thumb = meta['banner_url']
     if thumb == '':
          thumb = artwork + 'nothumb.png'
     
     addon.add_directory(params, meta,img=thumb)

def addHDir(name,url,mode,thumb,hthumb):   
     params = {'url':url, 'mode':mode, 'name':name, 'thumb':thumb, 'year':year, 'types':types}
     addon.add_directory(params, {'title':name}, img= hthumb)

def addEDir(name,url,mode,thumb,show):
     params = {'url':url, 'mode':mode, 'name':name, 'thumb':thumb, 'year':year, 'types':types}
     meta = grab.get_meta('tvshow',show)

     sooeoo = re.findall('[Ss]\d\d[Ee]\d\d',name)
     sooeoo = str(sooeoo)
     sooeoo.strip('[Ss][Ee]')
     episode = sooeoo[-4:]
     episode = episode[:-2]
     season = sooeoo[:5]
     season = season[-2:]

     show_id = meta['imdb_id']
     ep_meta = grab.get_episode_meta(show,show_id,season,episode)

     if thumb == '':
          thumb = ep_meta['cover_url']
     if thumb == '':
          thumb = meta['cover_url']
     if thumb == '':
          thumb = artwork + 'nothumb.png'
     
     addon.add_directory(params, ep_meta,img=thumb)
    
     

def GETHOSTTHUMB(host):
        if host.endswith('.com'):
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
        if host.startswith('www.'):
             host = host[4:]
        if 'movzap' in host:
             host = 'movzap'
        host = artwork + host +'.png'
        return(host)
     
def RESOLVE(name,url,thumb):
        hmf = urlresolver.HostedMediaFile(url)
        host = ''
        if hmf:
             url = urlresolver.resolve(url)
             host = hmf.get_host()
             
        params = {'url':url, 'name':name, 'thumb':thumb}
        addon.add_item(params, {'title':name}, img= thumb)
        
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=thumb)
        xbmc.Player ().play(url, liz, False)

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


        
