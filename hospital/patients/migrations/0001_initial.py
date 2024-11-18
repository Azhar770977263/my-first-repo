# Generated by Django 5.1.1 on 2024-11-02 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='unknown', max_length=30)),
                ('last_name', models.CharField(default='unknown', max_length=30)),
                ('age', models.PositiveBigIntegerField(default=18)),
                ('image', models.ImageField(null=True, upload_to='images/%y/%m/%d')),
                ('files_report', models.FileField(null=True, upload_to='files/%y/%m/%d')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('report', models.TextField(max_length=200)),
            ],
        ),
    ]