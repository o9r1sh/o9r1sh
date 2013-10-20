#WeWatchMoviesFree Module by o9r1sh October 2013

import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmcaddon,sys,main,xbmc,os
import urlresolver

artwork = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.videophile/resources/artwork/', ''))
base_url = 'http://www.iwatchonline.to'


def MOVIE_CATEGORIES():
        main.addDir('Recently Added',base_url +'/main/content_more/movies/?sort=latest&start=0',51,artwork + '/main/recentlyadded.png')
        main.addDir('Popular',base_url + '/main/content_more/movies/?sort=popular&start=0',51,artwork + '/main/popular.png')
        main.addDir('A-Z','none',54,artwork + '/main/a-z.png')
        main.addDir('HD Movies','none',53,artwork + '/main/hd.png')
        main.addDir('Genres','none',56,artwork + '/main/genres.png')

def HD_MOVIES():
        main.addDir('Recently Added',base_url +'/main/content_more/movies/?sort=latest&quality=hd&start=0',51,artwork + '/main/recentlyadded.png')
        main.addDir('Popular',base_url + '/main/content_more/movies/?sort=popular&quality=hd&start=0',51,artwork + '/main/popular.png')
        main.addDir('A-Z','none',55,artwork + '/main/a-z.png')
        main.addDir('Genres','none',57,artwork + '/main/genres.png')
        
def LETTERS():
        main.addDir('#',base_url + '/main/content_more/movies/?startwith=09&start=0',51,artwork + '/letters/num.png')
        main.addDir('A',base_url + '/main/content_more/movies/?startwith=a&start=0',51,artwork + '/letters/a.png')
        main.addDir('B',base_url + '/main/content_more/movies/?startwith=b&start=0',51,artwork + '/letters/b.png')
        main.addDir('C',base_url + '/main/content_more/movies/?startwith=c&start=0',51,artwork + '/letters/c.png')
        main.addDir('D',base_url + '/main/content_more/movies/?startwith=d&start=0',51,artwork + '/letters/d.png')
        main.addDir('E',base_url + '/main/content_more/movies/?startwith=e&start=0',51,artwork + '/letters/e.png')
        main.addDir('F',base_url + '/main/content_more/movies/?startwith=f&start=0',51,artwork + '/letters/f.png')
        main.addDir('G',base_url + '/main/content_more/movies/?startwith=g&start=0',51,artwork + '/letters/g.png')
        main.addDir('H',base_url + '/main/content_more/movies/?startwith=h&start=0',51,artwork + '/letters/h.png')
        main.addDir('I',base_url + '/main/content_more/movies/?startwith=i&start=0',51,artwork + '/letters/i.png')
        main.addDir('J',base_url + '/main/content_more/movies/?startwith=j&start=0',51,artwork + '/letters/j.png')
        main.addDir('K',base_url + '/main/content_more/movies/?startwith=k&start=0',51,artwork + '/letters/k.png')
        main.addDir('L',base_url + '/main/content_more/movies/?startwith=l&start=0',51,artwork + '/letters/l.png')
        main.addDir('M',base_url + '/main/content_more/movies/?startwith=m&start=0',51,artwork + '/letters/m.png')
        main.addDir('N',base_url + '/main/content_more/movies/?startwith=n&start=0',51,artwork + '/letters/n.png')
        main.addDir('O',base_url + '/main/content_more/movies/?startwith=o&start=0',51,artwork + '/letters/o.png')
        main.addDir('P',base_url + '/main/content_more/movies/?startwith=p&start=0',51,artwork + '/letters/p.png')
        main.addDir('Q',base_url + '/main/content_more/movies/?startwith=q&start=0',51,artwork + '/letters/q.png')
        main.addDir('R',base_url + '/main/content_more/movies/?startwith=r&start=0',51,artwork + '/letters/r.png')
        main.addDir('S',base_url + '/main/content_more/movies/?startwith=s&start=0',51,artwork + '/letters/s.png')
        main.addDir('T',base_url + '/main/content_more/movies/?startwith=t&start=0',51,artwork + '/letters/t.png')
        main.addDir('U',base_url + '/main/content_more/movies/?startwith=u&start=0',51,artwork + '/letters/u.png')
        main.addDir('V',base_url + '/main/content_more/movies/?startwith=v&start=0',51,artwork + '/letters/v.png')
        main.addDir('W',base_url + '/main/content_more/movies/?startwith=w&start=0',51,artwork + '/letters/w.png')
        main.addDir('X',base_url + '/main/content_more/movies/?startwith=x&start=0',51,artwork + '/letters/x.png')
        main.addDir('Y',base_url + '/main/content_more/movies/?startwith=y&start=0',51,artwork + '/letters/y.png')
        main.addDir('Z',base_url + '/main/content_more/movies/?startwith=z&start=0',51,artwork + '/letters/z.png')

