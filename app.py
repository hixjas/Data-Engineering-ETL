from flask import Flask, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/columbusdata_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Models
class Community(db.Model):
    __tablename__ = 'community'
    community_id = db.Column(db.Float, primary_key=True)
    community_name = db.Column(db.String(255))
    community_no = db.Column(db.Float)
    global_id = db.Column(db.String(255))
    businesses = db.relationship('Business', backref='community', lazy=True)

class Business(db.Model):
    __tablename__ = 'business'
    business_id = db.Column(db.Integer, primary_key=True)
    business_name = db.Column(db.String(255))
    business_type = db.Column(db.String(255))
    address = db.Column(db.String(255))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    community_id = db.Column(db.Float, db.ForeignKey('community.community_id'))

# Routes
@app.route('/')
def home():
    return """
    <h1>Columbus Business Locator API</h1>
    <p>Available endpoints:</p>
    <ul>
        <li><a href="/api/businesses">/api/businesses</a> - List all businesses</li>
        <li><a href="/api/communities">/api/communities</a> - List all communities</li>
    </ul>
    """

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )

@app.route('/api/businesses', methods=['GET'])
def get_businesses():
    businesses = Business.query.all()
    return jsonify([{
        'business_id': biz.business_id,
        'name': biz.business_name,
        'type': biz.business_type,
        'address': biz.address,
        'coordinates': [biz.latitude, biz.longitude]
    } for biz in businesses])

if __name__ == '__main__':
    os.makedirs(os.path.join(app.root_path, 'static'), exist_ok=True)
    app.run(debug=True)
