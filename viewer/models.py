from django.db.models import (
    DO_NOTHING, CharField, DateField, DateTimeField, ForeignKey, IntegerField,
    Model, TextField
)


class Category(Model):
    objects = None
    name = CharField(max_length=128)

    def __str__(self):
        return str(self.name)


class Product(Model):
    objects = None
    title = CharField(max_length=128)
    category = ForeignKey(Category, on_delete=DO_NOTHING)
    quantity = IntegerField()
    released = DateField()
    description = TextField()
    created = DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

