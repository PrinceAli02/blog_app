# Generated by Django 4.2.11 on 2024-05-14 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_commentlike_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='postlike',
            name='like',
            field=models.BooleanField(default=True),
        ),
    ]