import graphene
from graphene_django import DjangoObjectType
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
    all_book_libraries = graphene.List(LibraryType, book_id=graphene.Int())
    libraries = graphene.List(LibraryType)

    def resolve_all_books(root, info, id):
        return Book.objects.get(pk=id)

    def resolve_all_book_libraries(root, info, book_id):
        try:
            book = Book.objects.get(pk=book_id)
            return book.library.all()
        except Book.DoesNotExist:
            return None

    def resolve_libraries(root, info):
        return Library.objects.all()


class LibraryMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    library = graphene.Field(LibraryType)

    @classmethod
    def mutate(cls, root, info, id):
        try:
            library = Library.objects.get(pk=id)
            library.delete()

            return None
        except Library.DoesNotExist:
            return None


class Mutation(graphene.ObjectType):
    delete_library = LibraryMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)



