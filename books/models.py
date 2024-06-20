from django.db import models
from services.mixin import DateMixin
from django.contrib.auth import get_user_model

User = get_user_model()


class Library(DateMixin):
    name = models.CharField(max_length=200)
    about = models.TextField()

    def __str__(self):
        return self.name


class Book(DateMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    author_name = models.CharField(max_length=200)
    release_year = models.PositiveIntegerField()
    library = models.ManyToManyField(Library)

    def __str__(self):
        return self.name



