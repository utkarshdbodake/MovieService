'''
Created on 29-Aug-2015

@author: utkarsh
'''
import json
from movie_service.models import Movie, Director, Genre
import traceback
import django
django.setup()

imdb = json.load(open('movie_service/imdb.json'))


def insert_director(imdb):
    director_list = []
    for entry in imdb:
        director_list.append(entry['director'])
    director_list = list(set(director_list))

    for director_name in director_list:
        try:
            director_obj = Director.objects.get_or_create(name=director_name.strip())
            director_obj.save()
        except:
            print "director omg"

for e in Director.objects.all():
    print e.name
 
print "*"*50
###########################

def insert_genre(imdb):
    genre_list = []
    for entry in imdb:
        genre_list.extend(entry['genre'])

    genre_list = list(set(genre_list))
    for genre_name in genre_list:
        try:
            genre_obj = Genre.objects.get_or_create(name=genre_name.strip())
            genre_obj.save()
        except:
            print "genre omg"


for e in Genre.objects.all():
    print e.name

print "*"*50
###########################

def insert_movies(imdb):
    for entry in imdb:
        popularity = entry['99popularity']
        director = entry['director']
        genres = entry['genre']
        imdb_score = entry['imdb_score']
        movie_name = entry['name']
    
        try:
            director_obj = Director.objects.filter(name=entry['director'].strip())[0]
            try:
                movie, created = Movie.objects.get_or_create(name=entry['name'].strip(),
                                                             director_id=director_obj.id)
                
                movie.director = director_obj
                movie.imdb_score = entry['imdb_score']
                movie.popularity = entry['99popularity']
                print "*"*50
                movie.save()
            except:
                print "movie1 omg" 
            try:
                genres_tmp_list = []
                for genre in entry['genre']:
                    genres_tmp_list.append(genre.strip())
                genre_list = Genre.objects.filter(name__in=genres_tmp_list)
                print len(genre_list)
                movie.genre = genre_list
                movie.save()
            except Exception:
#                 movie.delete()
                print traceback.format_exc()
        except Exception, e:
            print traceback.format_exc()


for e in Movie.objects.all():
    print e.__dict__

# Movie.objects.all().delete()
# Genre.objects.all().delete()
# Director.objects.all().delete()

insert_director(imdb)
insert_genre(imdb)
insert_movies(imdb)

