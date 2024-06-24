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


class LibraryMutation(graphene.Mutation):  # mutations are used for crud operations in the database
    class Arguments:
        name = graphene.String(required=True)  # Specify the argument for mutation
        about = graphene.String(required=True)

    library = graphene.Field(LibraryType)  # output field of the mutation

    @classmethod
    def mutate(cls, root, info, name, about):  # class method that performs the actual mutation
        library = Library(name=name, about=about)  # a new Library object is created
        library.save()  # save object to db
        return LibraryMutation(library=library)  # returns an instance of LibraryMutation with the newly
        # created library object


class Mutation(graphene.ObjectType):  # this class for defines the root for all mutations in
    # the GraphQL schema
    add_library = LibraryMutation.Field() # this means that the add_library mutation can be
    # executed in GraphQL queries.

schema = graphene.Schema(query=Query, mutation=Mutation)


# mutation {
#   addLibrary(name: "New Library", about: "New Library About") {
#     library {
#       name
#       about
#     }
#   }
# }
