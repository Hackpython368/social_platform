from django.db import models
from django.conf import settings

# Create your models here.


class Follow(models.Model):

    follower = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='follower')
    following = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='following')

    created_at = models.DateField(auto_now_add=True)

    class Meta:

        unique_together = ('follower','following')

    
    def __str__(self):
        return f"{self.follower.email} follow {self.following.email}"
    
    @classmethod
    def user_follower(cls, follower, following):

        if follower == following:
            raise ValueError("User are not allowed to follow himself!!")
        
        follow , created = cls.objects.get_or_create(
            follower = follower,
            following = following
        )

        return follow , created
    
    @classmethod
    def user_unfollow(cls, follower, following):

        if follower == following:
            raise ValueError("User are not allowed to unfollow himself!!")
        
        unfollow = cls.objects.get(follower=follower,following=following)

        if unfollow:
            unfollow.delete()
            return True
        
        return False
        




