# Generated by Django 5.1.1 on 2024-11-02 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctors',
            name='image',
            field=models.ImageField(null=True, upload_to='images/%y/%m/%d'),
        ),
    ]