from django.db import models


class Author(models.Model):
    fullname = models.TextField(max_length=200, unique=True)
    born_date = models.DateField()
    born_location = models.TextField()
    description = models.TextField()
    #created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.fullname}"

class Tag(models.Model):
    name = models.TextField(unique=True)

    def __str__(self):
        return f"{self.name}"



class Quote(models.Model):
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None, null=True)
    quote = models.TextField()
    #created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quote}"

