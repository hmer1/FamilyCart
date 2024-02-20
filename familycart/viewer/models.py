from django.db.models import (
    DO_NOTHING, CharField, DateField, DateTimeField, ForeignKey, IntegerField,
    Model, TextField
)


class Genre(Model):
    objects = None
    name = CharField(max_length=128)

    def __str__(self):
        return str(self.name)


class Movie(Model):
    objects = None
    title = CharField(max_length=128)
    genre = ForeignKey(Genre, on_delete=DO_NOTHING)
    rating = IntegerField()
    released = DateField()
    description = TextField()
    created = DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

