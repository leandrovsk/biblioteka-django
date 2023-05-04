from django.db import models
from users.models import User


class Followings(models.Model):
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"<following {self.id} = {self.books}]>"


class Book(models.Model):
    title = models.CharField(max_length=120)
    sinopse = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    year = models.DateTimeField(auto_now_add=True)

    collaborator = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="books"
    )

    user = models.ManyToManyField(
        User, through=Followings, related_name="books"
    )

    def __str__(self) -> str:
        return f"<Book {self.id} = {self.title}]>"