from django.db import models

# Create your models here.
class Books(models.Model):
    book_title=models.CharField(max_length=200)
    Author_name=models.CharField(max_length=200)
    Genre=models.CharField(max_length=200)
    Review=models.IntegerField()
    Favorite=models.BooleanField()

    def __str__(self):
        return self.book_title
    class Meta:
        ordering=['id']