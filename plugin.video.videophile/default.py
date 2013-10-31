#VideoPhile addon by o9r1sh

import urllib,urllib2,re,xbmcplugin,xbmcgui,sys,xbmc,urlresolver,xbmcaddon
from resources.modules import main,mooviemaniac,wsoeu,youtube,nmvl,fma,zmovie,wwmf,videocloud,iwo,freeomovie,tvrelease,tubepirate,cartoonfreak
from resources.modules import channelcut,mmline,filmikz,epornik

addon_id = 'plugin.video.videophile'
from t0mm0.common.addon import Addon
addon = main.addon

settings = xbmcaddon.Addon(id='<plugin.video.videophile>')
artwork = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.videophile/resources/artwork/', ''))

text_file = None
if not os.path.exists(xbmc.translatePath("special://home/userdata/addon_data/plugin.video.videophile/")):
        os.makedirs(xbmc.translatePath("special://home/userdata/addon_data/plugin.video.videophile/"))

if not os.path.exists(xbmc.translatePath("special://home/userdata/addon_data/plugin.video.videophile/sec.0")):
        pin = ''
        notice = xbmcgui.Dialog().ok('Notice','VideoPhile now contains an adult section, for safety reasons','after pressing ok you will be asked to set a password','that will be used to gain access to the adult section')
        keyboard = xbmc.Keyboard(pin,'Please Choose A New Password')
        keyboard.doModal()
        if keyboard.isConfirmed():
                pin = keyboard.getText()
        text_file = open(xbmc.translatePath("special://home/userdata/addon_data/plugin.video.videophile/sec.0"), "w")
        text_file.write(pin)
        text_file.close()
           
def CATEGORIES():
        if settings.getSetting('adult') == 'true':
                main.addDir('Adults Only','none','adultSections',artwork + '/main/adult.png')
        if settings.getSetting('movies') == 'true':
                main.addDir('Movies','none','movieSections',artwork + '/main/movie.png')
        if settings.getSetting('hdmovies') == 'true':
                main.addDir('HD Movies','none','hdSections',artwork + '/main/hd.png')
        if settings.getSetting('shows') == 'true':        
                main.addDir('TV Shows','none','tvSections',artwork + '/main/tv.png')
        if settings.getSetting('docs') == 'true':
                main.addDir('Documentaries','none','docSections',artwork + '/main/docs.png')
        if settings.getSetting('cartoons') == 'true':
                main.addDir('Cartoons','none','cartoonSections',artwork + '/main/cartoons.png')
        if settings.getSetting('anime') == 'true':
                main.addDir('Anime','none','animeSections',artwork + '/main/anime.png')
        if settings.getSetting('favorites') == 'true':
                main.addDir('Favorites','none','favorites',artwork + '/main/favorites.png')
        if settings.getSetting('search') == 'true':
                main.addDir('Master Search','none','masterSearch',artwork + '/main/search.png')
        if settings.getSetting('resolver') == 'true':
                main.addDir('Resolver Settings','none','resolverSettings',artwork + '/main/resolver.png')

def MOVIESECTIONS():
        if settings.getSetting('mooviemaniac') == 'true':
                main.addDir('MoovieManiac','none','moovieManiacCategories',artwork + '/main/mmaniac.png')
        if settings.getSetting('newmyvideolinks') == 'true':
                main.addDir('NewMyVideoLinks','none','newMyVideoLinksCategories',artwork + '/main/nmvl.png')
        if settings.getSetting('freemoviesaddict') == 'true':
                main.addDir('FreeMoviesAddict','none','fmaCategories',artwork + '/main/fma.png')
        if settings.getSetting('zmovie') == 'true':
                main.addDir('Watch-Movies / Z-Movie','none','zmovieCategories',artwork + '/main/zmovie.png')
        if settings.getSetting('wwmf') == 'true':
                main.addDir('WeWatchMoviesFree','none','wwmfCategories',artwork + '/main/wwmf.png')
        if settings.getSetting('videocloud') == 'true':
                main.addDir('VideoCloud','none','videoCloudCategories',artwork + '/main/videocloud.png')
        if settings.getSetting('iwatchonline') == 'true':
               main.addDir('I-WatchOnline','none','iwoCategories',artwork + '/main/iwatchonline.png')
        if settings.getSetting('tvrelease') == 'true':
                main.addDir('TV Release','none','tvreleaseMovieCategories',artwork + '/main/tvrelease.png')
        if settings.getSetting('mmline') == 'true':
                main.addDir('MegaMovieLine','none','mmlineCategories',artwork + '/main/mmline.png')

