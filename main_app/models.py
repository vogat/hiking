from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate(value):
    if value > 5 or value < 1:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )

# Create your models here.
class Trail(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    difficulty = models.IntegerField(validators=[validate])
    description = models.TextField(max_length=250)
    streetAddress = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    map = models.CharField(max_length=250)  

    def get_location_url(self):
        return f"https://www.google.com/maps?q={self.streetAddress}, {self.city}, {self.state}, {self.zip}"


    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'trail_id': self.id})