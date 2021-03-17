import requests
import json


api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkZGEzYzhhYmEyODVhZDBhZjYxM2E5NmEyMWZlMDllNiIsInN1YiI6IjYwMmQzNWVhZDRiOWQ5MDAzZmQyOWY1MiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.oDchyvN4gbwaNHGH2QsEs2mJiUGJStE76Rvby3CY3kU"


# TOP RATED MOVIES
def get_top_rated_movies():
    endpoint = "https://api.themoviedb.org/3/movie/top_rated"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

# UPCOMING MOVIES
def get_upcoming_movies():
    endpoint = "https://api.themoviedb.org/3/movie/upcoming"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()   

# POPULAR MOVIES
def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

 # MOVIES NOW PLAYING
def get_now_playing_movies():
    endpoint = "https://api.themoviedb.org/3/movie/now_playing"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()  

# MOVIE DETAILS    
def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_movies(how_many, list_type):
    if list_type == "popular":
        data = get_popular_movies()
    elif list_type =="top_rated":
        data = get_top_rated_movies()
    elif list_type == "upcoming":
        data = get_upcoming_movies()
    elif list_type == "now_playing":
        data = get_now_playing_movies()
    return data["results"][:how_many]


def get_movies_list(list_type):
    endpoint = "https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    
    return response.json()


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"



def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_single_movie_cast(movie_id, how_many):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"][:how_many]


def search(search_query):
    base_url = "https://api.themoviedb.org/3/"
    endpoint = f"{base_url}search/movie/?query={search_query}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    response =  response.json()
    return response["results"]


def get_airing_today():
    endpoint = f"https://api.themoviedb.org/3/tv/airing_today"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    response = response.json()
    return response['results']