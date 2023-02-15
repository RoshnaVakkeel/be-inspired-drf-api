from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from recommendations.models import Recommendation


class Like(models.Model):
    '''
    Like model
    Related to User, Post and Recommendation
    '''
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='likes',
        default=None,
        null=True,
        )
    recommendation = models.ForeignKey(
        Recommendation,
        on_delete=models.CASCADE,
        related_name='likes',
        default=None,
        null=True,
        )

    class Meta:
        '''
        Orders Like objects in the order latest to old
        'unique_together' for single selection of post/recommendation
        '''
        ordering = ['-created_on']
        unique_together = ['owner', 'post'], ['owner', 'recommendation']

    def __str__(self):
        '''
        Returns the string representation of a model instance
        '''
        return f'{self.owner} {self.post} {self.recommendation}'
