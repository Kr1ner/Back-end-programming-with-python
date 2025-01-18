from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "496ea68f85a47064ed2679131184343c"
BASE_URL = "https://api.themoviedb.org/3"
IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"

def get_movies(query):
    url = f"{BASE_URL}/search/movie"
    params = {"api_key": API_KEY, "query": query}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get("results", [])
    return []

def get_movie_details(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}"
    params = {"api_key": API_KEY}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return {}

@app.route("/")
def home():
    response = requests.get(f"{BASE_URL}/movie/popular?api_key={API_KEY}&language=en-US&page=1")
    movies = response.json().get('results', [])
    return render_template("home.html", movies=movies)

@app.route("/search")
def search():
    query = request.args.get("query", "")
    movies = get_movies(query) if query else []
    return render_template("search.html", query=query, movies=movies, image_base_url=IMAGE_BASE_URL)

@app.route("/movie/<int:movie_id>")
def movie_details(movie_id):
    movie = get_movie_details(movie_id)
    return render_template("movie.html", movie=movie, image_base_url=IMAGE_BASE_URL)

if __name__ == "__main__":
    app.run(debug=True)
