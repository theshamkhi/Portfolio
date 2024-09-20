# Generated by Django 4.2.6 on 2023-11-10 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0015_alter_portfolio_picture_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='picture',
            field=models.ImageField(upload_to='media/users/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='media/projects/'),
        ),
    ]
