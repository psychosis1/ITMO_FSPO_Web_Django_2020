# Generated by Django 3.0.5 on 2020-05-14 11:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0006_auto_20200514_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carowner',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
