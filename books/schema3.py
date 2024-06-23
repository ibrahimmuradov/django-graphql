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
    all_books = DjangoListField(BookType)
    all_libraries = DjangoListField(LibraryType)  # multiple queries can be used this way

    def resolve_all_books(root, info):
        return Book.objects.filter(release_year__gte=2020)

    def resolve_all_libraries(root, info):
        return Library.objects.all()


schema = graphene.Schema(query=Query)


# query{
#   allBooks{
#     id
#     name
#   }
#   allLibraries{
#     id
#     name
#   }
# }

