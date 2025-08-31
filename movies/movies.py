import requests
import json

API_KEY = "ca2dd883"
def search_movie(keyword):
    try:
        data = requests.get(f"https://www.omdbapi.com/?t={keyword}&apikey={API_KEY}")
        movie_data = json.loads(data.text)
        print(
            f"""
        Movie actors: {movie_data['Actors']}
        Movie writer: {movie_data['Writer']}
        Movie genre: {movie_data['Genre']}
        Movie year: {movie_data['Year']}
        Movie plot: {movie_data['Plot']}
        Movie length: {movie_data['Runtime']}
        Movie rating: {movie_data['imdbRating']}
        Movie awards: {movie_data['Awards']}
        Movie released: {movie_data['Released']}
        """
        )
    except requests.exceptions.RequestException as e:
        print(e)
while True:
    movie_name = input("Movie name: ")
    search_movie(movie_name)
