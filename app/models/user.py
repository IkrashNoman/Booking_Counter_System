from app import db

class User(db.Model):
    __tablename__ = 'users'
    
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    cnic=db.Column(db.String(16), unique=True, nullable=False)
    email=db.Column(db.String(120), unique=True, nullable=False)
    password_hash=db.Column(db.String(255), nullable=False)

    bookings = db.relationship('Booking', backref='user', lazy=True)