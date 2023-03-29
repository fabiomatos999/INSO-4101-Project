from . import db
from flask_login import UserMixin
import hashlib

#defining the tables
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(150))
    isSeller = db.Column(db.boolean, default=False)
    
    
class Sneaker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(100))
    model_name = db.Column(db.String(100))
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    size = db.Column(db.Float)
    color = db.Column(db.String(50))
    image_url = db.Column(db.String(255))
    
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    status = db.Column(db.String(50))
    shipping_address = db.Column(db.Text)
    total_price = db.Column(db.Float)

    user = db.relationship('User', backref='orders')
    
class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    sneaker_id = db.Column(db.Integer, db.ForeignKey('sneaker.id'))
    quantity = db.Column(db.Integer)

    order = db.relationship('Order', backref='order_items')
    sneaker = db.relationship('Sneaker', backref='order_items')
    
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    sneaker_id = db.Column(db.Integer, db.ForeignKey('sneaker.id'))
    rating = db.Column(db.Integer)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref='reviews')
    sneaker = db.relationship('Sneaker', backref='reviews')