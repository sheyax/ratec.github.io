from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class post(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    ctype = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    Interest = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('event-testinfopage')



class ourevents(models.Model):
    event_name = models.CharField(max_length=100)
    info = models.TextField(null=True)
    date_of_event = models.DateField(default=timezone.now)
    organizer = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.event_name
    
            
class Photo(models.Model):
    file = models.ImageField()
    description = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'photo'
        verbose_name_plural = 'photos'