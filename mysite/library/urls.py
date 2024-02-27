from django.urls import path

from . import views

urlpatterns = [
    path("hello", views.hello_world, name="hello"),
    path("books", views.add_book, name="add_book"),
    path("books/<int:id>", views.delete)
]


# GET    /books             ->  retrieve all books data
# GET    /books/123         ->  retrieve the book with id 123
# POST   /books    (+body)  ->  create one book with the given data
# DELETE /books/123         ->  delete the book with id 123