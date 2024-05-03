import typing
import strawberry


@strawberry.type
class Book:
    title: str
    author: str


def get_books():
    return [
        Book(
            title="How The World Really Works",
            author="Vaclav Smil"
        )
    ]


@strawberry.type
class Query:
    books: typing.List[Book] = strawberry.field(resolver=get_books)


schema = strawberry.Schema(query=Query)
