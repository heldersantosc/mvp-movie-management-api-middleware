from flask import Blueprint, request, jsonify
from .services import *

movies_bp = Blueprint("movies", __name__, url_prefix="/movies")


@movies_bp.route("/", methods=["POST"])
def add_movie_route():
    data = request.json
    new_movie = add_movie(data["title"], data["director"], data["release_date"])
    return (
        jsonify(
            {
                "id": new_movie.id,
                "title": new_movie.title,
                "director": new_movie.director,
                "release_date": new_movie.release_date,
            }
        ),
        201,
    )


@movies_bp.route("/", methods=["GET"])
def get_movies_route():
    movies = get_all_movies()
    return jsonify(
        [
            {
                "id": movie.id,
                "title": movie.title,
                "director": movie.director,
                "release_date": movie.release_date,
            }
            for movie in movies
        ]
    )


@movies_bp.route("/<int:id>", methods=["GET"])
def get_movie_route(id):
    movie = get_movie_by_id(id)
    return jsonify(
        {
            "id": movie.id,
            "title": movie.title,
            "director": movie.director,
            "release_date": movie.release_date,
        }
    )


@movies_bp.route("/<int:id>", methods=["PUT"])
def update_movie_route(id):
    data = request.json
    updated_movie = update_movie(
        id, data["title"], data["director"], data["release_date"]
    )
    return jsonify(
        {
            "id": updated_movie.id,
            "title": updated_movie.title,
            "director": updated_movie.director,
            "release_date": updated_movie.release_date,
        }
    )


@movies_bp.route("/<int:id>", methods=["DELETE"])
def delete_movie_route(id):
    delete_movie(id)
    return "", 204