def HDMOVIESECTIONS():
        if settings.getSetting('newmyvideolinks') == 'true':
                main.addDir('NewMyVideoLinks Yify Movies','none','newMyVideoLinksHDMovies',artwork + '/main/nmvl.png')
        if settings.getSetting('tvrelease') == 'true':
                main.addDir('TV Release','none','tvreleaseHDMovies',artwork + '/main/tvrelease.png')
        
def TVSECTIONS():
        if settings.getSetting('wsoeu') == 'true':
                main.addDir('WatchSeries-Online','none','watchSeriesOnlineCategories',artwork + '/main/wso.png')
        if settings.getSetting('newmyvideolinks') == 'true':
                main.addDir('NewMyVideoLinks','none','newMyVideoLinksTVCategories',artwork + '/main/nmvl.png')
        if settings.getSetting('tvrelease') == 'true':
                main.addDir('TV Release','none','tvreleaseTVCategories',artwork + '/main/tvrelease.png')
        if settings.getSetting('channelcut') == 'true':
                main.addDir('ChannelCut','none','channelCutCategories',artwork + '/main/channelcut.png')
        if settings.getSetting('iwatchonline') == 'true':
               main.addDir('I-WatchOnline','none','iwoSeriesCategories',artwork + '/main/iwatchonline.png')

def DOCSECTIONS():
        if settings.getSetting('youtubedocs') == 'true':
                main.addDir('National Geographic Documentaries','http://www.youtube.com/results?search_query=national+geographic&oq=national+geographic&gs_l=youtube.3..35i39l2j0l8.1350.5331.0.5427.19.19.0.0.0.0.106.1194.17j2.19.0...0.0...1ac.1.11.youtube._BEl_uoU7Bk','youtubeIndex',artwork + '/main/natgeo.png')
                main.addDir('BBC Documentaries','http://www.youtube.com/results?search_query=bbc&oq=bbc&gs_l=youtube.3..0l7j0i3j0l2.11848138.11848424.0.11848594.3.3.0.0.0.0.116.301.1j2.3.0...0.0...1ac.1.11.youtube.de569af2UXE','youtubeIndex',artwork + '/main/bbc.png')
                main.addDir('History Channel Documentaries','http://www.youtube.com/results?search_query=history+channel+documentary&oq=history+&gs_l=youtube.1.0.0l10.24739.26444.0.29034.8.6.0.2.2.0.121.583.5j1.6.0...0.0...1ac.1.11.youtube.9fDvAjIM7ug','youtubeIndex',artwork + '/main/history.png')
                main.addDir('Discovery Channel Documentaries','http://www.youtube.com/results?search_query=discovery+channel+documentary&oq=discovery+channel+documentary&gs_l=youtube.3..0l10.243928.245622.0.246576.10.10.0.0.0.0.110.743.9j1.10.0...0.0...1ac.1.11.youtube.oK45qI8tlys','youtubeIndex',artwork + '/main/discovery.png')

def MASTERSEARCH():
        search = ''
        keyboard = xbmc.Keyboard(search,'Search')
        keyboard.doModal()
        if keyboard.isConfirmed():
                search = keyboard.getText()
                search = search.replace(' ','+')

        threads = []
        if settings.getSetting('mmline') == 'true':
                threads.append(main.Thread(mmline.MASTERSEARCH(search)))
        if settings.getSetting('wwmf') == 'true':
                threads.append(main.Thread(wwmf.MASTERSEARCH(search)))
        if settings.getSetting('newmyvideolinks') == 'true':
                threads.append(main.Thread(nmvl.MASTERSEARCH(search)))
        if settings.getSetting('channelcut') == 'true':
                threads.append(main.Thread(channelcut.MASTERSEARCH(search)))
        if settings.getSetting('wsoeu') == 'true':
                threads.append(main.Thread(wsoeu.MASTERSEARCH(search)))
        if settings.getSetting('tvrelease') == 'true':
                threads.append(main.Thread(tvrelease.MASTERSEARCH(search)))
        [i.start() for i in threads]
        [i.join() for i in threads]

