from django.db import models

# Create your models here.

class Product(models.Model):
    prod_name=models.CharField(max_length=100)
    prod_price=models.IntegerField()
    prod_desc = models.TextField()
    prod_img = models.ImageField(upload_to='products/')
    prod_qty = models.IntegerField()
    # anytime you make changes to the models file you must make and run migrations
    # python manage.py makemigrations
    # python manage.py migrate
    # python manage.py runserver