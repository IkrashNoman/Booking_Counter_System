from app import db
import enum

class BookingStatus(enum.Enum):
    PENDING = "PENDING"      # User is at the checkout page
    CONFIRMED = "CONFIRMED"  # Payment successful, ticket is valid
    FAILED = "FAILED"        # Payment failed or timeout occurred

class SeatStatus(enum.Enum):
    BOOKED='BOOKED'
    LOCKED='LOCKED'
    AVAILABLE="AVAILABLE"


class Booking(db.Model):
    __tablename__='bookings'
    booking_id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    show_id=db.Column(db.Integer, db.ForeignKey('shows.show_id'), nullable=False)
    booking_date=db.Column(db.DateTime, nullable=False)
    booking_status=db.Column(db.Enum(BookingStatus), 
                             nullable=False,
                             default=BookingStatus.PENDING)
    user = db.relationship('User', backref='bookings')
    show = db.relationship('Show', backref='bookings')

class ShowSeat(db.Model):
    __tablename__ = 'show_seats'
    show_seats_id = db.Column(db.Integer, primary_key=True)
    show_id = db.Column(db.Integer, db.ForeignKey('shows.show_id'), nullable=False)
    seat_id = db.Column(db.Integer, db.ForeignKey('seats.seat_id'), nullable=False)
    booking_id = db.Column(db.Integer, db.ForeignKey('bookings.booking_id'), nullable=True)
    status = db.Column(db.Enum(SeatStatus), nullable=False, default=SeatStatus.AVAILABLE)
    locked_at = db.Column(db.DateTime, nullable=True)
    
    __table_args__ = (
        db.UniqueConstraint('show_id', 'seat_id', name='uq_show_seat'),
    )
    
    seat = db.relationship('Seat', backref='show_seats')
    show = db.relationship('Show', backref='show_seats')
    booking = db.relationship('Booking', backref='show_seats')