def HD_LETTERS():
        main.addDir('#',base_url + '/main/content_more/movies/?quality=hd&startwith=09&start=0',51,artwork + '/letters/num.png')
        main.addDir('A',base_url + '/main/content_more/movies/?quality=hd&startwith=a&start=0',51,artwork + '/letters/a.png')
        main.addDir('B',base_url + '/main/content_more/movies/?quality=hd&startwith=b&start=0',51,artwork + '/letters/b.png')
        main.addDir('C',base_url + '/main/content_more/movies/?quality=hd&startwith=c&start=0',51,artwork + '/letters/c.png')
        main.addDir('D',base_url + '/main/content_more/movies/?quality=hd&startwith=d&start=0',51,artwork + '/letters/d.png')
        main.addDir('E',base_url + '/main/content_more/movies/?quality=hd&startwith=e&start=0',51,artwork + '/letters/e.png')
        main.addDir('F',base_url + '/main/content_more/movies/?quality=hd&startwith=f&start=0',51,artwork + '/letters/f.png')
        main.addDir('G',base_url + '/main/content_more/movies/?quality=hd&startwith=g&start=0',51,artwork + '/letters/g.png')
        main.addDir('H',base_url + '/main/content_more/movies/?quality=hd&startwith=h&start=0',51,artwork + '/letters/h.png')
        main.addDir('I',base_url + '/main/content_more/movies/?quality=hd&startwith=i&start=0',51,artwork + '/letters/i.png')
        main.addDir('J',base_url + '/main/content_more/movies/?quality=hd&startwith=j&start=0',51,artwork + '/letters/j.png')
        main.addDir('K',base_url + '/main/content_more/movies/?quality=hd&startwith=k&start=0',51,artwork + '/letters/k.png')
        main.addDir('L',base_url + '/main/content_more/movies/?quality=hd&startwith=l&start=0',51,artwork + '/letters/l.png')
        main.addDir('M',base_url + '/main/content_more/movies/?quality=hd&startwith=m&start=0',51,artwork + '/letters/m.png')
        main.addDir('N',base_url + '/main/content_more/movies/?quality=hd&startwith=n&start=0',51,artwork + '/letters/n.png')
        main.addDir('O',base_url + '/main/content_more/movies/?quality=hd&startwith=o&start=0',51,artwork + '/letters/o.png')
        main.addDir('P',base_url + '/main/content_more/movies/?quality=hd&startwith=p&start=0',51,artwork + '/letters/p.png')
        main.addDir('Q',base_url + '/main/content_more/movies/?quality=hd&startwith=q&start=0',51,artwork + '/letters/q.png')
        main.addDir('R',base_url + '/main/content_more/movies/?quality=hd&startwith=r&start=0',51,artwork + '/letters/r.png')
        main.addDir('S',base_url + '/main/content_more/movies/?quality=hd&startwith=s&start=0',51,artwork + '/letters/s.png')
        main.addDir('T',base_url + '/main/content_more/movies/?quality=hd&startwith=t&start=0',51,artwork + '/letters/t.png')
        main.addDir('U',base_url + '/main/content_more/movies/?quality=hd&startwith=u&start=0',51,artwork + '/letters/u.png')
        main.addDir('V',base_url + '/main/content_more/movies/?quality=hd&startwith=v&start=0',51,artwork + '/letters/v.png')
        main.addDir('W',base_url + '/main/content_more/movies/?quality=hd&startwith=w&start=0',51,artwork + '/letters/w.png')
        main.addDir('X',base_url + '/main/content_more/movies/?quality=hd&startwith=x&start=0',51,artwork + '/letters/x.png')
        main.addDir('Y',base_url + '/main/content_more/movies/?quality=hd&startwith=y&start=0',51,artwork + '/letters/y.png')
        main.addDir('Z',base_url + '/main/content_more/movies/?quality=hd&startwith=z&start=0',51,artwork + '/letters/z.png')

