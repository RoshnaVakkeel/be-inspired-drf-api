from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    '''
    Post model
    '''
    class Category(models.TextChoices):
        '''
        A class for the age_group key
        Contains different age ranges to choose from
        '''
        BOOKS = 'Books',
        MUSIC = 'Music',
        ART = 'Art',
        PERSON = 'Person',
        PLACE = 'Place',
        MOVIES = 'Movies',
        EVENT = 'Event'

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    category = models.CharField(
        max_length=50,
        choices=Category.choices
        )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/',
        default='../default_post_ludaix',
        blank=True
    )

    class Meta:
        '''
        Orders Posts objects in the order latest to old
        '''
        ordering = ['-created_on']

    def __str__(self):
        '''
        Returns the string representation of a model instance
        '''
        return f'{self.id} {self.title}'
