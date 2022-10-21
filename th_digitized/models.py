from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Partner(models.Model):
    name=models.CharField('Organization Name',max_length=200)
    logo=models.CharField('logo', default='logo',max_length=300)
    website=models.URLField('website link',max_length=300)
    bio=models.TextField()
    headquater=models.CharField('Headquater',max_length=200)
    image=models.ImageField('Organization logo',blank=True,null=True)

    def __str__(self):

        return self.name

class Workplan(models.Model):
    name=models.CharField('file name',max_length=200)
    owner=models.CharField('Owner',max_length=200)
    pdf=models.FileField(upload_to='uploads')
    cover=models.ImageField()

    def __str__(self):
        return self.owner


