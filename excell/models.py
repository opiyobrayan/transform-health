from django.db import models

# Create your models here.
class PartnerFile(models.Model):
     file_name=models.FileField(upload_to='partners')
     created=models.DateTimeField(auto_now_add=True)
     activated=models.BooleanField(default=False)

     def __str__(self):
        return f'File Id:{self.id}'
