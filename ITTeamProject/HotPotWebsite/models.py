from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# Create your models here.

class MenuCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)

    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(MenuCategory, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Dish(models.Model):
    category = models.ForeignKey(MenuCategory)
    title = models.CharField(max_length=128, unique=True)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    zipcode = models.CharField(max_length=128,blank=True)
    headpicture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username