def GENRES():
        main.addDir('Action','none',58,artwork + '/genres/action.png')
        main.addDir('Adventure','none',59,artwork + '/genres/adventure.png')
        main.addDir('Animation','none',60,artwork + '/genres/animation.png')
        main.addDir('Biography','none',61,artwork + '/genres/biography.png')
        main.addDir('Comedy','none',62,artwork + '/genres/comedy.png')
        main.addDir('Crime','none',63,artwork + '/genres/crime.png')
        main.addDir('Documentary','none',64,artwork + '/genres/docs.png')
        main.addDir('Drama','none',65,artwork + '/genres/drama.png')
        main.addDir('Family','none',66,artwork + '/genres/family.png')
        main.addDir('Fantasy','none',67,artwork + '/genres/fantasy.png')
        main.addDir('Film-Noir','none',68,artwork + '/genres/film-noir.png')
        main.addDir('History','none',69,artwork + '/genres/historyg.png')
        main.addDir('Horror','none',70,artwork + '/genres/horror.png')
        main.addDir('Music','none',71,artwork + '/genres/music.png')
        main.addDir('Musical','none',72,artwork + '/genres/musical.png')
        main.addDir('Mystery','none',73,artwork + '/genres/mystery.png')
        main.addDir('News','none',74,artwork + '/genres/news.png')
        main.addDir('Romance','none',75,artwork + '/genres/romance.png')
        main.addDir('Sci-Fi','none',76,artwork + '/genres/sci-fi.png')
        main.addDir('Short','none',77,artwork + '/genres/short.png')
        main.addDir('Sport','none',78,artwork + '/genres/sport.png')
        main.addDir('Thriller','none',79,artwork + '/genres/thriller.png')
        main.addDir('War','none',80,artwork + '/genres/war.png')
        main.addDir('Western','none',81,artwork + '/genres/western.png')

def ACTION():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=action&sort=popular&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=action&sort=latest&start=0',51,artwork + '/main/recentlyadded.png')

def ADVENTURE():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=adventure&sort=popular&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=adventure&sort=latest&start=0',51,artwork + '/main/recentlyadded.png')

def ANIMATION():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=animation&sort=popular&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=animation&sort=latest&start=0',51,artwork + '/main/recentlyadded.png')

def BIOGRAPHY():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=biography&sort=popular&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=biography&sort=latest&start=0',51,artwork + '/main/recentlyadded.png')

def COMEDY():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=comedy&sort=popular&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=comedy&sort=latest&start=0',51,artwork + '/main/recentlyadded.png')

def CRIME():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=crime&sort=popular&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=crime&sort=latest&start=0',51,artwork + '/main/recentlyadded.png')

def DOCUMENTARY():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=documentary&sort=popular&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=documentary&sort=latest&start=0',51,artwork + '/main/recentlyadded.png')

def DRAMA():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=drama&sort=popular&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=drama&sort=latest&start=0',51,artwork + '/main/recentlyadded.png')

def FAMILY():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=family&sort=popular&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=family&sort=latest&start=0',51,artwork + '/main/recentlyadded.png')

def FANTASY():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=fantasy&sort=popular&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=fantasy&sort=latest&start=0',51,artwork + '/main/recentlyadded.png')

def FILMNOIR():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=film-noir&sort=popular&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=film-noir&sort=latest&start=0',51,artwork + '/main/recentlyadded.png')

def HISTORY():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=history&sort=popular&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=history&sort=latest&start=0',51,artwork + '/main/recentlyadded.png')

def HORROR():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=horror&sort=popular&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=horror&sort=latest&start=0',51,artwork + '/main/recentlyadded.png')

def MUSIC():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=music&sort=popular&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=music&sort=latest&start=0',51,artwork + '/main/recentlyadded.png')

def MUSICAL():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=musical&sort=popular&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=musical&sort=latest&start=0',51,artwork + '/main/recentlyadded.png')

def MYSTERY():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=mystery&sort=popular&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=mystery&sort=latest&start=0',51,artwork + '/main/recentlyadded.png')

def NEWS():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=news&sort=popular&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=news&sort=latest&start=0',51,artwork + '/main/recentlyadded.png')

def ROMANCE():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=romance&sort=popular&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=romance&sort=latest&start=0',51,artwork + '/main/recentlyadded.png')

