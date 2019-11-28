from django.db import models

# Create your models here.
class resourcegroup(models.Model):
    ResourceGroupName = models.CharField(max_length=100)
    ResourceId = models.CharField(max_length=200)
    Location = models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = "ResourceGroup"
    def __str__(self):
        return self.ResourceGroupName

class resource(resourcegroup):
    Name = models.CharField(max_length=100)
    ResourceType = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Resource"
    def __str__(self):
        return self.Name
        
class Hero(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    
    def __str__(self):
        return self.name