import graphene
from graphene_django import DjangoObjectType, DjangoListField
from .models import Book, Library


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ("id", "user", "name", "author_name", "release_year", "library")


class LibraryType(DjangoObjectType):
    class Meta:
        model = Library
        fields = ("id", "name", "about")


class Query(graphene.ObjectType):
    all_books = graphene.Field(BookType, id=graphene.Int())

    def resolve_all_books(root, info, id):
        return Book.objects.get(pk=id)


schema = graphene.Schema(query=Query)

