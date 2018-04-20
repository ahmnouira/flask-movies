from flask import Flask, jsonify
from pymongo import MongoClient
from movies import MovieCollection


app = Flask(__name__)
client = MongoClient('mongodb://localhost')
database = client.video
movie_collection = MovieCollection(database)


@app.route('/movies')
def movies_list():
    """Return a list of movies."""
    return jsonify(movie_collection.list())


@app.route('/movies/<imdb>')
def movies_retrieve(imdb):
    """Return a specific movie based on IMDB id."""
    return jsonify(movie_collection.read(imdb))


if __name__ == '__main__':
    app.run()
