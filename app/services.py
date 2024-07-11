from .models import db, Movie


def add_movie(title, director, release_date):
    new_movie = Movie(title=title, director=director, release_date=release_date)
    db.session.add(new_movie)
    db.session.commit()
    return new_movie


def get_all_movies():
    return Movie.query.all()


def get_movie_by_id(id):
    return Movie.query.get_or_404(id)


def update_movie(id, title, director, release_date):
    movie = Movie.query.get_or_404(id)
    movie.title = title
    movie.director = director
    movie.release_date = release_date
    db.session.commit()
    return movie


def delete_movie(id):
    movie = Movie.query.get_or_404(id)
    db.session.delete(movie)
    db.session.commit()
