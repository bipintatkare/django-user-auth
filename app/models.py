from django.db.models import (
    Model, 
    CharField, 
    EmailField, 
    PositiveIntegerField,
    TextField
)


class User(Model):

    first_name = CharField(max_length=100, default="")
    last_name = CharField(max_length=100, default="")
    email = EmailField(unique=True)

    password = CharField(max_length=255, default="")
    contact = PositiveIntegerField(default=0)
    address = TextField()

    def __str__(self):

        return self.first_name