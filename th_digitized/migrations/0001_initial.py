# Generated by Django 4.1.2 on 2022-10-16 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Organization Name')),
                ('website', models.URLField(verbose_name='website link')),
                ('bio', models.TextField()),
                ('headquater', models.CharField(max_length=200, verbose_name='Headquater')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
