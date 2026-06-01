from app import db

class Cinema(db.Model):
    __tablename__ = 'cinemas'
    cinema_id=db.Column(db.Integer, primary_key=True)
    cinema_name=db.Column(db.String(150), nullable=False)
    cinema_address=db.Column(db.String(200), nullable=False)
    cinema_location=db.Column(db.String(100), nullable=False)

    def full_cinema_info(self):
        return f"{self.cinema_name}, {self.cinema_address}, {self.cinema_location}"
    

class Screen(db.Model):
    __tablename__ = 'screens'
    screen_id=db.Column(db.Integer, primary_key=True)
    cinema_id=db.Column(db.Integer, db.ForeignKey('cinemas.cinema_id'), nullable=False)
    screen_name=db.Column(db.String(150), nullable=False)
    capacity=db.Column(db.Integer, nullable=False)
    def unique_screen(self):
        return f"{self.cinema_id}, {self.screen_name}"
    
class Seat(db.Model):
    __tablename__ = 'seats'
    seat_id = db.Column(db.Integer, primary_key=True)
    screen_id = db.Column(db.Integer, db.ForeignKey('screens.screen_id'), nullable=False)
    seat_number = db.Column(db.Integer, nullable=False)
    seat_type = db.Column(db.String(10), nullable=False)
    
    __table_args__ = (
        db.UniqueConstraint('screen_id', 'seat_number', name='uq_screen_seat_number'),
        db.CheckConstraint('seat_number > 0 AND seat_number < 100', name='check_seat_number_range'),
    )