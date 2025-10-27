from django.db import models
from django.contrib.auth.models import User
class Track(models.Model):

    STATUS_CHOICES = [
        (1, 'Demo Version'),
        (2, 'Released Version')
    ]
    PRIVATE_CHOICES = [
        (1, 'Private'),
        (2, 'Public')
    ]

    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    note_num =models.IntegerField()
    duration = models.DurationField()
    created_at = models.DateTimeField(auto_now_add=True)
    dere_st = models.IntegerField(choices=STATUS_CHOICES, default=1)
    privaty_ch = models.IntegerField(choices=PRIVATE_CHOICES, default=2)
    likes = models.IntegerField(default=0)
    cho_ones = models.ManyToManyField(User, related_name='featured_tracks', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    authpr = models.ForeignKey(User, on_delete=models.CASCADE)
# Create your models here.
