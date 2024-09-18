from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    stock = models.PositiveIntegerField()  

    def __str__(self):
        return f'{self.title} by {self.author}'


class Member(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    outstanding_debt = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    fee = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)

    def __str__(self):
        return f'{self.member.name} - {self.book.title}'
