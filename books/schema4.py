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
    all_books = graphene.Field(BookType, id=graphene.Int())  # single object data can be retrieved this way,
    # graphene.Field method states that a single field is used,
    # graphene.Int() method specifies the type of field to use
    all_book_libraries = graphene.List(LibraryType, book_id=graphene.Int())

    def resolve_all_books(root, info, id):
        return Book.objects.get(pk=id)

    def resolve_all_book_libraries(root, info, book_id):
        try:
            book = Book.objects.get(pk=book_id)
            return book.library.all()
        except Book.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)

