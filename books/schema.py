import graphene
from graphene_django import DjangoObjectType, DjangoListField
from .models import Book, Library


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ("id", "user", "name", "author_name", "release_year", "library")

# class Query(graphene.ObjectType):
#     all_books = DjangoListField(BookType)  # Specifying what type of data will come and what type will be obtained.


# ------

class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)  # DjangoListField and graphene.List methods do the same thing

    def resolve_all_books(root, info):  # To use filters on the fetched data, a function with root and
        # info parameters must be created
        return Book.objects.filter(release_year__gte=2020)


schema = graphene.Schema(query=Query)
