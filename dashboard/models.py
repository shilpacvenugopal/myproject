
import uuid
import os
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile


class Table1(models.Model):
    class Meta:
        db_table = '"dashboard_table1"'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)

class Table2(models.Model):
    class Meta:
        db_table = '"dashboard_table2"'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey('dashboard.Table1', on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=255, blank=True, null=True)
    age = models.SmallIntegerField(default=0, null=True, blank=True)
    blood_group = models.CharField(max_length=255, blank=True, null=True)

### Model for image upload
class ConvertImageToWebP:
    @classmethod
    def convert_to_webp(cls, image):
        img = Image.open(image)
        if img.format not in ['JPEG', 'PNG']:
            raise ValueError("Unsupported image format. Only JPG and PNG are supported.")

        buffer = BytesIO()
        img.save(buffer, format="WEBP")
        webp_file = InMemoryUploadedFile(buffer, None, os.path.splitext(image.name)[0] + ".webp", 'image/webp',
                                         buffer.tell(), None)
        return webp_file


class ImageModel(models.Model):
    image = models.ImageField(upload_to='images')

    def save(self, *args, **kwargs):
        if self.image:
            webp_file = ConvertImageToWebP.convert_to_webp(self.image)
            self.image = webp_file
        super().save(*args, **kwargs)



