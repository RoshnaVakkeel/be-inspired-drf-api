from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    '''
    Profile model
    Extends user model
    '''
    class AgeGroup(models.TextChoices):
        """
        A class for the age_group key
        Contains different age ranges to choose from
        """
        TEENAGER = 'Teenager (10 - 18)',
        YOUNGADULT = 'Young Adult (19 - 25)',
        ADULT = 'Adult (26 - 40)',
        MIDDLEAGED = 'Middle Aged (41 - 60)',
        SENIOR = 'Senior (>61)',

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True)
    age_group = models.CharField(
        max_length=50,
        choices=AgeGroup.choices
        )
    brief_bio = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    # Default profile image
    image = models.ImageField(
        upload_to='images/', default='../user_pixabay_mcfz1f'
    )

    class Meta:
        '''
        Orders Profile objects in reverse order of when they were created
        '''
        ordering = ['-created_on']

    def __str__(self):
        ''' Returns the string representation of a model instance
        (dunder string method)
        '''
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    # Creates a Profile object automatically when a User is created
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
