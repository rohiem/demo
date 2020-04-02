# Generated by Django 2.2.11 on 2020-04-02 11:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20200326_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='User',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='notes',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]