def SCIFI():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=sci-fi&sort=popular&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=sci-fi&sort=latest&start=0',51,artwork + '/main/recentlyadded.png')

def SHORT():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=short&sort=popular&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=short&sort=latest&start=0',51,artwork + '/main/recentlyadded.png')

def SPORT():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=sport&sort=popular&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=sport&sort=latest&start=0',51,artwork + '/main/recentlyadded.png')

def THRILLER():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=thriller&sort=popular&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=thriller&sort=latest&start=0',51,artwork + '/main/recentlyadded.png')

def WAR():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=war&sort=popular&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=war&sort=latest&start=0',51,artwork + '/main/recentlyadded.png')

def WESTERN():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=western&sort=popular&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=western&sort=latest&start=0',51,artwork + '/main/recentlyadded.png')

def HD_GENRES():
        main.addDir('Action','none',82,artwork + '/genres/action.png')
        main.addDir('Adventure','none',83,artwork + '/genres/adventure.png')
        main.addDir('Animation','none',84,artwork + '/genres/animation.png')
        main.addDir('Biography','none',85,artwork + '/genres/biography.png')
        main.addDir('Comedy','none',86,artwork + '/genres/comedy.png')
        main.addDir('Crime','none',87,artwork + '/genres/crime.png')
        main.addDir('Documentary','none',88,artwork + '/genres/docs.png')
        main.addDir('Drama','none',89,artwork + '/genres/drama.png')
        main.addDir('Family','none',90,artwork + '/genres/family.png')
        main.addDir('Fantasy','none',91,artwork + '/genres/fantasy.png')
        main.addDir('Film-Noir','none',92,artwork + '/genres/film-noir.png')
        main.addDir('History','none',93,artwork + '/genres/historyg.png')
        main.addDir('Horror','none',94,artwork + '/genres/horror.png')
        main.addDir('Music','none',95,artwork + '/genres/music.png')
        main.addDir('Musical','none',96,artwork + '/genres/musical.png')
        main.addDir('Mystery','none',97,artwork + '/genres/mystery.png')
        main.addDir('News','none',98,artwork + '/genres/news.png')
        main.addDir('Romance','none',99,artwork + '/genres/romance.png')
        main.addDir('Sci-Fi','none',100,artwork + '/genres/sci-fi.png')
        main.addDir('Short','none',101,artwork + '/genres/short.png')
        main.addDir('Sport','none',102,artwork + '/genres/sport.png')
        main.addDir('Thriller','none',103,artwork + '/genres/thriller.png')
        main.addDir('War','none',104,artwork + '/genres/war.png')
        main.addDir('Western','none',105,artwork + '/genres/western.png')

def HD_ACTION():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=action&sort=popular&quality=hd&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=action&sort=latest&quality=hd&start=0',51,artwork + '/main/recentlyadded.png')

def HD_ADVENTURE():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=adventure&sort=popular&quality=hd&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=adventure&sort=latest&quality=hd&start=0',51,artwork + '/main/recentlyadded.png')

def HD_ANIMATION():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=animation&sort=popular&quality=hd&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=animation&sort=latest&quality=hd&start=0',51,artwork + '/main/recentlyadded.png')

def HD_BIOGRAPHY():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=biography&sort=popular&quality=hd&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=biography&sort=latest&quality=hd&start=0',51,artwork + '/main/recentlyadded.png')

def HD_COMEDY():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=comedy&sort=popular&quality=hd&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=comedy&sort=latest&quality=hd&start=0',51,artwork + '/main/recentlyadded.png')

def HD_CRIME():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=crime&sort=popular&quality=hd&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=crime&sort=latest&quality=hd&start=0',51,artwork + '/main/recentlyadded.png')

def HD_DOCUMENTARY():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=documentary&sort=popular&quality=hd&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=documentary&sort=latest&quality=hd&start=0',51,artwork + '/main/recentlyadded.png')

def HD_DRAMA():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=drama&sort=popular&quality=hd&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=drama&sort=latest&quality=hd&start=0',51,artwork + '/main/recentlyadded.png')

def HD_FAMILY():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=family&sort=popular&quality=hd&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=family&sort=latest&quality=hd&start=0',51,artwork + '/main/recentlyadded.png')

def HD_FANTASY():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=fantasy&sort=popular&quality=hd&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=fantasy&sort=latest&quality=hd&start=0',51,artwork + '/main/recentlyadded.png')

