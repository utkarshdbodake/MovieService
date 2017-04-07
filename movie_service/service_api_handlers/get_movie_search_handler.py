'''
Created on 29-Aug-2015

@author: utkarsh
'''
from rest_framework.response import Response
from movie_service.utils.logger import logger
import traceback


def handle_request(movies):
    try:
        movie_list = []
        for movie in movies:
            movie_map = {}
            movie_map["name"] = movie.name
            movie_map["director"] = movie.director.name
            movie_map["imdb_score"] = movie.imdb_score
            movie_map["99popularity"] = movie.popularity
            genre_list = []
            for genre in movie.genre.all():
                genre_list.append(genre.name)
            movie_map["genre"] = genre_list
            movie_list.append(movie_map)
        return Response({"size": len(movie_list),
                         "result": movie_list})
    except:
        logger.info(traceback.format_exc())
