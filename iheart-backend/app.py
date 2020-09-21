from flask import Flask, request, jsonify

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import os

# Init app

app = Flask(__name__)
CORS(app)
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

# Db creation flask commands


@app.cli.command('db_create')
def db_create():
    db.create_all()
    print('Database Created!')


@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print('Database Dropped!')


@app.cli.command('db_seed')
def db_seed():
    song1 = Song(title='Pretty Boy', artist='The Neighbourhood',
                 genre='Alternative', year=2020)
    song2 = Song(title='Tui', artist='FKJ', genre='Electronic', year=2018)
    song3 = Song(title='Love Bomb', artist='East Forrest',
                 genre='Electronic', year=2012)
    song4 = Song(title='Years', artist='DRAMA', genre='Electronic', year=2020)
    song5 = Song(title='Cinnamon', artist='Jome',
                 genre='Alternative', year=2016)
    song6 = Song(title='Liminal', artist='The Acid',
                 genre='Alternative', year=2016)
    song7 = Song(title='ii', artist='Aquilo', genre='Alternative', year=2017)
    song8 = Song(title='Pacific II', artist='Goth Babe',
                 genre='Alternative', year=2018)
    song9 = Song(title='Summers Gone', artist='Nombe',
                 genre='Alternative', year=2018)
    song10 = Song(title='Its okay, youre okay', artist='Bonjr',
                  genre='Alternative', year=2018)
    song11 = Song(title='Distance', artist='Hippie Sabotage',
                  genre='Electronic', year=2018)
    song12 = Song(title='Notion', artist='Tash Saltuna',
                  genre='Alternative', year=2016)
    song13 = Song(title='Mutual Love', artist='Shallou',
                  genre='Electronic', year=2020)
    song14 = Song(title='Dance', artist='Aaron Smith',
                  genre='Dance', year=2014)

    db.session.add(song1)
    db.session.add(song2)
    db.session.add(song3)
    db.session.add(song4)
    db.session.add(song5)
    db.session.add(song6)
    db.session.add(song7)
    db.session.add(song8)
    db.session.add(song9)
    db.session.add(song10)
    db.session.add(song11)
    db.session.add(song12)
    db.session.add(song13)
    db.session.add(song14)

    db.session.commit()
    print('Database Seeded!')

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

# Get single Song


@app.route('/song/<id>', methods=['GET'])
def get_song(id):
    song = Song.query.get(id)
    return song_schema.jsonify(song)

# Update a Product


@app.route('/song/<id>', methods=['PUT'])
def update_song(id):
    song = Song.query.get(id)

    title = request.json['title']
    artist = request.json['artist']
    genre = request.json['genre']
    year = request.json['year']

    song.title = title
    song.artist = artist
    song.genre = genre
    song.year = year

    db.session.commit()
    return song_schema.jsonify(song)


# Delete Product
@app.route('/song/<id>', methods=['DELETE'])
def delete_song(id):
    song = Song.query.get(id)
    db.session.delete(song)
    db.session.commit()
    return song_schema.jsonify(song)


# Run Server
if __name__ == '__main__':
    app.run(debug=True)
