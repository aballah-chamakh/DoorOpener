from django.db import models
from account.models import Profile
# Create your models here.
class Door(models.Model):
    owner = models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True)
    name = models.CharField(max_length=255)
    opened = models.BooleanField(default=False)

    def __str__(self):
        state = 'open'
        if self.opened == False  :
            stat = 'close'

        return self.name+' is '+state
