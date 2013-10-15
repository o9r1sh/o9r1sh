# -*- coding: utf-8 -*-
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
season = addon.queries.get('season', '')
episode = addon.queries.get('episode', '')
show = addon.queries.get('show', '')
types = addon.queries.get('types', '')

settings = xbmcaddon.Addon(id='<plugin.video.videophile>')
artwork = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.videophile/resources/artwork/', ''))
grab=metahandlers.MetaData()

def addDir(name,url,mode,thumb):   
     params = {'url':url, 'mode':mode, 'name':name, 'thumb':thumb, 'year':year, 'types':types}
     addon.add_directory(params, {'title':name}, img= thumb)

def addMDir(name,url,mode,thumb,year):
     contextMenuItems = []
     
     meta = grab.get_meta('movie',name,year,None,None,overlay=6)
     try:
          imdb = meta['imdb_id']
     except:
          imdb_id = ''

     if year == '':
          year = str(meta['year'])
          if year == '0':
               name = name
          else:
               name = name + ' ' + '(' + year +')'
          
     else:
          name = name + ' ' +  year

     meta['title'] = name
     if thumb == '':
          thumb = meta['cover_url']
     if thumb == '':
          thumb = artwork + 'nothumb.png'

     params = {'url':url, 'mode':mode, 'name':name, 'thumb':thumb, 'year':year, 'types':types}

     contextMenuItems.append(('Movie Information', 'XBMC.Action(Info)'))
     
     if os.path.exists(xbmc.translatePath("special://home/addons/plugin.video.collective")):
                        contextMenuItems.append(('Search The Collective', 'XBMC.Container.Update(%s?mode=51&url=url&name=%s)' % ('plugin://plugin.video.collective/', name)))

     addon.add_directory(params, meta, contextMenuItems, img= thumb, fanart=meta['backdrop_url'])


def addSDir(name,url,mode,thumb):
     contextMenuItems = []
     
     params = {'url':url, 'mode':mode, 'name':name, 'thumb':thumb, 'year':year, 'types':types}
     meta = grab.get_meta('tvshow',name)

     if thumb == '':
          thumb = meta['cover_url']
     if thumb == '':
          thumb = meta['banner_url']
     if thumb == '':
          thumb = artwork + 'nothumb.png'

     contextMenuItems.append(('Show Information', 'XBMC.Action(Info)'))

     if os.path.exists(xbmc.translatePath("special://home/addons/plugin.video.collective")):
                        contextMenuItems.append(('Search The Collective', 'XBMC.Container.Update(%s?mode=52&url=url&name=%s)' % ('plugin://plugin.video.collective/', name)))
     
     addon.add_directory(params, meta, contextMenuItems, img=thumb, fanart=meta['backdrop_url'])

def addHDir(name,url,mode,thumb,hthumb):   
     params = {'url':url, 'mode':mode, 'name':name, 'thumb':thumb, 'year':year, 'types':types}
     addon.add_directory(params, {'title':name}, img= hthumb)

def addEDir(name,url,mode,thumb,show):
     
     meta = grab.get_meta('tvshow',show)
     ep_meta = None
     show_id = meta['imdb_id']

     s,e = GET_EPISODE_NUMBERS(name)
     try:
          ep_meta = grab.get_episode_meta(show,show_id,int(s),int(e))
     except:
          ep_meta=0

     params = {'url':url, 'mode':mode, 'name':name, 'thumb':thumb, 'show':show, 'season':season, 'episode':episode}        
     
     if ep_meta==0:
          addon.add_directory(params, {'title':name}, img=thumb) 
     else:
          ep_meta['title'] = name
          addon.add_directory(params, ep_meta, fanart=meta['backdrop_url'], img=ep_meta['cover_url'])

def GET_SHOW_THUMB(show_name):
     meta = grab.get_meta('tvshow',show_name)
     thumb = meta['cover_url']
     if thumb == '':
          thumb = meta['banner_url']  
     return(thumb)
     
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
          S00E00 = str(S00E00)
          S00E00.strip('[Ss][Ee]')
          e = S00E00[-4:]
          e = e[:-2]
          s = S00E00[:5]
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
        if host.endswith('.sx'):
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

        xbmc.sleep(1000)
        
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


        
