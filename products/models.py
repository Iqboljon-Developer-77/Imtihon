from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import CustomUser


class CategoryComputer(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'category_computer'

    def __str__(self):
        return self.name


class Computers(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(CategoryComputer, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='books/', default='default_img/default_book_img.png')

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        db_table = 'computers'

    def __str__(self):
        return self.title


class Made(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'author'

    def __str__(self):
        return f'{self.name}'


class ComputerMade(models.Model):
    computer = models.ForeignKey(Computers, on_delete=models.CASCADE)
    made = models.ForeignKey(Made, on_delete=models.CASCADE)

    class Meta:
        db_table = 'computer_made'

    def __str__(self):
        return f'{self.computer.title} - {self.made.name}'


class Review(models.Model):
    comment = models.CharField(max_length=200)
    star_given = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    computer = models.ForeignKey(Computers, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        db_table = 'review'

    def __str__(self):
        return f'{self.star_given} - {self.computer.title} - {self.user.username}'
