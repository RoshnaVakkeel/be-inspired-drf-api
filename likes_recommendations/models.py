from django.db import models
from django.contrib.auth.models import User
from recommendations.models import Recommendation


class LikeRecommendation(models.Model):
    '''
    LikeRecommendation model
    Related to User and Recommendation
    '''
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    recommendation = models.ForeignKey(
        Recommendation,
        on_delete=models.CASCADE,
        related_name='likes_recommendations',
        default=None,
        null=True,
        blank=True
        )

    class Meta:
        '''
        Orders Like objects in the order latest to old
        'unique_together' for single selection of post/recommendation
        '''
        ordering = ['-created_on']
        unique_together = ['owner', 'recommendation']

    def __str__(self):
        '''
        Returns the string representation of a model instance
        '''
        return f'{self.owner} {self.recommendation}'

