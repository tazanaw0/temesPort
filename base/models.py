from django.db import models

#Photo model defined to store information about different photos 
class Photo(models.Model):

 #Choices defined for our category field
    CATEGORY_CHOICES = [
        ('portrait', 'Portrait Photography'),
        ('landscape', 'Landscape Photography'),
        ('street', 'Street Photography')
    ]

    #Fields for our Photo Model
    title = models.CharField(max_length=100) #Title of our image 
    image = models.ImageField(upload_to='photos/') # Image file
    description = models.TextField(blank=True) #Description is optional 
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES) #Category of the photo
    created_at = models.DateTimeField(auto_now_add=True) #Timestamp when photo is created

    def __str__(self):
        return self.title #String representation of our model
    

