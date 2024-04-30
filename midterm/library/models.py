from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Author(Person):
    age = models.IntegerField(default=18)
    birth_date = models.DateField()


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    established_date = models.DateField()

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title


class BookInstance(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    due_back = models.DateField()
    is_available = models.BooleanField(default=True)
    borrower = models.ForeignKey('Customer', on_delete=models.CASCADE, null=True, blank=True)
    borrowed_date = models.DateField(null=True, blank=True)


class Customer(Person):
    username = models.CharField(max_length=155)