def COLLECTIVESEARCH(search):
        threads = []
        if settings.getSetting('mmline') == 'true':
                threads.append(main.Thread(mmline.MASTERSEARCH(search)))
        if settings.getSetting('wwmf') == 'true':
                threads.append(main.Thread(wwmf.MASTERSEARCH(search)))
        if settings.getSetting('newmyvideolinks') == 'true':
                threads.append(main.Thread(nmvl.MASTERSEARCH(search)))
        if settings.getSetting('channelcut') == 'true':
                threads.append(main.Thread(channelcut.MASTERSEARCH(search)))
        if settings.getSetting('wsoeu') == 'true':
                threads.append(main.Thread(wsoeu.MASTERSEARCH(search)))
        if settings.getSetting('tvrelease') == 'true':
                threads.append(main.Thread(tvrelease.MASTERSEARCH(search)))
        [i.start() for i in threads]
        [i.join() for i in threads]
                
def CARTOONSECTIONS():
        if settings.getSetting('cartoonfreak') == 'true':
                main.addDir('Cartoon Freak','none','cartoonFreakToons',artwork + '/main/cartoonfreak.png')

def ANIMESECTIONS():
        if settings.getSetting('cartoonfreak') == 'true':
                main.addDir('Cartoon Freak','none','cartoonFreakAnime',artwork + '/main/cartoonfreak.png')
        
def ADULT():
        pin = ''
        keyboard = xbmc.Keyboard(pin,'Please Enter Your Password')
        keyboard.doModal()
        if keyboard.isConfirmed():
                pin = keyboard.getText()
        text_file = open(xbmc.translatePath("special://home/userdata/addon_data/plugin.video.videophile/sec.0"), "r")
        line = file.readline(text_file)
        if pin == line:
                main.addDir('Epornik','none','epornikCategories',artwork + '/main/epornik.png')
                main.addDir('Filmikz','none','filmikzAdultCategories',artwork + '/main/filmikz.png')
                main.addDir('FreeoMovie','none','freeOMovieCategories',artwork + '/main/freeomovie.png')
                main.addDir('TubePirate','none','tubePirateCategories',artwork + '/main/tubepirate.png')
        else:
                notice = xbmcgui.Dialog().ok('Wrong Password','The password you entered is incorrect')

def FAVORITES():
        if settings.getSetting('movies') == 'true':
                main.addDir('Movies','movie','getFavorites',artwork + '/main/movie.png')
        if settings.getSetting('shows') == 'true':
                main.addDir('TV Shows','tvshow','getFavorites',artwork + '/main/tv.png')
        if settings.getSetting('cartoons') == 'true':
                main.addDir('Cartoons','cartoon','getFavorites',artwork + '/main/cartoons.png')
        if settings.getSetting('anime') == 'true':
                main.addDir('Anime','anime','getFavorites',artwork + '/main/anime.png')
      
mode = addon.queries['mode']
url = addon.queries.get('url', '')
name = addon.queries.get('name', '')
thumb = addon.queries.get('thumb', '')
year = addon.queries.get('year', '')
season = addon.queries.get('season', '')
episode = addon.queries.get('episode', '')
show = addon.queries.get('show', '')
types = addon.queries.get('types', '')

print "Mode is: "+str(mode)
print "URL is: "+str(url)
print "Name is: "+str(name)
print "Thumb is: "+str(thumb)
print "Year is: "+str(year)
print "Season is: "+str(season)
print "Episode is: "+str(episode)
print "Show is: "+str(show)
print "Type is: "+str(types)

#Default modes__________________________________________________________________
if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()

elif mode=='addFavorite':
        print ""+url
        main.addFavorite()

elif mode=='removeFavorite':
        print ""+url
        main.removeFavorite()


