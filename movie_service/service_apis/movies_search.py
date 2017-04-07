'''
Created on 28-Aug-2015

@author: utkarsh
'''
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from movie_service.models import Movie
from movie_service.service_api_handlers.get_movie_search_handler import handle_request
from movie_service.utils.logger import logger
import json
import traceback


class MovieSearch(APIView):

    def get(self, request):
        '''
        Gets the matching movie list w.r.t. the query data
        '''
        try:
            logger.info("GET Search movies %s" % (request.GET.values()[0]))
            request_dict = json.loads(request.GET.values()[0])

            movie_ids = []
            is_lone_value = True
            if "movie_name" in request_dict.keys():
                movie_tmp_ids = (Movie.objects.filter(name__icontains=request_dict['movie_name']).
                                    values_list('id', flat=True))
                movie_ids.extend(movie_tmp_ids)
                is_lone_value = False

            if "director" in request_dict.keys():
                if movie_ids:
                    movie_tmp_ids = (Movie.objects.filter(director__name__icontains=request_dict['director'],
                                                          id__in=movie_ids).values_list('id', flat=True))
                    movie_ids = list(set(movie_tmp_ids).intersection(movie_ids))
                elif is_lone_value:
                    movie_ids = (Movie.objects.filter(director__name__icontains=request_dict['director']).
                                    values_list('id', flat=True))
                is_lone_value = False

            if "genre" in request_dict.keys():
                if movie_ids:
                    movie_tmp_ids = (Movie.objects.filter(genre__name__icontains=request_dict['genre'],
                                                          id__in=movie_ids).values_list('id', flat=True))
                    movie_ids = list(set(movie_tmp_ids).intersection(movie_ids))
                elif is_lone_value:
                    movie_ids = (Movie.objects.filter(genre__name__icontains=request_dict['genre']).
                                    values_list('id', flat=True))
                is_lone_value = False
        
            if "imdb_score" in request_dict.keys():
                if movie_ids:
                    movie_tmp_ids = (Movie.objects.filter(imdb_score=request_dict['imdb_score'],
                                                          id__in=movie_ids).values_list('id', flat=True))
                    movie_ids = list(set(movie_tmp_ids).intersection(movie_ids))
                elif is_lone_value:
                    movie_ids = (Movie.objects.filter(imdb_score=request_dict['imdb_score']).
                                    values_list('id', flat=True))
                is_lone_value = False

            if "popularity" in request_dict.keys():
                if movie_ids:
                    movie_tmp_ids = (Movie.objects.filter(popularity=request_dict['popularity'],
                                                          id__in=movie_ids).values_list('id', flat=True))
                    movie_ids = list(set(movie_tmp_ids).intersection(movie_ids))
                elif is_lone_value:
                    movie_ids = (Movie.objects.filter(popularity=request_dict['popularity']).
                                    values_list('id', flat=True))
                is_lone_value = False

            movies = Movie.objects.filter(id__in=movie_ids)
            if movies:
                return handle_request(movies)
            else:
                logger.info("No entries in DB for given query data")
                return Response("No Results matching the search query",
                                status.HTTP_204_NO_CONTENT)
        except:
            logger.error(traceback.format_exc())
            return Response("Error", status.HTTP_500_INTERNAL_SERVER_ERROR)
