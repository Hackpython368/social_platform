from django.contrib import admin
from .models import Post,Like,Comment



class CustomPostView(admin.ModelAdmin):
    list_display = ('id','user','content','like_count','comment_count')
# Register your models here.

admin.site.register(Post,CustomPostView)
admin.site.register(Like)
admin.site.register(Comment)