elif mode=='getFavorites':
        print ""+url
        main.getFavorites(url)

elif mode=='favorites':
        print ""+url
        FAVORITES()
        
elif mode=='movieSections':
        print ""+url
        MOVIESECTIONS()

elif mode=='tvSections':
        print ""+url
        TVSECTIONS()

elif mode=='docSections':
        print ""+url
        DOCSECTIONS()

elif mode=='hdSections':
        print ""+url
        HDMOVIESECTIONS()

elif mode=='masterSearch':
        print ""+url
        MASTERSEARCH()

elif mode=='collectiveSearch':
        print ""+url
        COLLECTIVESEARCH(search)

elif mode=='adultSections':
        print ""+url
        ADULT()

elif mode=='resolverSettings':
        print ""+url
        urlresolver.display_settings()

elif mode=='cartoonSections':
        print ""+url
        CARTOONSECTIONS()

elif mode=='animeSections':
        print ""+url
        ANIMESECTIONS()
#Main modes_____________________________________________________________________
elif mode=='resolve':
        print ""+url
        main.RESOLVE(name,url,thumb)
#MoovieManic modes______________________________________________________________
elif mode=='moovieManiacCategories':
        print ""+url
        mooviemaniac.CATEGORIES()

elif mode=='moovieManiacIndex':
        print ""+url
        mooviemaniac.INDEX(url)
#WatchSeries-Online modes_______________________________________________________
elif mode=='watchSeriesOnlineCategories':
        print ""+url
        wsoeu.CATEGORIES()

elif mode=='watchSeriesOnlineSeriesIndex':
        print ""+url
        wsoeu.INDEXSHOWS(url)

elif mode=='watchSeriesOnlineEpisodesIndex':
        print ""+url
        wsoeu.INDEXEPS(url,name)

elif mode=='watchSeriesOnlineVideoLinks':
        print ""+url
        wsoeu.VIDEOLINKS(url,name,thumb)

elif mode=='watchSeriesOnlineSearch':
        print ""+url
        wsoeu.SEARCH()

elif mode=='watchSeriesOnlineLetters':
        print ""+url
        wsoeu.LETTERS()

elif mode=='watchSeriesOnlineRecentEpisodes':
        print ""+url
        wsoeu.RECENTEPS(url)
#Youtube documentaries modes____________________________________________________
elif mode=='youtubeIndex':
        print ""+url
        youtube.INDEX(url)
#NewMyVideoLinks modes__________________________________________________________
elif mode=='newMyVideoLinksCategories':
        print ""+url
        nmvl.CATEGORIES()

elif mode=='newMyVideoLinksIndex':
        print ""+url
        nmvl.INDEX(url)
        
elif mode=='newMyVideoLinksVideoLinks':
        print ""+url
        nmvl.VIDEOLINKS(name,url,thumb,year)

elif mode=='newMyVideoLinksTVCategories':
        print ""+url
        nmvl.TVCATEGORIES()

elif mode=='newMyVideoLinksSearch':
        print ""+url
        nmvl.SEARCH()

elif mode=='newMyVideoLinksHDMovies':
        print ""+url
        nmvl.HDMOVIES()

#Free Movies Addict modes_______________________________________________________
elif mode=='fmaCategories':
        print ""+url
        fma.CATEGORIES()

elif mode=='fmaIndex':
        print ""+url
        fma.INDEX(url)

elif mode=='fmaVideoLinks':
        print ""+url
        fma.VIDEOLINKS(name,url,thumb)

elif mode=='fmaGenres':
        print ""+url
        fma.GENRES()

elif mode=='fmaYears':
        print ""+url
        fma.YEARS()

elif mode=='fmaLetters':
        print ""+url
        fma.LETTERS()
#Z-Movie modes__________________________________________________________________
elif mode=='zmovieIndex':
        print ""+url
        zmovie.INDEX(url)

elif mode=='zmovieLetters':
        print ""+url
        zmovie.LETTERS()

elif mode=='zmovieGenres':
        print ""+url
        zmovie.GENRES()

elif mode=='zmovieCategories':
        print ""+url
        zmovie.CATEGORIES()

