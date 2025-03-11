from django.db import models

# Create your models here.
# I added all the code below
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)
# once I write code above
# I write in terminal: 'python manage.py makemigrations'
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories' # to change item name in django administration
    def __str__(self):# to show/display (category)names
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    #text field longer than char field
    understanding = models.FloatField()
    image = models.ImageField(upload_to='image', blank=True, null=True)
    #python will create this folder for us if it doesn't exist
    watched = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    #if user is deleted all items will also be deleted
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
