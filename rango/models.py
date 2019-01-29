from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Category(models.Model):
    max_name_length = 128
    name = models.CharField(max_length=max_name_length, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Page(models.Model):
    max_title_length=128
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=max_title_length)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):  # For Python 2, use __unicode__ too
        return self.title