elif mode=='zmovieVideoLinks':
        print ""+url
        zmovie.VIDEOLINKS(name,url,thumb)
#We Watch Movies Free___________________________________________________________
elif mode=='wwmfCategories':
        print ""+url
        wwmf.CATEGORIES()
        
elif mode=='wwmfIndex':
        print ""+url
        wwmf.INDEX(url)

elif mode=='wwmfLetters':
        print ""+url
        wwmf.LETTERS()

elif mode=='wwmfGenres':
        print ""+url
        wwmf.GENRES()

elif mode=='wwmfSearch':
        print ""+url
        wwmf.SEARCH()

elif mode=='wwmfVideoLinks':
        print ""+url
        wwmf.VIDEOLINKS(name,url,thumb)
#Videocloud modes_______________________________________________________________
elif mode=='videoCloudCategories':
        print ""+url
        videocloud.CATEGORIES()

elif mode=='videoCloudIndex':
        print ""+url
        videocloud.INDEX(url)
#I-WatchOnline modes____________________________________________________________
elif mode=='iwoCategories':
        print ""+url
        iwo.MOVIE_CATEGORIES()

elif mode=='iwoSeriesCategories':
        print ""+url
        iwo.SERIES_CATEGORIES()

elif mode=='iwoSeriesGenres':
        print ""+url
        iwo.SERIES_GENRES()

elif mode=='iwoSeriesLetters':
        print ""+url
        iwo.SERIES_LETTERS()

elif mode=='iwoIndex':
        print ""+url
        iwo.MOVIE_INDEX(url)

elif mode=='iwoSeriesIndex':
        print ""+url
        iwo.SERIES_INDEX(url)

elif mode=='iwoEpisodesIndex':
        print ""+url
        iwo.EPISODES_INDEX(url,name)

elif mode=='iwoVideoLinks':
        print ""+url
        iwo.VIDEOLINKS(name,url,thumb)

elif mode=='iwoHDMovies':
        print ""+url
        iwo.HD_MOVIES()

elif mode=='iwoLetters':
        print ""+url
        iwo.LETTERS()

elif mode=='iwoHDLetters':
        print ""+url
        iwo.HD_LETTERS()

elif mode=='iwoGenres':
        print ""+url
        iwo.GENRES()

elif mode=='iwoHDGenres':
        print ""+url
        iwo.HD_GENRES()

elif mode=='iwoAction':
        print ""+url
        iwo.ACTION()

elif mode=='iwoAdventure':
        print ""+url
        iwo.ADVENTURE()

elif mode=='iwoAnimation':
        print ""+url
        iwo.ANIMATION()

elif mode=='iwoBiography':
        print ""+url
        iwo.BIOGRAPHY()

elif mode=='iwoComedy':
        print ""+url
        iwo.COMEDY()

elif mode=='iwoCrime':
        print ""+url
        iwo.CRIME()

elif mode=='iwoDocumentary':
        print ""+url
        iwo.DOCUMENTARY()

elif mode=='iwoDrama':
        print ""+url
        iwo.DRAMA()

elif mode=='iwoFamily':
        print ""+url
        iwo.FAMILY()

elif mode=='iwoFantasy':
        print ""+url
        iwo.FANTASY()

elif mode=='iwoFilmNoir':
        print ""+url
        iwo.FILMNOIR()

elif mode=='iwoHistory':
        print ""+url
        iwo.HISTORY()

elif mode=='iwoHorror':
        print ""+url
        iwo.HORROR()

elif mode=='iwoMusic':
        print ""+url
        iwo.MUSIC()

elif mode=='iwoMusical':
        print ""+url
        iwo.MUSICAL()

elif mode=='iwoMystery':
        print ""+url
        iwo.MYSTERY()

elif mode=='iwoNews':
        print ""+url
        iwo.NEWS()

elif mode=='iwoRomance':
        print ""+url
        iwo.ROMANCE()

elif mode=='iwoSciFi':
        print ""+url
        iwo.SCIFI()

elif mode=='iwoShort':
        print ""+url
        iwo.SHORT()

