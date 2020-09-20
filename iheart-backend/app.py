from flask import Flask, request, jsonify

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init DB
db = SQLAlchemy(app)

# Init Marshmallow
ma = Marshmallow(app)

# Song Class/Model


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    artist = db.Column(db.String(100))
    genre = db.Column(db.String(100))
    year = db.Column(db.Integer)

    def __init__(self, title, artist, genre, year):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.year = year

# Song Schema


class SongSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'artist', 'genre', 'year')


# Init Schema
song_schema = SongSchema()
songs_schema = SongSchema(many=True)

# Create Song


@app.route('/song', methods=['POST'])
def add_song():
    title = request.json['title']
    artist = request.json['artist']
    genre = request.json['genre']
    year = request.json['year']

    new_song = Song(title, artist, genre, year)
    db.session.add(new_song)
    db.session.commit()
    return song_schema.jsonify(new_song)

# Get all Songs


@app.route('/song', methods=['GET'])
def get_songs():
    all_songs = Song.query.all()
    result = songs_schema.dump(all_songs)
    return jsonify(result)


# Run Server
if __name__ == '__main__':
    app.run(debug=True)
