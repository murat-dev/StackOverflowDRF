from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Problem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='problems')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.title


class CodeImage(models.Model):
    image = models.ImageField(upload_to='images')
    problem = models.ForeignKey('Problem', on_delete=models.CASCADE, related_name='images')


class Reply(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name='replies')
    body = models.TextField()
    image = models.ImageField(upload_to='replies', blank=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='replies')
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.problem}: {self.body}'


    class Meta:
        ordering = ('created',)

class Comment(models.Model):
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='comments')

    def __str__(self):
        return self.comment

    class Meta:
        ordering = ('-created',)