elif mode=='iwoSport':
        print ""+url
        iwo.SPORT()

elif mode=='iwoThriller':
        print ""+url
        iwo.THRILLER()

elif mode=='iwoWar':
        print ""+url
        iwo.WAR()

elif mode=='iwoWestern':
        print ""+url
        iwo.WESTERN()


elif mode=='iwoHDAction':
        print ""+url
        iwo.HD_ACTION()

elif mode=='iwoHDAdventure':
        print ""+url
        iwo.HD_ADVENTURE()

elif mode=='iwoHDAnimation':
        print ""+url
        iwo.HD_ANIMATION()

elif mode=='iwoHDBiography':
        print ""+url
        iwo.HD_BIOGRAPHY()

elif mode=='iwoHDComedy':
        print ""+url
        iwo.HD_COMEDY()

elif mode=='iwoHDCrime':
        print ""+url
        iwo.HD_CRIME()

elif mode=='iwoHDDocumentary':
        print ""+url
        iwo.HD_DOCUMENTARY()

elif mode=='iwoHDDrama':
        print ""+url
        iwo.HD_DRAMA()

elif mode=='iwoHDFamily':
        print ""+url
        iwo.HD_FAMILY()

elif mode=='iwoHDFantasy':
        print ""+url
        iwo.HD_FANTASY()

elif mode=='iwoHDFilmNoir':
        print ""+url
        iwo.HD_FILMNOIR()

elif mode=='iwoHDHistory':
        print ""+url
        iwo.HD_HISTORY()

elif mode=='iwoHDHorror':
        print ""+url
        iwo.HD_HORROR()

elif mode=='iwoHDMusic':
        print ""+url
        iwo.HD_MUSIC()

elif mode=='iwoHDMusical':
        print ""+url
        iwo.HD_MUSICAL()

elif mode=='iwoHDMystery':
        print ""+url
        iwo.HD_MYSTERY()

elif mode=='iwoHDNews':
        print ""+url
        iwo.HD_NEWS()

elif mode=='IwoHDRomance':
        print ""+url
        iwo.HD_ROMANCE()

elif mode=='iwoHDSciFi':
        print ""+url
        iwo.HD_SCIFI()

elif mode=='iwoHDShort':
        print ""+url
        iwo.HD_SHORT()

elif mode=='iwoHDSport':
        print ""+url
        iwo.HD_SPORT()

elif mode=='iwoHDThriller':
        print ""+url
        iwo.HD_THRILLER()

elif mode=='iwoHDWar':
        print ""+url
        iwo.HD_WAR()

elif mode=='iwoHDWestern':
        print ""+url
        iwo.HD_WESTERN()
#TV Release Modes_______________________________________________________________
elif mode=='tvreleaseHDMovies':
        print ""+url
        tvrelease.HDMOVIES()

elif mode=='tvreleaseSearch':
        print ""+url
        tvrelease.SEARCH()
        
elif mode=='tvreleaseVideoLinks':
        print ""+url
        tvrelease.VIDEOLINKS(name,url,thumb)

elif mode=='tvreleaseIndex':
        print ""+url
        tvrelease.INDEX(url) 

elif mode=='tvreleaseMovieCategories':
        print ""+url
        tvrelease.MOVIE_CATEGORIES() 

elif mode=='tvreleaseTVCategories':
        print ""+url
        tvrelease.TV_CATEGORIES()
#FreeOMovie Modes_______________________________________________________________
elif mode=='freeOMovieCategories':
        print ""+url
        freeomovie.CATEGORIES()

elif mode=='freeOMovieGenres':
        print ""+url
        freeomovie.GENRES()

elif mode=='freeOMovieIndex':
        print ""+url
        freeomovie.INDEX(url)

elif mode=='freeOMovieVideoLinks':
        print ""+url
        freeomovie.VIDEOLINKS(name,url,thumb)
#TubePirate Modes_______________________________________________________________
elif mode=='tubePirateCategories':
        print ""+url
        tubepirate.CATEGORIES()

elif mode=='tubePirateIndex':
        print ""+url
        tubepirate.INDEX(url)

elif mode=='tubePirateMostViewed':
        print ""+url
        tubepirate.MOST_VIEWED()

