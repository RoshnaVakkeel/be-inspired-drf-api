from django.db import models
from django.contrib.auth.models import User

class Recommendation(models.Model):
    '''
    Recommendation model
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

    class PriceCategory(models.TextChoices):
        """
        Price categories for the user to choose
        """
        FREE = 'Free',
        CHEAP = '€',
        AVERAGE = '€€',
        ABOVEAVERAGE = '€€€',
        EXPENSIVE = '€€€€',

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    category = models.CharField(
        max_length=50,
        choices=Category.choices
        )
    price_category = models.CharField(
        max_length=50,
        choices=PriceCategory.choices
        )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)
    reason = models.TextField(blank=True)   
    image = models.ImageField(
        upload_to='images/',
        default='../default_post_l2kfwu',
        blank=True
    )

    class Meta:
        '''
        Orders Recommendation objects in the order latest to old
        '''
        ordering = ['-created_on']

    def __str__(self):
        ''' 
        Returns the string representation of a model instance
        '''
        return f'{self.id} {self.title}'