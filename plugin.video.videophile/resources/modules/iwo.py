#WeWatchMoviesFree Module by o9r1sh October 2013

import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmcaddon,sys,main,xbmc,os
import urlresolver

artwork = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.videophile/resources/artwork/', ''))
base_url = 'http://www.iwatchonline.to'


def MOVIE_CATEGORIES():
        main.addDir('Recently Added',base_url +'/main/content_more/movies/?sort=latest&start=0','iwoIndex',artwork + '/main/recentlyadded.png')
        main.addDir('Popular',base_url + '/main/content_more/movies/?sort=popular&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('A-Z','none','iwoLetters',artwork + '/main/a-z.png')
        main.addDir('HD Movies','none','iwoHDMovies',artwork + '/main/hd.png')
        main.addDir('Genres','none','iwoGenres',artwork + '/main/genres.png')

def SERIES_CATEGORIES():
        main.addDir('Recently Added',base_url +'/main/content_more/tv/?sort=latest&start=0','iwoSeriesIndex',artwork + '/main/recentlyadded.png')
        main.addDir('Popular',base_url + '/main/content_more/tv/?sort=popular&start=0','iwoSeriesIndex',artwork + '/main/popular.png')
        main.addDir('A-Z','none','iwoSeriesLetters',artwork + '/main/a-z.png')
        main.addDir('Genres','none','iwoSeriesGenres',artwork + '/main/genres.png')

def SERIES_LETTERS():
        main.addDir('#',base_url + '/main/content_more/tv/?startwith=09&start=0','iwoSeriesIndex',artwork + '/letters/num.png')
        main.addDir('A',base_url + '/main/content_more/tv/?startwith=a&start=0','iwoSeriesIndex',artwork + '/letters/a.png')
        main.addDir('B',base_url + '/main/content_more/tv/?startwith=b&start=0','iwoSeriesIndex',artwork + '/letters/b.png')
        main.addDir('C',base_url + '/main/content_more/tv/?startwith=c&start=0','iwoSeriesIndex',artwork + '/letters/c.png')
        main.addDir('D',base_url + '/main/content_more/tv/?startwith=d&start=0','iwoSeriesIndex',artwork + '/letters/d.png')
        main.addDir('E',base_url + '/main/content_more/tv/?startwith=e&start=0','iwoSeriesIndex',artwork + '/letters/e.png')
        main.addDir('F',base_url + '/main/content_more/tv/?startwith=f&start=0','iwoSeriesIndex',artwork + '/letters/f.png')
        main.addDir('G',base_url + '/main/content_more/tv/?startwith=g&start=0','iwoSeriesIndex',artwork + '/letters/g.png')
        main.addDir('H',base_url + '/main/content_more/tv/?startwith=h&start=0','iwoSeriesIndex',artwork + '/letters/h.png')
        main.addDir('I',base_url + '/main/content_more/tv/?startwith=i&start=0','iwoSeriesIndex',artwork + '/letters/i.png')
        main.addDir('J',base_url + '/main/content_more/tv/?startwith=j&start=0','iwoSeriesIndex',artwork + '/letters/j.png')
        main.addDir('K',base_url + '/main/content_more/tv/?startwith=k&start=0','iwoSeriesIndex',artwork + '/letters/k.png')
        main.addDir('L',base_url + '/main/content_more/tv/?startwith=l&start=0','iwoSeriesIndex',artwork + '/letters/l.png')
        main.addDir('M',base_url + '/main/content_more/tv/?startwith=m&start=0','iwoSeriesIndex',artwork + '/letters/m.png')
        main.addDir('N',base_url + '/main/content_more/tv/?startwith=n&start=0','iwoSeriesIndex',artwork + '/letters/n.png')
        main.addDir('O',base_url + '/main/content_more/tv/?startwith=o&start=0','iwoSeriesIndex',artwork + '/letters/o.png')
        main.addDir('P',base_url + '/main/content_more/tv/?startwith=p&start=0','iwoSeriesIndex',artwork + '/letters/p.png')
        main.addDir('Q',base_url + '/main/content_more/tv/?startwith=q&start=0','iwoSeriesIndex',artwork + '/letters/q.png')
        main.addDir('R',base_url + '/main/content_more/tv/?startwith=r&start=0','iwoSeriesIndex',artwork + '/letters/r.png')
        main.addDir('S',base_url + '/main/content_more/tv/?startwith=s&start=0','iwoSeriesIndex',artwork + '/letters/s.png')
        main.addDir('T',base_url + '/main/content_more/tv/?startwith=t&start=0','iwoSeriesIndex',artwork + '/letters/t.png')
        main.addDir('U',base_url + '/main/content_more/tv/?startwith=u&start=0','iwoSeriesIndex',artwork + '/letters/u.png')
        main.addDir('V',base_url + '/main/content_more/tv/?startwith=v&start=0','iwoSeriesIndex',artwork + '/letters/v.png')
        main.addDir('W',base_url + '/main/content_more/tv/?startwith=w&start=0','iwoSeriesIndex',artwork + '/letters/w.png')
        main.addDir('X',base_url + '/main/content_more/tv/?startwith=x&start=0','iwoSeriesIndex',artwork + '/letters/x.png')
        main.addDir('Y',base_url + '/main/content_more/tv/?startwith=y&start=0','iwoSeriesIndex',artwork + '/letters/y.png')
        main.addDir('Z',base_url + '/main/content_more/tv/?startwith=z&start=0','iwoSeriesIndex',artwork + '/letters/z.png')

def SERIES_GENRES():
        main.addDir('Action',base_url + '/main/content_more/tv/?gener=action&start=0','iwoSeriesIndex',artwork + '/genres/action.png')
        main.addDir('Adventure',base_url + '/main/content_more/tv/?gener=adventure&start=0','iwoSeriesIndex',artwork + '/genres/adventure.png')
        main.addDir('Adult Cartoons',base_url + '/main/content_more/tv/?gener=adult-cartoons&start=0','iwoSeriesIndex',artwork + '/genres/adultcartoons.png')
        main.addDir('Animals',base_url + '/main/content_more/tv/?gener=pets-animals-general&start=0','iwoSeriesIndex',artwork + '/genres/animals.png')
        main.addDir('Animation',base_url + '/main/content_more/tv/?gener=animation-general&start=0','iwoSeriesIndex',artwork + '/genres/animation.png')
        main.addDir('Anime',base_url + '/main/content_more/tv/?gener=anime&start=0','iwoSeriesIndex',artwork + '/genres/anime.png')
        main.addDir('Anthology',base_url + '/main/content_more/tv/?gener=anthology&start=0','iwoSeriesIndex',artwork + '/genres/anthology.png')
        main.addDir('Arts & Crafts',base_url + '/main/content_more/tv/?gener=arts-crafts&start=0','iwoSeriesIndex',artwork + '/genres/artscrafts.png')
        main.addDir('Automobiles',base_url + '/main/content_more/tv/?gener=automobiles&start=0','iwoSeriesIndex',artwork + '/genres/automobiles.png')
        main.addDir('Barter',base_url + '/main/content_more/tv/?gener=buy-sell-trade&start=0','iwoSeriesIndex',artwork + '/genres/barter.png')
        main.addDir('Building',base_url + '/main/content_more/tv/?gener=housing-building&start=0','iwoSeriesIndex',artwork + '/genres/building.png')
        main.addDir('Business',base_url + '/main/content_more/tv/?gener=financial-business&start=0','iwoSeriesIndex',artwork + '/genres/business.png')
        main.addDir('Cartoons',base_url + '/main/content_more/tv/?gener=children-cartoons&start=0','iwoSeriesIndex',artwork + '/genres/cartoons.png')
        main.addDir('Celebrities',base_url + '/main/content_more/tv/?gener=celebrities&start=0','iwoSeriesIndex',artwork + '/genres/celebrities.png')
        main.addDir('Children',base_url + '/main/content_more/tv/?gener=children&start=0','iwoSeriesIndex',artwork + '/genres/children.png')
        main.addDir('Comedy',base_url + '/main/content_more/tv/?gener=comedy&start=0','iwoSeriesIndex',artwork + '/genres/comedy.png')
        main.addDir('Cooking',base_url + '/main/content_more/tv/?gener=cooking-food&start=0','iwoSeriesIndex',artwork + '/genres/cooking.png')
        main.addDir('Crime',base_url + '/main/content_more/tv/?gener=crime&start=0','iwoSeriesIndex',artwork + '/genres/crime.png')
        main.addDir('Current Events',base_url + '/main/content_more/tv/?gener=current-events&start=0','iwoSeriesIndex',artwork + '/genres/currentevents.png')
        main.addDir('Dance',base_url + '/main/content_more/tv/?gener=dance&start=0','iwoSeriesIndex',artwork + '/genres/dance.png')
        main.addDir('Debate',base_url + '/main/content_more/tv/?gener=debate&start=0','iwoSeriesIndex',artwork + '/genres/debate.png')
        main.addDir('Design',base_url + '/main/content_more/tv/?gener=design-decorating&start=0','iwoSeriesIndex',artwork + '/genres/design.png')
        main.addDir('Discovery',base_url + '/main/content_more/tv/?gener=discovery-science&start=0','iwoSeriesIndex',artwork + '/genres/discovery.png')
        main.addDir('DIY',base_url + '/main/content_more/tv/?gener=how-to-do-it-yourself&start=0','iwoSeriesIndex',artwork + '/genres/diy.png')
        main.addDir('Drama',base_url + '/main/content_more/tv/?gener=drama&start=0','iwoSeriesIndex',artwork + '/genres/drama.png')
        main.addDir('Educational',base_url + '/main/content_more/tv/?gener=educational&start=0','iwoSeriesIndex',artwork + '/genres/educational.png')
        main.addDir('Family',base_url + '/main/content_more/tv/?gener=family&start=0','iwoSeriesIndex',artwork + '/genres/family.png')
        main.addDir('Fantasy',base_url + '/main/content_more/tv/?gener=fantasy&start=0','iwoSeriesIndex',artwork + '/genres/fantasy.png')
        main.addDir('Fashion',base_url + '/main/content_more/tv/?gener=fashion-make-up&start=0','iwoSeriesIndex',artwork + '/genres/fashion.png')
        main.addDir('Finance',base_url + '/main/content_more/tv/?gener=finance&start=0','iwoSeriesIndex',artwork + '/genres/finance.png')
        main.addDir('Fitness',base_url + '/main/content_more/tv/?gener=fitness&start=0','iwoSeriesIndex',artwork + '/genres/fitness.png')
        main.addDir('Garden',base_url + '/main/content_more/tv/?gener=garden-landscape&start=0','iwoSeriesIndex',artwork + '/genres/garden.png')
        main.addDir('History',base_url + '/main/content_more/tv/?gener=history&start=0','iwoSeriesIndex',artwork + '/genres/history.png')
        main.addDir('Horror',base_url + '/main/content_more/tv/?gener=horror-supernatural&start=0','iwoSeriesIndex',artwork + '/genres/horror.png')
        main.addDir('Interview',base_url + '/main/content_more/tv/?gener=interview&start=0','iwoSeriesIndex',artwork + '/genres/interview.png')
        main.addDir('Lifestyle',base_url + '/main/content_more/tv/?gener=lifestyle&start=0','iwoSeriesIndex',artwork + '/genres/lifestyle.png')
        main.addDir('Literature',base_url + '/main/content_more/tv/?gener=literature&start=0','iwoSeriesIndex',artwork + '/genres/literature.png')
        main.addDir('Medical',base_url + '/main/content_more/tv/?gener=medical&start=0','iwoSeriesIndex',artwork + '/genres/medical.png')
        main.addDir('Military',base_url + '/main/content_more/tv/?gener=military-war&start=0','iwoSeriesIndex',artwork + '/genres/military.png')
        main.addDir('Music',base_url + '/main/content_more/tv/?gener=music&start=0','iwoSeriesIndex',artwork + '/genres/music.png')
        main.addDir('Mystery',base_url + '/main/content_more/tv/?gener=mystery&start=0','iwoSeriesIndex',artwork + '/genres/mystery.png')
        main.addDir('Pets',base_url + '/main/content_more/tv/?gener=pets&start=0','iwoSeriesIndex',artwork + '/genres/pets.png')
        main.addDir('Politics',base_url + '/main/content_more/tv/?gener=politics&start=0','iwoSeriesIndex',artwork + '/genres/politics.png')
        main.addDir('Reality',base_url + '/main/content_more/tv/?gener=reality-tv&start=0','iwoSeriesIndex',artwork + '/genres/reality.png')
        main.addDir('Religion',base_url + '/main/content_more/tv/?gener=religion&start=0','iwoSeriesIndex',artwork + '/genres/religion.png')
        main.addDir('Romance',base_url + '/main/content_more/tv/?gener=romance-dating&start=0','iwoSeriesIndex',artwork + '/genres/romance.png')
        main.addDir('Sci-Fi',base_url + '/main/content_more/tv/?gener=sci-fi&start=0','iwoSeriesIndex',artwork + '/genres/sci-fi.png')
        main.addDir('Sketch',base_url + '/main/content_more/tv/?gener=sketch-improv&start=0','iwoSeriesIndex',artwork + '/genres/sketch.png')
        main.addDir('Soap Opera',base_url + '/main/content_more/tv/?gener=soaps-improv&start=0','iwoSeriesIndex',artwork + '/genres/soapopera.png')
        main.addDir('Sport',base_url + '/main/content_more/tv/?gener=sports&start=0','iwoSeriesIndex',artwork + '/genres/sport.png')
        main.addDir('Super Heroes',base_url + '/main/content_more/tv/?gener=super-heroes&start=0','iwoSeriesIndex',artwork + '/genres/superhero.png')
        main.addDir('Talent',base_url + '/main/content_more/tv/?gener=talent&start=0','iwoSeriesIndex',artwork + '/genres/talent.png')
        main.addDir('Teens',base_url + '/main/content_more/tv/?gener=teens&start=0','iwoSeriesIndex',artwork + '/genres/teens.png')
        main.addDir('Theatre',base_url + '/main/content_more/tv/?gener=cinema-theatre&start=0','iwoSeriesIndex',artwork + '/genres/theatre.png')
        main.addDir('Thriller',base_url + '/main/content_more/tv/?gener=thriller&start=0','iwoSeriesIndex',artwork + '/genres/thriller.png')
        main.addDir('Travel',base_url + '/main/content_more/tv/?gener=travel&start=0','iwoSeriesIndex',artwork + '/genres/travel.png')
        main.addDir('Vehicles',base_url + '/main/content_more/tv/?gener=automobiles-vehicles&start=0','iwoSeriesIndex',artwork + '/genres/vehicles.png')
        main.addDir('Western',base_url + '/main/content_more/tv/?gener=western&start=0','iwoSeriesIndex',artwork + '/genres/western.png')
        main.addDir('Wildlife',base_url + '/main/content_more/tv/?gener=wildlife&start=0','iwoSeriesIndex',artwork + '/genres/wildlife.png')
     
def HD_MOVIES():
        main.addDir('Recently Added',base_url +'/main/content_more/movies/?sort=latest&quality=hd&start=0','iwoIndex',artwork + '/main/recentlyadded.png')
        main.addDir('Popular',base_url + '/main/content_more/movies/?sort=popular&quality=hd&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('A-Z','none','iwoHDLetters',artwork + '/main/a-z.png')
        main.addDir('Genres','none','iwoHDGenres',artwork + '/main/genres.png')
        
def LETTERS():
        main.addDir('#',base_url + '/main/content_more/movies/?startwith=09&start=0','iwoIndex',artwork + '/letters/num.png')
        main.addDir('A',base_url + '/main/content_more/movies/?startwith=a&start=0','iwoIndex',artwork + '/letters/a.png')
        main.addDir('B',base_url + '/main/content_more/movies/?startwith=b&start=0','iwoIndex',artwork + '/letters/b.png')
        main.addDir('C',base_url + '/main/content_more/movies/?startwith=c&start=0','iwoIndex',artwork + '/letters/c.png')
        main.addDir('D',base_url + '/main/content_more/movies/?startwith=d&start=0','iwoIndex',artwork + '/letters/d.png')
        main.addDir('E',base_url + '/main/content_more/movies/?startwith=e&start=0','iwoIndex',artwork + '/letters/e.png')
        main.addDir('F',base_url + '/main/content_more/movies/?startwith=f&start=0','iwoIndex',artwork + '/letters/f.png')
        main.addDir('G',base_url + '/main/content_more/movies/?startwith=g&start=0','iwoIndex',artwork + '/letters/g.png')
        main.addDir('H',base_url + '/main/content_more/movies/?startwith=h&start=0','iwoIndex',artwork + '/letters/h.png')
        main.addDir('I',base_url + '/main/content_more/movies/?startwith=i&start=0','iwoIndex',artwork + '/letters/i.png')
        main.addDir('J',base_url + '/main/content_more/movies/?startwith=j&start=0','iwoIndex',artwork + '/letters/j.png')
        main.addDir('K',base_url + '/main/content_more/movies/?startwith=k&start=0','iwoIndex',artwork + '/letters/k.png')
        main.addDir('L',base_url + '/main/content_more/movies/?startwith=l&start=0','iwoIndex',artwork + '/letters/l.png')
        main.addDir('M',base_url + '/main/content_more/movies/?startwith=m&start=0','iwoIndex',artwork + '/letters/m.png')
        main.addDir('N',base_url + '/main/content_more/movies/?startwith=n&start=0','iwoIndex',artwork + '/letters/n.png')
        main.addDir('O',base_url + '/main/content_more/movies/?startwith=o&start=0','iwoIndex',artwork + '/letters/o.png')
        main.addDir('P',base_url + '/main/content_more/movies/?startwith=p&start=0','iwoIndex',artwork + '/letters/p.png')
        main.addDir('Q',base_url + '/main/content_more/movies/?startwith=q&start=0','iwoIndex',artwork + '/letters/q.png')
        main.addDir('R',base_url + '/main/content_more/movies/?startwith=r&start=0','iwoIndex',artwork + '/letters/r.png')
        main.addDir('S',base_url + '/main/content_more/movies/?startwith=s&start=0','iwoIndex',artwork + '/letters/s.png')
        main.addDir('T',base_url + '/main/content_more/movies/?startwith=t&start=0','iwoIndex',artwork + '/letters/t.png')
        main.addDir('U',base_url + '/main/content_more/movies/?startwith=u&start=0','iwoIndex',artwork + '/letters/u.png')
        main.addDir('V',base_url + '/main/content_more/movies/?startwith=v&start=0','iwoIndex',artwork + '/letters/v.png')
        main.addDir('W',base_url + '/main/content_more/movies/?startwith=w&start=0','iwoIndex',artwork + '/letters/w.png')
        main.addDir('X',base_url + '/main/content_more/movies/?startwith=x&start=0','iwoIndex',artwork + '/letters/x.png')
        main.addDir('Y',base_url + '/main/content_more/movies/?startwith=y&start=0','iwoIndex',artwork + '/letters/y.png')
        main.addDir('Z',base_url + '/main/content_more/movies/?startwith=z&start=0','iwoIndex',artwork + '/letters/z.png')

def HD_LETTERS():
        main.addDir('#',base_url + '/main/content_more/movies/?quality=hd&startwith=09&start=0','iwoIndex',artwork + '/letters/num.png')
        main.addDir('A',base_url + '/main/content_more/movies/?quality=hd&startwith=a&start=0','iwoIndex',artwork + '/letters/a.png')
        main.addDir('B',base_url + '/main/content_more/movies/?quality=hd&startwith=b&start=0','iwoIndex',artwork + '/letters/b.png')
        main.addDir('C',base_url + '/main/content_more/movies/?quality=hd&startwith=c&start=0','iwoIndex',artwork + '/letters/c.png')
        main.addDir('D',base_url + '/main/content_more/movies/?quality=hd&startwith=d&start=0','iwoIndex',artwork + '/letters/d.png')
        main.addDir('E',base_url + '/main/content_more/movies/?quality=hd&startwith=e&start=0','iwoIndex',artwork + '/letters/e.png')
        main.addDir('F',base_url + '/main/content_more/movies/?quality=hd&startwith=f&start=0','iwoIndex',artwork + '/letters/f.png')
        main.addDir('G',base_url + '/main/content_more/movies/?quality=hd&startwith=g&start=0','iwoIndex',artwork + '/letters/g.png')
        main.addDir('H',base_url + '/main/content_more/movies/?quality=hd&startwith=h&start=0','iwoIndex',artwork + '/letters/h.png')
        main.addDir('I',base_url + '/main/content_more/movies/?quality=hd&startwith=i&start=0','iwoIndex',artwork + '/letters/i.png')
        main.addDir('J',base_url + '/main/content_more/movies/?quality=hd&startwith=j&start=0','iwoIndex',artwork + '/letters/j.png')
        main.addDir('K',base_url + '/main/content_more/movies/?quality=hd&startwith=k&start=0','iwoIndex',artwork + '/letters/k.png')
        main.addDir('L',base_url + '/main/content_more/movies/?quality=hd&startwith=l&start=0','iwoIndex',artwork + '/letters/l.png')
        main.addDir('M',base_url + '/main/content_more/movies/?quality=hd&startwith=m&start=0','iwoIndex',artwork + '/letters/m.png')
        main.addDir('N',base_url + '/main/content_more/movies/?quality=hd&startwith=n&start=0','iwoIndex',artwork + '/letters/n.png')
        main.addDir('O',base_url + '/main/content_more/movies/?quality=hd&startwith=o&start=0','iwoIndex',artwork + '/letters/o.png')
        main.addDir('P',base_url + '/main/content_more/movies/?quality=hd&startwith=p&start=0','iwoIndex',artwork + '/letters/p.png')
        main.addDir('Q',base_url + '/main/content_more/movies/?quality=hd&startwith=q&start=0','iwoIndex',artwork + '/letters/q.png')
        main.addDir('R',base_url + '/main/content_more/movies/?quality=hd&startwith=r&start=0','iwoIndex',artwork + '/letters/r.png')
        main.addDir('S',base_url + '/main/content_more/movies/?quality=hd&startwith=s&start=0','iwoIndex',artwork + '/letters/s.png')
        main.addDir('T',base_url + '/main/content_more/movies/?quality=hd&startwith=t&start=0','iwoIndex',artwork + '/letters/t.png')
        main.addDir('U',base_url + '/main/content_more/movies/?quality=hd&startwith=u&start=0','iwoIndex',artwork + '/letters/u.png')
        main.addDir('V',base_url + '/main/content_more/movies/?quality=hd&startwith=v&start=0','iwoIndex',artwork + '/letters/v.png')
        main.addDir('W',base_url + '/main/content_more/movies/?quality=hd&startwith=w&start=0','iwoIndex',artwork + '/letters/w.png')
        main.addDir('X',base_url + '/main/content_more/movies/?quality=hd&startwith=x&start=0','iwoIndex',artwork + '/letters/x.png')
        main.addDir('Y',base_url + '/main/content_more/movies/?quality=hd&startwith=y&start=0','iwoIndex',artwork + '/letters/y.png')
        main.addDir('Z',base_url + '/main/content_more/movies/?quality=hd&startwith=z&start=0','iwoIndex',artwork + '/letters/z.png')

def GENRES():
        main.addDir('Action','none','iwoAction',artwork + '/genres/action.png')
        main.addDir('Adventure','none','iwoAdventure',artwork + '/genres/adventure.png')
        main.addDir('Animation','none','iwoAnimation',artwork + '/genres/animation.png')
        main.addDir('Biography','none','iwoBiography',artwork + '/genres/biography.png')
        main.addDir('Comedy','none','iwoComedy',artwork + '/genres/comedy.png')
        main.addDir('Crime','none','iwoCrime',artwork + '/genres/crime.png')
        main.addDir('Documentary','none','iwoDocumentary',artwork + '/genres/docs.png')
        main.addDir('Drama','none','iwoDrama',artwork + '/genres/drama.png')
        main.addDir('Family','none','iwoFamily',artwork + '/genres/family.png')
        main.addDir('Fantasy','none','iwoFantasy',artwork + '/genres/fantasy.png')
        main.addDir('Film-Noir','none','iwoFilmNoir',artwork + '/genres/film-noir.png')
        main.addDir('History','none','iwoHistory',artwork + '/genres/history.png')
        main.addDir('Horror','none','iwoHorror',artwork + '/genres/horror.png')
        main.addDir('Music','none','iwoMusic',artwork + '/genres/music.png')
        main.addDir('Musical','none','iwoMusical',artwork + '/genres/musical.png')
        main.addDir('Mystery','none','iwoMystery',artwork + '/genres/mystery.png')
        main.addDir('News','none','iwoNews',artwork + '/genres/news.png')
        main.addDir('Romance','none','iwoRomance',artwork + '/genres/romance.png')
        main.addDir('Sci-Fi','none','iwoSciFi',artwork + '/genres/sci-fi.png')
        main.addDir('Short','none','iwoShort',artwork + '/genres/short.png')
        main.addDir('Sport','none','iwoSport',artwork + '/genres/sport.png')
        main.addDir('Thriller','none','iwoThriller',artwork + '/genres/thriller.png')
        main.addDir('War','none','iwoWar',artwork + '/genres/war.png')
        main.addDir('Western','none','iwoWestern',artwork + '/genres/western.png')

def ACTION():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=action&sort=popular&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=action&sort=latest&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def ADVENTURE():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=adventure&sort=popular&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=adventure&sort=latest&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def ANIMATION():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=animation&sort=popular&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=animation&sort=latest&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def BIOGRAPHY():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=biography&sort=popular&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=biography&sort=latest&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def COMEDY():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=comedy&sort=popular&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=comedy&sort=latest&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def CRIME():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=crime&sort=popular&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=crime&sort=latest&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def DOCUMENTARY():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=documentary&sort=popular&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=documentary&sort=latest&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def DRAMA():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=drama&sort=popular&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=drama&sort=latest&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def FAMILY():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=family&sort=popular&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=family&sort=latest&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def FANTASY():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=fantasy&sort=popular&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=fantasy&sort=latest&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def FILMNOIR():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=film-noir&sort=popular&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=film-noir&sort=latest&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def HISTORY():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=history&sort=popular&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=history&sort=latest&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def HORROR():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=horror&sort=popular&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=horror&sort=latest&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def MUSIC():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=music&sort=popular&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=music&sort=latest&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def MUSICAL():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=musical&sort=popular&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=musical&sort=latest&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def MYSTERY():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=mystery&sort=popular&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=mystery&sort=latest&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def NEWS():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=news&sort=popular&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=news&sort=latest&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def ROMANCE():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=romance&sort=popular&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=romance&sort=latest&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def SCIFI():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=sci-fi&sort=popular&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=sci-fi&sort=latest&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def SHORT():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=short&sort=popular&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=short&sort=latest&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def SPORT():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=sport&sort=popular&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=sport&sort=latest&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def THRILLER():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=thriller&sort=popular&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=thriller&sort=latest&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def WAR():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=war&sort=popular&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=war&sort=latest&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def WESTERN():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=western&sort=popular&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=western&sort=latest&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def HD_GENRES():
        main.addDir('Action','none','iwoHDAction',artwork + '/genres/action.png')
        main.addDir('Adventure','none','iwoHDAdventure',artwork + '/genres/adventure.png')
        main.addDir('Animation','none','iwoHDAnimation',artwork + '/genres/animation.png')
        main.addDir('Biography','none','iwoHDBiography',artwork + '/genres/biography.png')
        main.addDir('Comedy','none','iwoHDComedy',artwork + '/genres/comedy.png')
        main.addDir('Crime','none','iwoHDCrime',artwork + '/genres/crime.png')
        main.addDir('Documentary','none','iwoHDDocumentary',artwork + '/genres/docs.png')
        main.addDir('Drama','none','iwoHDDrama',artwork + '/genres/drama.png')
        main.addDir('Family','none','iwoHDFamily',artwork + '/genres/family.png')
        main.addDir('Fantasy','none','iwoHDFantasy',artwork + '/genres/fantasy.png')
        main.addDir('Film-Noir','none','iwoHDFilmNoir',artwork + '/genres/film-noir.png')
        main.addDir('History','none','iwoHDHistory',artwork + '/genres/history.png')
        main.addDir('Horror','none','iwoHDHorror',artwork + '/genres/horror.png')
        main.addDir('Music','none','iwoHDMusic',artwork + '/genres/music.png')
        main.addDir('Musical','none','iwoHDMusical',artwork + '/genres/musical.png')
        main.addDir('Mystery','none','iwoHDMystery',artwork + '/genres/mystery.png')
        main.addDir('News','none','iwoHDNews',artwork + '/genres/news.png')
        main.addDir('Romance','none','IwoHDRomance',artwork + '/genres/romance.png')
        main.addDir('Sci-Fi','none','iwoHDSciFi',artwork + '/genres/sci-fi.png')
        main.addDir('Short','none','iwoHDShort',artwork + '/genres/short.png')
        main.addDir('Sport','none','iwoHDSport',artwork + '/genres/sport.png')
        main.addDir('Thriller','none','iwoHDThriller',artwork + '/genres/thriller.png')
        main.addDir('War','none','iwoHDWar',artwork + '/genres/war.png')
        main.addDir('Western','none','iwoHDWestern',artwork + '/genres/western.png')

def HD_ACTION():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=action&sort=popular&quality=hd&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=action&sort=latest&quality=hd&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def HD_ADVENTURE():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=adventure&sort=popular&quality=hd&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=adventure&sort=latest&quality=hd&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def HD_ANIMATION():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=animation&sort=popular&quality=hd&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=animation&sort=latest&quality=hd&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def HD_BIOGRAPHY():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=biography&sort=popular&quality=hd&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=biography&sort=latest&quality=hd&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def HD_COMEDY():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=comedy&sort=popular&quality=hd&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=comedy&sort=latest&quality=hd&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def HD_CRIME():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=crime&sort=popular&quality=hd&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=crime&sort=latest&quality=hd&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def HD_DOCUMENTARY():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=documentary&sort=popular&quality=hd&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=documentary&sort=latest&quality=hd&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def HD_DRAMA():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=drama&sort=popular&quality=hd&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=drama&sort=latest&quality=hd&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def HD_FAMILY():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=family&sort=popular&quality=hd&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=family&sort=latest&quality=hd&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def HD_FANTASY():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=fantasy&sort=popular&quality=hd&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=fantasy&sort=latest&quality=hd&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def HD_FILMNOIR():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=film-noir&sort=popular&quality=hd&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=film-noir&sort=latest&quality=hd&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def HD_HISTORY():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=history&sort=popular&quality=hd&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=history&sort=latest&quality=hd&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def HD_HORROR():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=horror&sort=popular&quality=hd&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=horror&sort=latest&quality=hd&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def HD_MUSIC():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=music&sort=popular&quality=hd&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=music&sort=latest&quality=hd&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def HD_MUSICAL():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=musical&sort=popular&quality=hd&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=musical&sort=latest&quality=hd&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def HD_MYSTERY():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=mystery&sort=popular&quality=hd&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=mystery&sort=latest&quality=hd&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def HD_NEWS():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=news&sort=popular&quality=hd&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=news&sort=latest&quality=hd&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def HD_ROMANCE():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=romance&sort=popular&quality=hd&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=romance&sort=latest&quality=hd&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def HD_SCIFI():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=sci-fi&sort=popular&quality=hd&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=sci-fi&sort=latest&quality=hd&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def HD_SHORT():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=short&sort=popular&quality=hd&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=short&sort=latest&quality=hd&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def HD_SPORT():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=sport&sort=popular&quality=hd&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=sport&sort=latest&quality=hd&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def HD_THRILLER():
        main.addDir('Popular',base_url + '/mai/main/content_more/movies/?gener=thriller&sort=popular&quality=hd&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=thriller&sort=latest&quality=hd&start=0','iwoIndex',artwork + '/main/recentlyadded.png')

def HD_WAR():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=war&sort=popular&quality=hd&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=war&sort=latest&quality=hd&start=0','iwoIndex',artwork + 'recentlyadded.png')

def HD_WESTERN():
        main.addDir('Popular',base_url + '/main/content_more/movies/?gener=western&sort=popular&quality=hd&start=0','iwoIndex',artwork + '/main/popular.png')
        main.addDir('Recently Added',base_url + '/main/content_more/movies/?gener=western&sort=latest&quality=hd&start=0','iwoIndex',artwork + '/main/recentlyadded.png')
        
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
                main.addDir('Next Page',next_page,'iwoIndex',artwork + '/main/next.png')
        
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
                        main.addMDir(name,url,'iwoVideoLinks',thumbnail,year,False)
                except:
                        continue
        main.AUTOVIEW('movies')

def SERIES_INDEX(url):
        a,b,c = url.partition('&start=')
        next_page_number = int(c) + 25
        next_page = a+b+str(next_page_number)
        print'tttttttt'+url
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('<a href="(.+?)" class=".+?" rel=".+?">\r\n\t\t\t\t\t\t\t<img class=".+?" src="(.+?)" alt="">\r\n\t\t\t\t\t\t\t <div class=".+?">.+?</div>\t  \r\n\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t<div class=".+?">.+?').findall(link)
        d,e,f = url.partition('=latest&start=')
        if len(match) >24:
                main.addDir('Next Page',next_page,'iwoSeriesIndex',artwork + '/main/next.png')
        
        for url,thumbnail in match:
                head,sep,tail = url.partition('/tv-shows/')
                head,sep,tail = url.partition('-')
                split = re.split('\d\d\d\d\d-',tail)
                try:
                        name = str(split[1])
                except:
                        continue
                name = name.replace('-',' ')
                name = name.title()

                if name == 'Battlestar Galactica':
                        name = 'Battlestar Galactica (2003)'
        
                try:
                        main.addSDir(name,url,'iwoEpisodesIndex',thumbnail,False)
                except:
                        continue
        main.AUTOVIEW('tvshows')

def EPISODES_INDEX(url,name):
        show = name
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('<a href="(.+?)"><i class="icon-play-circle"></i>.+?</a></td>\r\n\t\t\t\t\t\t\t  <td>(.+?)</td>\r\n\t\t\t\t\t\t\t  <td><div class="pull-right"><div class="star" data-rating=".+?">').findall(link)
        for url,name in match:
                s,e = main.GET_EPISODE_NUMBERS(url)
                s = 'S' + s
                e = 'E' + e
                se = s+e
                name = name + ' ' + se
                print s+e
                try:
                        main.addEDir(name,url,'iwoVideoLinks','',show)
                except:
                        continue
        main.AUTOVIEW('episodes')

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
                                        main.addHDir(name,str(urls[0]),'resolve',thumb,hthumb)
                                        inc +=1
                                except:
                                        continue
                