elif mode=='tubePirateTopRated':
        print ""+url
        tubepirate.TOP_RATED()

elif mode=='tubePirateActors':
        print ""+url
        tubepirate.ACTORS()

elif mode=='tubePirateLetters':
        print ""+url
        tubepirate.LETTERS()

elif mode=='tubePirateTopRatedActors':
        print ""+url
        tubepirate.TOP_RATED_ACTORS()

elif mode=='tubePirateMostViewedActors':
        print ""+url
        tubepirate.MOST_VIEWED_ACTORS()

elif mode=='tubePirateMostActorIndex':
        print ""+url
        tubepirate.ACTOR_INDEX(url)

elif mode=='tubePirateGenres':
        print ""+url
        tubepirate.GENRES()
#CartoonFreak Modes_____________________________________________________________
elif mode=='cartoonFreakToons':
        print ""+url
        cartoonfreak.CARTOONS()

elif mode=='cartoonFreakAnime':
        print ""+url
        cartoonfreak.ANIME()

elif mode=='cartoonFreakAnimeSeries':
        print ""+url
        cartoonfreak.ANIMESERIES()

elif mode=='cartoonFreakAnimeMovies':
        print ""+url
        cartoonfreak.ANIMEMOVIES()

elif mode=='cartoonFreakIndex':
        print ""+url
        cartoonfreak.INDEX(url)

elif mode=='cartoonFreakMovieIndex':
        print ""+url
        cartoonfreak.MOVIEINDEX(url)

elif mode=='cartoonFreakEpisodes':
        print ""+url
        cartoonfreak.EPISODES(url)

elif mode=='cartoonFreakAnimeEpisodes':
        print ""+url
        cartoonfreak.ANIMEEPISODES(url,thumb)

elif mode=='cartoonFreakMovieEpisodes':
        print ""+url
        cartoonfreak.MOVIEEPISODES(url,thumb)

elif mode=='cartoonFreakVideoLinks':
        print ""+url
        cartoonfreak.VIDEOLINKS(name,url,thumb)
#ChannelCut Modes_______________________________________________________________
elif mode=='channelCutIndex':
        print ""+url
        channelcut.INDEX(url)

elif mode=='channelCutCategories':
        print ""+url
        channelcut.CATEGORIES()

elif mode=='channelCutLetters':
        print ""+url
        channelcut.LETTERS()

elif mode=='channelCutEpisodes':
        print ""+url
        channelcut.EPISODES(url)

elif mode=='channelCutRecentEpisodes':
        print ""+url
        channelcut.RECENTEPISODES(url)

elif mode=='channelCutVideoLinks':
        print ""+url
        channelcut.VIDEOLINKS(name,url)

elif mode=='channelCutNum':
        print ""+url
        channelcut.NUM()

elif mode=='channelCutA':
        print ""+url
        channelcut.A()

elif mode=='channelCutB':
        print ""+url
        channelcut.B()

elif mode=='channelCutC':
        print ""+url
        channelcut.C()

elif mode=='channelCutD':
        print ""+url
        channelcut.D()

elif mode=='channelCutE':
        print ""+url
        channelcut.E()

elif mode=='channelCutF':
        print ""+url
        channelcut.F()

elif mode=='channelCutG':
        print ""+url
        channelcut.G()

elif mode=='channelCutH':
        print ""+url
        channelcut.H()

elif mode=='channelCutI':
        print ""+url
        channelcut.I()

elif mode=='channelCutJ':
        print ""+url
        channelcut.J()

elif mode=='channelCutK':
        print ""+url
        channelcut.K()

elif mode=='channelCutL':
        print ""+url
        channelcut.L()

elif mode=='channelCutM':
        print ""+url
        channelcut.M()

elif mode=='channelCutN':
        print ""+url
        channelcut.N()

elif mode=='channelCutO':
        print ""+url
        channelcut.O()

elif mode=='channelCutP':
        print ""+url
        channelcut.P()

elif mode=='channelCutQ':
        print ""+url
        channelcut.Q()

elif mode=='channelCutR':
        print ""+url
        channelcut.R()

