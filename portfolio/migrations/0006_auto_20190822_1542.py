# Generated by Django 2.2.4 on 2019-08-22 10:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_myusers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myusers',
            name='username',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
