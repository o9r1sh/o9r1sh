# -*- coding: utf-8 -*-
#Main VideoPhile module by o9r1sh

import urllib,urllib2,re,xbmcplugin,xbmcgui,sys,urlresolver,xbmc,os,xbmcaddon,mechanize
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
fanart = addon.queries.get('fanart', '')

settings = xbmcaddon.Addon(id='<plugin.video.videophile>')
artwork = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.videophile/resources/artwork/', ''))
grab=metahandlers.MetaData()


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

def addDir(name,url,mode,thumb):   
     params = {'url':url, 'mode':mode, 'name':name, 'thumb':thumb, 'year':year, 'types':'movie'}
     addon.add_directory(params, {'title':name}, img= thumb, fanart= artwork + '/main/fanart.jpg')

def addMDir(name,url,mode,thumb,year):
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

     contextMenuItems.append(('Movie Information', 'XBMC.Action(Info)'))
     
     if os.path.exists(xbmc.translatePath("special://home/addons/plugin.video.collective")):
                        contextMenuItems.append(('Search The Collective', 'XBMC.Container.Update(%s?mode=51&url=url&name=%s)' % ('plugin://plugin.video.collective/', name)))
     if settings.getSetting('metadata') == 'true':
          addon.add_directory(params, meta, contextMenuItems, img= thumb, fanart=fanart)
     else:
               addon.add_directory(params, {'title':name}, img= thumb, fanart= artwork + '/main/fanart.jpg')

          

def addSDir(name,url,mode,thumb):
     contextMenuItems = []
     meta = None
     
     params = {'url':url, 'mode':mode, 'name':name, 'thumb':thumb, 'year':year, 'types':types, 'show':name}

     if settings.getSetting('metadata') == 'true':
          meta = grab.get_meta('tvshow',name)

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
     
   

     contextMenuItems.append(('Show Information', 'XBMC.Action(Info)'))

     if os.path.exists(xbmc.translatePath("special://home/addons/plugin.video.collective")):
                        contextMenuItems.append(('Search The Collective', 'XBMC.Container.Update(%s?mode=52&url=url&name=%s)' % ('plugin://plugin.video.collective/', name)))
     if settings.getSetting('metadata') == 'true':
          addon.add_directory(params, meta, contextMenuItems, img=thumb, fanart=fanart)
     else:
          addon.add_directory(params, {'title':name}, img= thumb, fanart=fanart)

def addHDir(name,url,mode,thumb,hthumb):
     fanart = artwork + '/main/fanart.jpg'
     name = re.sub('[()]','',name)
     params = {'url':url, 'mode':mode, 'name':name, 'thumb':thumb, 'year':year, 'types':types, 'season':season, 'episode':episode, 'show':show}
     addon.add_directory(params, {'title':name}, img=hthumb, fanart=fanart)

def addEDir(name,url,mode,thumb,show):
     ep_meta = None
     show_id = None
     meta = None
     othumb = thumb
     if settings.getSetting('metadata') == 'true':
          meta = grab.get_meta('tvshow',show)
          show_id = meta['imdb_id']
     
     s,e = GET_EPISODE_NUMBERS(name)

     if settings.getSetting('metadata') == 'true':
          try:
               ep_meta = grab.get_episode_meta(show,show_id,int(s),int(e))
          except:
               ep_meta=0

          try:
               thumb = str(ep_meta['cover_url'])
          
          except:
               if thumb == '':
                    thumb = othumb
     else:
          thumb = othumb
          

     params = {'url':url, 'mode':mode, 'name':name, 'thumb':thumb, 'season':s, 'episode':e, 'show':show, 'types':'episode'}        
     if settings.getSetting('metadata') == 'true':

          if ep_meta==0:
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
          addon.add_directory(params, {'title':name}, img=thumb, fanart=fanart) 

          
     
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
        host = artwork + '/hosts/' + host +'.png'
        return(host)
     
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

     return str(url)
     

          
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


        
