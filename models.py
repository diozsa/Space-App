from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class User(db.Model):
    """User model"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

    images = db.relationship("Image", backref="user", cascade="all, delete")


    @classmethod
    def register(cls, username, password):
        """Registers new user with hashed password
            and returns user
        """

        hashed = bcrypt.generate_password_hash(password)
        hashed_utf8 = hashed.decode("utf8")

        return cls(username=username, password=hashed_utf8)


    @classmethod
    def authenticate(cls, username, password):
        """Validate username exists and password is correct
            Returns user id valid, otherwise False
        """

        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            return False

    
class Image(db.Model):
    """Image model"""

    __tablename__ = "images"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # id = db.Column(db.String(100), primary_key=True, nullable=False, unique=True)
    nasa_id = db.Column(db.String(255))
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    photographer = db.Column(db.String(255))
    creator = db.Column(db.String(255))
    thumbnail = db.Column(db.String(255))
    full_size = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    