def HD_FILMNOIR():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=film-noir&sort=popular&quality=hd&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=film-noir&sort=latest&quality=hd&start=0',51,artwork + '/main/recentlyadded.png')

def HD_HISTORY():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=history&sort=popular&quality=hd&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=history&sort=latest&quality=hd&start=0',51,artwork + '/main/recentlyadded.png')

def HD_HORROR():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=horror&sort=popular&quality=hd&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=horror&sort=latest&quality=hd&start=0',51,artwork + '/main/recentlyadded.png')

def HD_MUSIC():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=music&sort=popular&quality=hd&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=music&sort=latest&quality=hd&start=0',51,artwork + '/main/recentlyadded.png')

def HD_MUSICAL():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=musical&sort=popular&quality=hd&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=musical&sort=latest&quality=hd&start=0',51,artwork + '/main/recentlyadded.png')

def HD_MYSTERY():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=mystery&sort=popular&quality=hd&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=mystery&sort=latest&quality=hd&start=0',51,artwork + '/main/recentlyadded.png')

def HD_NEWS():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=news&sort=popular&quality=hd&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=news&sort=latest&quality=hd&start=0',51,artwork + '/main/recentlyadded.png')

def HD_ROMANCE():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=romance&sort=popular&quality=hd&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=romance&sort=latest&quality=hd&start=0',51,artwork + '/main/recentlyadded.png')

def HD_SCIFI():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=sci-fi&sort=popular&quality=hd&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=sci-fi&sort=latest&quality=hd&start=0',51,artwork + '/main/recentlyadded.png')

def HD_SHORT():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=short&sort=popular&quality=hd&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=short&sort=latest&quality=hd&start=0',51,artwork + '/main/recentlyadded.png')

def HD_SPORT():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=sport&sort=popular&quality=hd&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=sport&sort=latest&quality=hd&start=0',51,artwork + '/main/recentlyadded.png')

def HD_THRILLER():
        main.addDir('Popular',base_url + '/mai/main/content_more/movies/?gener=thriller&sort=popular&quality=hd&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=thriller&sort=latest&quality=hd&start=0',51,artwork + '/main/recentlyadded.png')

def HD_WAR():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=war&sort=popular&quality=hd&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=war&sort=latest&quality=hd&start=0',51,artwork + 'recentlyadded.png')

def HD_WESTERN():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=western&sort=popular&quality=hd&start=0',51,artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=western&sort=latest&quality=hd&start=0',51,artwork + '/main/recentlyadded.png')
        
def MOVIE_INDEX(url):
        a,b,c = url.partition('&start=')
        next_page_number = int(c) + 25
        next_page = a+b+str(next_page_number)
        
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('<a href="(.+?)" class=".+?" rel=".+?">\r\n\t\t\t\t\t\t\t<img class=".+?" src="(.+?)" alt="">\r\n\t\t\t\t\t\t\t <div class=".+?">.+?</div>\t  \r\n\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t<div class=".+?">.+?').findall(link)
        d,e,f = url.partition('=latest&start=')
        if len(match) >24:
                main.addDir('Next Page',next_page,51,artwork + '/main/next.png')
        
        for url,thumbnail in match:
                head,sep,tail = url.partition('/movie/')
                head,sep,tail = url.partition('-')
                year = tail[-4:]
                year = '(' + year + ')'
                name = tail[:-4]
                name = re.sub('-s','s',name)
                name = re.sub('-',' ',name)
                name = re.sub("'",'',name)
                name = name.title()
        
                try:
                        main.addMDir(name,url,52,thumbnail,year)
                except:
                        continue
        main.AUTOVIEW('movies')

def VIDEOLINKS(name,url,thumb):
        inc = 0
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('<td class="sideleft"><a href="(.+?)"').findall(link)
        for url in match:
                if inc < 50:
                        req = urllib2.Request(url)
                        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                        response = urllib2.urlopen(req)
                        link=response.read()
                        response.close()
                        urls=re.compile('<iframe name="frame" class="frame" src="(.+?)"').findall(link)

                        hmf = urlresolver.HostedMediaFile(urls[0])
                        if hmf:
                                host = hmf.get_host()
                                hthumb = main.GETHOSTTHUMB(host)
                                try:
                                        main.addHDir(name,str(urls[0]),9,thumb,hthumb)
                                        inc +=1
                                except:
                                        continue
                