elif mode=='channelCutS':
        print ""+url
        channelcut.S()

elif mode=='channelCutT':
        print ""+url
        channelcut.T()

elif mode=='channelCutU':
        print ""+url
        channelcut.U()

elif mode=='channelCutV':
        print ""+url
        channelcut.V()

elif mode=='channelCutW':
        print ""+url
        channelcut.W()

elif mode=='channelCutX':
        print ""+url
        channelcut.X()

elif mode=='channelCutY':
        print ""+url
        channelcut.Y()

elif mode=='channelCutZ':
        print ""+url
        channelcut.Z()

elif mode=='channelCutSearch':
        print ""+url
        channelcut.SEARCH()

elif mode=='mmlineCategories':
        print ""+url
        mmline.CATEGORIES()

elif mode=='mmlineIndex':
        print ""+url
        mmline.INDEX(url)

elif mode=='mmlineGenres':
        print ""+url
        mmline.GENRES()

elif mode=='mmlineVideoLinks':
        print ""+url
        mmline.VIDEOLINKS(name,url,thumb)

elif mode=='mmlineSearch':
        print ""+url
        mmline.SEARCH()

elif mode=='mmlineAction':
        print ""+url
        mmline.ACION()

elif mode=='mmlineAdventure':
        print ""+url
        mmline.ADVENTURE()
        
elif mode=='mmlineAnimation':
        print ""+url
        mmline.ANIMATION()
        
elif mode=='mmlineBiography':
        print ""+url
        mmline.BIOGRAPHY()
        
elif mode=='mmlineComedy':
        print ""+url
        mmline.COMEDY()
        
elif mode=='mmlineCrime':
        print ""+url
        mmline.CRIME()
        
elif mode=='mmlineDocumentary':
        print ""+url
        mmline.DOCUMENTARY()
        
elif mode=='mmlineDrama':
        print ""+url
        mmline.DRAMA()
        
elif mode=='mmlineFamily':
        print ""+url
        mmline.FAMILY()

elif mode=='mmlineHistory':
        print ""+url
        mmline.HISTORY()
        
elif mode=='mmlineHorror':
        print ""+url
        mmline.HORROR()
        
elif mode=='mmlineMusic':
        print ""+url
        mmline.MUSIC()
        
elif mode=='mmlineMusical':
        print ""+url
        mmline.MUSICAL()
        
elif mode=='mmlineMystery':
        print ""+url
        mmline.MYSTERY()
        
elif mode=='mmlineRomance':
        print ""+url
        mmline.ROMANCE()
        
elif mode=='mmlineScifi':
        print ""+url
        mmline.SCIFI()
        
elif mode=='mmlineSport':
        print ""+url
        mmline.SPORT()
        
elif mode=='mmlineThriller':
        print ""+url
        mmline.THRILLER()

elif mode=='mmlineWar':
        print ""+url
        mmline.WAR()
        
elif mode=='mmlineWestern':
        print ""+url
        mmline.WESTERN()
        
elif mode=='mmlineIndian':
        print ""+url
        mmline.INDIAN()
        
elif mode=='mmlineShort':
        print ""+url
        mmline.SHORT()

elif mode=='mmlineClassic':
        print ""+url
        mmline.CLASSIC()
#Filmikz Modes___________________________________________________________________
elif mode=='filmikzAdultCategories':
        print ""+url
        filmikz.ADULT_CATEGORIES()

elif mode=='filmikzAdultIndex':
        print ""+url
        filmikz.ADULT_INDEX(url)

elif mode=='filmikzVideoLinks':
        print ""+url
        filmikz.VIDEOLINKS(url,name,thumb)

elif mode=='filmikzAdultSearch':
        print ""+url
        filmikz.ADULT_SEARCH()
#Epornik Modes__________________________________________________________________
elif mode=='epornikCategories':
        print ""+url
        epornik.CATEGORIES()

elif mode=='epornikIndex':
        print ""+url
        epornik.INDEX(url)

elif mode=='epornikSearch':
        print ""+url
        epornik.SEARCH()

















xbmcplugin.endOfDirectory(int(sys.argv[1]))
