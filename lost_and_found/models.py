from distutils.command.upload import upload
from django.db import models
from PIL import Image

# Create your models here.
class MissingPerson(models.Model):
    name = models.CharField(max_length=100)
    # date_of_birth = models.DateField()
    birth_mark = models.TextField(null=True)
    image = models.ImageField(upload_to='missing_people_images')
    # date_missing = models.DateField()
    place_seen_last_time = models.TextField()

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        new_img = (200, 200)
        img.thumbnail(new_img)
        img.save(self.image.path)
        return