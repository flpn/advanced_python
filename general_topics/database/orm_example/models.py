import peewee


db = peewee.SqliteDatabase('mydb.db')


class Album(peewee.Model):
    name = peewee.CharField()
    artist = peewee.CharField()
    release = peewee.DateTimeField()

    def __str__(self):
        return '{} | {} | {}'.format(self.name, self.artist, self.release)

    class Meta:
        database = db


class Song(peewee.Model):
    album = peewee.ForeignKeyField(Album)
    name = peewee.CharField()
    length = peewee.FloatField()

    def __str__(self):
        return '{} | {} | {}'.format(self.album.name, self.name, self.length)

    class Meta:
        database = db
