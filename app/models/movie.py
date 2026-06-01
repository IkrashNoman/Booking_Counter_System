from app import db

class Movie(db.Model):
    __tablename__ = 'movies'
    movie_id=db.Column(db.Integer, primary_key=True)
    movie_name=db.Column(db.String(300), unique=True, nullable=False)
    movie_duration=db.Column(db.Integer, nullable=False)
    movie_description=db.Column(db.String(10000), nullable=False)
    movie_rating = db.Column(db.Float)
    genre=db.Column(db.String(100))
    languages = db.Column(db.String(255), nullable=False)
    release_date = db.Column(db.DateTime)
    poster_url=db.Column(db.String(300))


class Show(db.Model):
    __tablename__='shows'
    show_id=db.Column(db.Integer, primary_key=True)
    movie_id=db.Column(db.Integer, db.ForeignKey('movies.movie_id'), nullable=False)
    screen_id=db.Column(db.Integer, db.ForeignKey('screens.screen_id'), nullable=False)
    show_date=db.Column(db.Date, nullable=False)
    show_time=db.Column(db.Time, nullable=False) 
    ticket_price=db.Column(db.Integer, nullable=False)
