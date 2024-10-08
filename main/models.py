from django.db import models

class PreviewImage(models.Model):
    image = models.ImageField(upload_to='images/')
    description = models.TextField()

    def __str__(self):
        return self.description
class Contact(models.Model):
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f'{self.phone} - {self.email}'
