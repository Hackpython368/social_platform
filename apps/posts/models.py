from django.db import models
from apps.accounts.models import User
from django.conf import settings 

# Create your models here.
class Post(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="owener"
    )

    content = models.TextField()


    like_count = models.IntegerField(default=0)

    comment_count = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.email
    

class Like(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="likes"
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="likes"
    )

    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:

        unique_together = ('user','post')

    def __str__(self):
        return self.user.email
    

    @classmethod
    def add_like(self, user, id):
        json , created = self.objects.get_or_create(user=user,post=id)
        
        if not created:
            json.delete()
        return created
    
class Comment(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    comment_text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return Post.user
    

    