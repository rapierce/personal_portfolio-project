from django.db import models

class project(models.Model):
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=100)
    about_project = models.TextField()
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return(self.title)
