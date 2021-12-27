from django.conf import settings
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    photo = models.ImageField(blank=True, upload_to='insta/post/%Y/%m/%d')  # pip install pillow 해야함.
    tag_set = models.ManyToManyField('Tag', blank=True)
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # return f'Custom Post objects ({self.id})'
        return self.message

    class Meta:
        ordering = ['-id']

    def message_length(self):
        return len(self.message)

    message_length.short_description = '메세지 글자수'


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, limit_choices_to={'is_public': True})  # post_id
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    # post_set = models.ManyToManyField(Post)

    def __str__(self):
        return self.name
