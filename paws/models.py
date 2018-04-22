from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
class Paws(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    createdAt = models.DateTimeField(default=datetime.now,blank=True, null=True)
    fromUserId = models.ForeignKey(User, on_delete=models.CASCADE)
    number_of_likes = models.IntegerField(default=0)
    class Meta:
        verbose_name_plural = "Paws"
    def __str__(self):
        return self.title

class Comments(models.Model):
    fromUserId = models.ForeignKey(User, on_delete= models.CASCADE)
    toPawsId = models.ForeignKey(Paws, on_delete = models.CASCADE)
    comment_content = models.TextField() 
    class Meta:
        verbose_name_plural = "Comments"
    def __str__(self):
        return self.comment_content
    
  

class Follow_Up (models.Model):
    fromUserId = models.ForeignKey(User,on_delete=models.CASCADE)
    toPawsId = models.ForeignKey(Paws,on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Follow_Up"
    def __str__(self):
        return self.fromUserId + " follow" + self.toPawsId