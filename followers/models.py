from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    '''
    Class for the Follower model.
    'owner_following' is a User who is following another User.
    'followed' is a User who is followed by the 'owner'.
    The related_name attribute differentiates 'owner' and 'followed'
    '''
    owner_following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following'
        )
    followed = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='followed'
        )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        # 'unique_together' avoids duplicates
        ordering = ['-created_on']
        unique_together = ['owner_following', 'followed']

    def __str__(self):
        return f'{self.owner} {self.followed}'