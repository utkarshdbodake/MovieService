'''
Created on 29-Aug-2015

@author: utkarsh
'''
from django.conf.urls import url
from movie_service.service_apis.movies_search import MovieSearch

urlpatterns = [
    url(r'^movies/search/$', MovieSearch.as_view()), 
]