from django.db import models

class Posts(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
