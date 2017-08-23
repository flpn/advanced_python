import peewee
from datetime import date
from general_topics.database.orm_example.models import Album, Song

db = peewee.SqliteDatabase('mydb.db')
db.connect()

db.drop_tables([Album, Song])
db.create_tables([Album, Song])


# INSERT SOME DATA INTO TABLES
new_album = Album.create(name='Repentless', artist='Slayer', release=date(2015, 9, 1))
song_one = Song(album=new_album, name='Delusions of Saviour', length=1.55)
song_one.save()

songs = [
    {'album': new_album,
     'name': 'You against you',
     'length': 5.34
     },
    {'album': new_album,
     'name': 'Repentless',
     'length': 4.21
     },
    {'album': new_album,
     'name': 'Pride in prejudice',
     'length': 3.3
     }]

Song.insert_many(songs).execute()


# RETRIEVING DATA
album = Album.select().where(Album.id == 1).get()
print(album)

# all table
for song in Song.select():
    print(song)

# shortcut and update
album = Album.get(Album.id == 1)
print(album)
album.name = 'Reign in Blood'
album.save()
print(album)

# working with foreign key
song = Song.select().where(Song.id == 1).get()
print(song.album.name)

# select with join
short_songs = Song.select().join(Album).where((Album.name == 'Repentless') and (Song.length < 5))

for song in short_songs:
    print(song)


# DELETE
Album.get(Album.name == 'Reign in Blood').delete_instance()

for i in Album.select():
    print('album')

short_songs = Song.select().join(Album).where((Album.name == 'Repentless') and (Song.length < 5))

for song in short_songs:
    print('song')

